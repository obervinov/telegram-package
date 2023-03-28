"""
This is an additional implementation compared to the telebot module.
This module is designed for quick initialization, authorization
and rendering of various buttons/widgets for telegram bot.
"""
import telebot

class TelegramBot:
    """
    This class is an implementation over the telebot module.
    Contains methods for quick initialization, authorization
    and rendering of various buttons/widgets for telegram bot.
    """
    def __init__(
        self,
        vault_client: object = None,
        parse_mode: str = 'HTML'
    ) -> None:
        """
        A method for create a new telebot client instance.
        
        :param vault_client: An instance with the vault client to receive a private token.
        :type vault_client: object
        :default vault_client: None
        :param parse_mode: Message parser. It can be HTML or MARKDOWN.
        :type parse_mode: str
        :default parse_mode: HTML
        """
        self.token = vault_client.vault_read_secrets(
            'configuration/telegram',
            "token"
        )
        self.telegram_bot = telebot.TeleBot(
            self.token,
            parse_mode=parse_mode
        )
        self.telegram_types = telebot.types


    def create_inline_buttons(
        self,
        names: list = None,
        size: int = None
    ) -> str:
        """
        Method for generating inline keyboard button according to the specified parameters.

        :param names: The name of the buttons in the form of a list for generating markup.
        :type names: list
        :default names: None
        :param size: Number of buttons per line.
        :type size: int
        :default size: None
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
