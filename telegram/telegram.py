"""
This is an additional implementation compared to the telebot module.
This module is designed for quick initialization, authorization
and rendering of various buttons/widgets for telegram bots.
"""
import telebot


class TelegramBot:
    """
    This class contains methods for quick initialization, authorization
    and rendering of various buttons/widgets for telegram bots.
    """
    def __init__(
        self,
        vault: object = None,
        parse_mode: str = 'HTML'
    ) -> None:
        """
        A method for create a new telebot client instance.

        Args:
            :param vault (object): an instance with the vault client to receive a private token.
            :param parse_mode (str): message parser. It can be HTML or MARKDOWN.

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

    def create_inline_markup(
        self,
        names: list = None,
        size: int = None
    ) -> telebot.types.InlineKeyboardMarkup:
        """
        A method for generating inline keyboard button according to the specified parameters.

        Args:
            :param names (list): the name of the buttons in the form of a list.
            :param size (int): number of buttons per line.

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
