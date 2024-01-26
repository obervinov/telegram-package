"""
This is an additional implementation compared to the telebot module.
This module is designed for quick initialization, authorization
and rendering of various buttons/widgets for telegram bots.
"""
import telebot
from telebot.apihelper import ApiTelegramException
from messages import Messages
from logger import log


class TelegramBot:
    """
    This class contains methods for quick initialization, authorization
    and rendering of various buttons/widgets for telegram bots.
    """
    def __init__(
        self,
        vault: object = None,
        parse_mode: str = 'HTML',
        messages_config: str = None
    ) -> None:
        """
        A method for create a new telebot client instance.

        Args:
            :param vault (object): an instance with the vault client to receive a private token.
            :param parse_mode (str): message parser. It can be HTML or MARKDOWN.
            :param messages_config (str): path to the messages configuration file with templates.

        Returns:
            None
        """
        self.token = vault.read_secret(
            'configuration/telegram',
            "token"
        )
        self.telegram_bot = telebot.TeleBot(
            self.token,
            parse_mode=parse_mode
        )
        self.telegram_types = telebot.types
        self.api_telegram_exception = ApiTelegramException
        self.messages = Messages(
            config_path=messages_config
        )

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
        reply_markup: telebot.types.InlineKeyboardMarkup = None
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

        Returns:
            telegram.telegram_types.Message: The message sent to the user.
        """
        try:
            response = self.telegram_bot.send_message(
                chat_id=chat_id,
                text=self.messages.render_template(
                    template_alias=messages_template['alias'],
                    **messages_template.get('kwargs', {})
                ),
                reply_markup=reply_markup,
            )
        except self.api_telegram_exception as exception:
            log.warning(
                '[Bot]: Error sending message to user %s: %s',
                chat_id,
                exception
            )
            response = None

        return response
