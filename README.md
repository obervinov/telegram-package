# Telegram Package
[![Release](https://github.com/obervinov/telegram-package/actions/workflows/release.yml/badge.svg)](https://github.com/obervinov/telegram-package/actions/workflows/release.yml)
[![CodeQL](https://github.com/obervinov/telegram-package/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/obervinov/telegram-package/actions/workflows/github-code-scanning/codeql)
[![Tests and checks](https://github.com/obervinov/telegram-package/actions/workflows/tests.yml/badge.svg?branch=main&event=pull_request)](https://github.com/obervinov/telegram-package/actions/workflows/tests.yml)

![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/obervinov/telegram-package?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/obervinov/telegram-package?style=for-the-badge)
![GitHub Release Date](https://img.shields.io/github/release-date/obervinov/telegram-package?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/obervinov/telegram-package?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/obervinov/telegram-package?style=for-the-badge)

## <img src="https://github.com/obervinov/_templates/blob/main/icons/book.png" width="25" title="about"> About this project
This is an additional implementation over the **telebot** module.

This module is designed for fast initialization and authorization of bot telegrams in the telegram api.

## <img src="https://github.com/obervinov/_templates/blob/main/icons/github-actions.png" width="25" title="github-actions"> GitHub Actions
| Name  | Version |
| ------------------------ | ----------- |
| GitHub Actions Templates | [v1.0.2](https://github.com/obervinov/_templates/tree/v1.0.2) |


## <img src="https://github.com/obervinov/_templates/blob/main/icons/requirements.png" width="25" title="functions"> Supported functions
- Authentication in api telegram
- Download `telebot.types`

## <img src="https://github.com/obervinov/_templates/blob/main/icons/stack2.png" width="20" title="install"> Installing
```bash
# Install current version
pip3 install git+https://github.com/obervinov/telegram-package.git#egg=vault
# Install version by branch
pip3 install git+https://github.com/obervinov/telegram-package.git@main#egg=vault
# Install version by tag
pip3 install git+https://github.com/obervinov/telegram-package.git@v1.0.0#egg=vault
```

## <img src="https://github.com/obervinov/_templates/blob/main/icons/config.png" width="25" title="usage"> Usage example
```python
"""Import module"""
from telegram import TelegramBot

"""Environment variables"""
bot_name = os.environ.get('BOT_NAME', 'pyinstabot-downloader')

"""Init class"""
Telegram = TelegramBot(bot_name, Vault)
telegram_bot = Telegram.telegram_bot

"""Decorators"""
@telegram_bot.message_handler(commands=['start'])
def start_message(message):
    answer = (
        f"Hi, <b>{message.chat.username}</b>! \u270B\n"
    )
    telegram_bot.send_message(message.chat.id, answer)  
```
