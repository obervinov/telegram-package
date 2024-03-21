"""
This is an additional implementation compared to the telebot module.
This module is designed for quick initialization, authorization
and rendering of various buttons/widgets for telegram bots.
"""
import os
import time
import telebot
from telebot.apihelper import ApiTelegramException
from messages import Messages
from logger import log
from vault import VaultClient
from .exceptions import VaultInstanceNotSet, BotNameNotSet, InvalidTokenConfiguration, FailedToCreateInstance


class ExceptionHandler(telebot.ExceptionHandler):
    """
    This class contains methods for handling exceptions that occur during the operation of the bot.
    """
    def handle(self, exception):
        attempt_timeout = 60
        log.error('[Bot]: Error creating the bot instance: %s', exception)
        if exception.error_code == 409:
            # Conflict between the more then one bot with the same token
            # Just trying to wait for the first bot to be stopped
            time.sleep(attempt_timeout)
            log.warning('[Bot]: Conflict between the more then one bot with the same token. Trying to wait for the first bot to be stopped...')
        elif exception.error_code == 400:
            log.error('[Bot]: Query execution error: %s', exception)
        else:
            log.error('[Bot]: Error: %s\nNext polling attempt in %s seconds...', exception, attempt_timeout)
            raise FailedToCreateInstance("Failed to create the bot instance.") from exception


class TelegramBot:
    """
    This class contains methods for quick initialization, authorization
    and rendering of various buttons/widgets for telegram bots.

    Args:
        :param name (str): the name of the bot.
        :param vault (any): Configuration for initializing the Vault client.
            - (object) VaultClient instance for interacting with the Vault API.
            - (dict) Configuration for initializing a VaultClient instance in this class.
        :param parse_mode (str): message parser. It can be HTML or MARKDOWN.
        :param messages_config (str): path to the messages configuration file with templates.

    Raises:
        :raises VaultInstanceNotSet: if the Vault instance is not set.
        :raises BotNameNotSet: if the bot name is not set.
        :raises InvalidTokenConfiguration: if the Telegram token is not set.
        :raises FailedToCreateInstance: if the bot instance cannot be created.

    Returns:
        None

    Example:
        >>> bot = TelegramBot()
    """
    def __init__(
        self,
        name: str = None,
        vault: any = None,
        parse_mode: str = 'HTML',
        messages_config: str = None
    ) -> None:
        """
        A method for create a new telebot client instance.

        Args:
            :param name (str): the name of the bot.
            :param vault (any): Configuration for initializing the Vault client.
                - (object) VaultClient instance for interacting with the Vault API.
                - (dict) Configuration for initializing a VaultClient instance in this class.
            :param parse_mode (str): message parser. It can be HTML or MARKDOWN.
            :param messages_config (str): path to the messages configuration file with templates.

        Raises:
            :raises VaultInstanceNotSet: if the Vault instance is not set.
            :raises BotNameNotSet: if the bot name is not set.
            :raises InvalidTokenConfiguration: if the Telegram token is not set.
            :raises FailedToCreateInstance: if the bot instance cannot be created.

        Returns:
            None
        """
        # Extract the bot name from the environment variable or the parameter
        if os.environ.get('TELEGRAM_BOT_NAME', None):
            self.name = os.environ.get('TELEGRAM_BOT_NAME')
        elif name:
            self.name = name
        else:
            raise BotNameNotSet(
                "Telegram bot name is not set. "
                "Please, set the TELEGRAM_BOT_NAME environment variable or pass the name parameter to the constructor."
            )

        # Initialize the Vault client
        if isinstance(vault, VaultClient):
            self._vault = vault
        elif isinstance(vault, dict):
            self._vault = VaultClient(
                name=vault.get('name', None),
                url=vault.get('url', None),
                approle=vault.get('approle', None)
            )
        else:
            log.error(
                '[class.%s] wrong vault parameters in Users(vault=%s), see doc-string',
                __class__.__name__,
                vault
            )
            raise VaultInstanceNotSet("Vault instance is not set. Please provide a valid Vault instance as instance or dictionary.")

        # Read the token from the Vault
        try:
            self.token = vault.read_secret(
                'configuration/telegram',
                "token"
            )
        except Exception as exception:
            log.error(
                '[class.%s] error reading the token from the Vault: %s',
                __class__.__name__,
                exception
            )
            raise InvalidTokenConfiguration("Telegram token is not set. Please provide a valid token in the Vault.") from exception

        # Create the bot instance
        self.telegram_bot = telebot.TeleBot(
            self.token,
            parse_mode=parse_mode,
            exception_handler=ExceptionHandler()
        )
        self.telegram_types = telebot.types
        self.callback_query = telebot.types.CallbackQuery
        self.messages = Messages(config_path=messages_config)

    def create_inline_markup(
        self,
        names: list = None,
        size: int = 3
    ) -> telebot.types.InlineKeyboardMarkup:
        """
        A method for generating inline keyboard button according to the specified parameters.

        Args:
            :param names (list): the name of the buttons in the form of a list.
            :param size (int): the number of buttons in a row. Default is 3.

        Returns:
            (telebot.types.InlineKeyboardMarkup) buttons
        """
        markup = self.telegram_types.InlineKeyboardMarkup()
        buttons = []
        for name in names:
            buttons.append(
                self.telegram_types.InlineKeyboardButton(
                    name,
                    callback_data=name
                )
            )
        for step in range(0, len(buttons), size):
            markup.row(*buttons[step:step+size])
        return markup

    def send_styled_message(
        self,
        chat_id: str = None,
        messages_template: dict = None,
        reply_markup: telebot.types.InlineKeyboardMarkup = None,
        progressbar: dict = None
    ) -> telebot.types.Message:
        """
        Send a formatted, beautiful message from the Messages text templates.

        Args:
            chat_id (str): The ID of the chat where the message will be sent.
            messages_template (dict): A dictionary containing the alias of the template to use and any keyword arguments to be passed to the template.
                The dictionary should contain the following keys:
                    - alias (str): The alias of the template to use.
                    - kwargs (dict): A dictionary containing any keyword arguments to be passed to the template.
            reply_markup (telebot.types.InlineKeyboardMarkup): The inline keyboard markup to be sent with the message.
            progressbar (dict): A dictionary containing the progress bar parameters.
                The dictionary should contain the following keys:
                    - current (int): The current value of the progress bar.
                    - total (int): The total value of the progress bar.

        Returns:
            telegram.telegram_types.Message: The message sent to the user.
        """
        try:
            if progressbar:
                progressbar_string = self.messages.render_progressbar(
                    total_count=progressbar['total'],
                    current_count=progressbar['current']
                )
            else:
                progressbar_string = None

            response = self.telegram_bot.send_message(
                chat_id=chat_id,
                text=self.messages.render_template(
                    template_alias=messages_template['alias'],
                    progressbar=progressbar_string,
                    **messages_template.get('kwargs', {})
                ),
                reply_markup=reply_markup,
            )
        except ApiTelegramException as api_exception:
            log.warning(
                '[Bot]: Error sending message to user %s: %s',
                chat_id,
                api_exception
            )
            response = None

        return response

    def launch_bot(self) -> None:
        """
        A method for start pulling the message with logging and exceptions.

        Args:
            None

        Returns:
            None

        Raises:
            :raises FailedToCreateInstance: if the bot instance cannot be created.
        """
        attempt_timeout = 60
        while True:
            log.info(
                '[Bot]: Starting bot %s...',
                self.name
            )
            self.telegram_bot.polling(timeout=attempt_timeout)
