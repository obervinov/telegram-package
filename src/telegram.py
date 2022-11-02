######### THIS FUNCTION FROM TELEGRAM INIT AND AUTH #########

### MODULES AND VARS ###
import telebot
### MODULES AND VARS ###


class TelegramBot:

    def __init__(self, bot_name, vault) -> None:     
        self.bot_name = bot_name
        self.vault = vault

        telegram_token = str(self.vault.vault_read_secrets(f"{self.bot_name}-config/config","b_token"))
        self.telegram_bot = telebot.TeleBot(telegram_token, parse_mode="HTML")
        self.telegram_types = telebot.types