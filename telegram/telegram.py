"""
This is an additional implementation compared to the telebot module.
This module is designed for quick initialization, authorization and rendering of various buttons/widgets for telegram bots.
"""
import os
import time
import telebot
from messages import Messages
from logger import log
from vault import VaultClient
from .constants import DEFAULT_PARSE_MODE, DEFAULT_TIMEOUT
from .exceptions import VaultInstanceNotSet, BotNameNotSet, InvalidTokenConfiguration, FailedToCreateInstance


class ExceptionHandler(telebot.ExceptionHandler):
    """
    This class contains methods for handling exceptions that occur during the operation of the bot.
    """
    def handle(self, exception):
        if 'Error code: 409' in str(exception):
            # Conflict between the more then one bot with the same token
            # Just trying to wait for the first bot to be stopped
            log.warning('[Bot]: %s. Trying to wait for the first bot to be stopped...', exception)
            time.sleep(DEFAULT_TIMEOUT)
        if 'Error code: 400' in str(exception):
            # https://github.com/obervinov/telegram-package/issues/43
            log.error('[Bot]: Bad request to the Telegram API: %s', exception)
        else:
            log.error('[Bot]: Error: %s', exception)
            raise FailedToCreateInstance("Failed to create the bot instance.") from exception


class TelegramBot:
    """
    This class contains methods for quick initialization, authorization
    and rendering of various buttons/widgets for telegram bots.

    Attributes:
        :param name (str): the name of the bot.
        :param vault (any): Configuration for initializing the Vault client.
            - (object) VaultClient instance for interacting with the Vault API.
            - (dict) Configuration for initializing a VaultClient instance in this class.
        :param telegram_bot (telebot.TeleBot): the bot instance.
        :param telegram_types (telebot.types): the types of the telegram bot.
        :param callback_query (telebot.types.CallbackQuery): the callback query of the telegram bot.
        :param messages (Messages): the messages instance.

    Methods:
        :method create_inline_markup: generate inline keyboard button according to the specified parameters.
        :method send_styled_message: send a styled message to the user or edit an existing message.
        :method delete_message: delete a message.
        :method launch_bot: start pulling the message with logging and exceptions.

    Raises:
        :raises VaultInstanceNotSet: if the Vault instance is not set.
        :raises BotNameNotSet: if the bot name is not set.
        :raises InvalidTokenConfiguration: if the Telegram token is not set.
        :raises FailedToCreateInstance: if the bot instance cannot be created.
    """
    def __init__(
        self,
        name: str = None,
        vault: any = None,
        parse_mode: str = DEFAULT_PARSE_MODE,
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

        Examples:
            >>> from telegram import TelegramBot
            >>> bot = TelegramBot(
            ...     name='my_bot',
            ...     vault={
            ...         'namespace': 'my_namespace',
            ...         'url': 'http://my_vault_url',
            ...         'auth': {
            ...             'method': 'approle',
            ...             'role_id': 'my_role_id',
            ...             'secret_id': 'my_secret_id'
            ...         }
            ...     },
            ...     parse_mode='HTML',
            ...     messages_config='messages.yaml'
            ... )
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
                namespace=vault.get('namespace', None),
                url=vault.get('url', None),
                auth=vault.get('auth', None)
            )
        else:
            log.error('[Telegram]: wrong vault parameters in Users(vault=%s), see doc-string', vault)
            raise VaultInstanceNotSet("Vault instance is not set. Please provide a valid Vault instance as instance or dictionary.")

        # Read the token from the Vault
        token = vault.kv2engine.read_secret(path='configuration/telegram', key="token")
        if token is None:
            raise InvalidTokenConfiguration("Telegram token is not set. Please provide a valid token in the Vault.")

        try:
            # Create the bot instance
            self.telegram_bot = telebot.TeleBot(
                token=token,
                parse_mode=parse_mode,
                exception_handler=ExceptionHandler()
            )
            # Set additional attributes
            self.telegram_types = telebot.types
            self.callback_query = telebot.types.CallbackQuery
            self.messages = Messages(config_path=messages_config)
        except Exception as exception:
            raise FailedToCreateInstance("Failed to create the bot instance.") from exception

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
        **kwargs
    ) -> telebot.types.Message:
        """
        A method for sending a styled message to the user or editing an existing message.

        Args:
            chat_id (str): The ID of the chat where the message will be sent.
            messages_template (dict): A dictionary containing the alias of the template to use and any keyword arguments to be passed to the template.
                The dictionary should contain the following keys:
                    - alias (str): The alias of the template to use.
                    - kwargs (dict): A dictionary containing any keyword arguments to be passed to the template.
        Keyword Args:
            reply_markup (telebot.types.InlineKeyboardMarkup): The inline keyboard markup to be sent with the message.
            progressbar (dict): A dictionary containing the progress bar parameters.
                The dictionary should contain the following keys:
                    - current (int): The current value of the progress bar.
                    - total (int): The total value of the progress bar.
            editable_message_id (int): The ID of the message to be edited. Used to edit an existing message.

        Returns:
            telegram.telegram_types.Message: The message sent to the user.
        """
        # extract keyword arguments
        progressbar = kwargs.get('progressbar', None)
        reply_markup = kwargs.get('reply_markup', None)
        editable_message_id = kwargs.get('editable_message_id', None)

        if progressbar:
            progressbar_string = self.messages.render_progressbar(
                total_count=progressbar['total'],
                current_count=progressbar['current']
            )
        else:
            progressbar_string = None

        if editable_message_id:
            response = self.telegram_bot.edit_message_text(
                chat_id=chat_id,
                message_id=editable_message_id,
                text=self.messages.render_template(
                    template_alias=messages_template['alias'],
                    progressbar=progressbar_string,
                    **messages_template.get('kwargs', {})
                ),
                reply_markup=reply_markup,
            )
        else:
            response = self.telegram_bot.send_message(
                chat_id=chat_id,
                text=self.messages.render_template(
                    template_alias=messages_template['alias'],
                    progressbar=progressbar_string,
                    **messages_template.get('kwargs', {})
                ),
                reply_markup=reply_markup,
            )
        return response

    def delete_message(
        self,
        chat_id: str = None,
        message_id: int = None
    ) -> None:
        """
        A method for deleting a message.

        Args:
            chat_id (str): The ID of the chat where the message will be deleted.
            message_id (int): The ID of the message to be deleted.
        """
        self.telegram_bot.delete_message(
            chat_id=chat_id,
            message_id=message_id
        )
            

    def launch_bot(self) -> None:
        """
        A method for start pulling the message with logging and exceptions.
        """
        while True:
            log.info('[Bot]: Starting bot %s...', self.name)
            self.telegram_bot.polling(timeout=DEFAULT_TIMEOUT)
