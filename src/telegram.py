"""This is an additional implementation over the telebot module.
This module is designed for fast initialization and authorization of bot in the telegram api
"""
import telebot

class TelegramBot:
    """This class is an implementation over the telebot module.
    Contains methods for reading/placing/listing secrets with additional doping and exceptions.
    """
    def __init__(
        self,
        bot_name: str = None,
        vault: object = None
    ) -> None:
        """A function for create a new telebot client instance.
        :param bot_name: Bot name for current instance.
        :type bot_name: str
        :default bot_name: None
        :param vault: An instance with an initialized vault client for obtaining a private token.
        :type vault: object
        :default vault: None
        """
        self.telegram_token = vault.vault_read_secrets(
            f"{bot_name}-config/config",
            "b_token"
        )
        self.telegram_bot = telebot.TeleBot(self.telegram_token, parse_mode="HTML")
        self.telegram_types = telebot.types
