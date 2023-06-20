# Telegram Package
[![Release](https://github.com/obervinov/telegram-package/actions/workflows/release.yml/badge.svg)](https://github.com/obervinov/telegram-package/actions/workflows/release.yml)
[![CodeQL](https://github.com/obervinov/telegram-package/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/obervinov/telegram-package/actions/workflows/github-code-scanning/codeql)
[![Tests and checks](https://github.com/obervinov/telegram-package/actions/workflows/tests.yml/badge.svg)](https://github.com/obervinov/telegram-package/actions/workflows/tests.yml)

![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/obervinov/telegram-package?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/obervinov/telegram-package?style=for-the-badge)
![GitHub Release Date](https://img.shields.io/github/release-date/obervinov/telegram-package?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/obervinov/telegram-package?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/obervinov/telegram-package?style=for-the-badge)

## <img src="https://github.com/obervinov/_templates/blob/main/icons/book.png" width="25" title="about"> About this project
This is an additional implementation compared to the **telebot** module.

This module is designed for quick initialization, authorization and rendering of various _buttons/widgets_ for telegram bot.

## <img src="https://github.com/obervinov/_templates/blob/main/icons/github-actions.png" width="25" title="github-actions"> GitHub Actions
| Name  | Version |
| ------------------------ | ----------- |
| GitHub Actions Templates | [v1.0.4](https://github.com/obervinov/_templates/tree/v1.0.4) |


## <img src="https://github.com/obervinov/_templates/blob/main/icons/requirements.png" width="25" title="functions"> Supported functions
- Creating a connection to the telegram api and initializing the objects necessary for the bot to function (_parser_, _format_, _types_, _etc_)
- Generating an inline keyboard button with a matrix of the specified size from the passed elements

## <img src="https://github.com/obervinov/_templates/blob/main/icons/requirements.png" width="25" title="functions"> Data structure in Vault
The structure of storing the bot token in the **Vault**
```bash
# token data
 % vault kv get ${mount_point}/configuration/telegram
========= Secret Path =========
configuration/data/telegram

======= Metadata =======
Key                Value
---                -----
created_time       2023-03-26T08:00:00.000000000Z
custom_metadata    <nil>
deletion_time      n/a
destroyed          false
version            1

====== Data ======
Key         Value
---         -----
token       123456qwerty
```


The `policy` required by the module when interacting with **Vault**
An example of a policy with all the necessary rights and a description can be found [here](tests/vault/policy.hcl)

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
 Simple
```python
# import module
from telegram import TelegramBot

# init class objects
telegram_bot = TelegramBot(vault_client).telegram_bot

# decorator
@telegram_bot.message_handler(commands=['start'])
def start_message(message):
    telegram_bot.send_message(
        message.chat.id,
        f"Hi, <b>{message.chat.username}</b>! \u270B"
    )  
```

Inline keyboard
```python
# import module
from telegram import TelegramBot

# init class objects
telegram_bot = TelegramBot(vault_client).telegram_bot

# decorator
@telegram_bot.message_handler(commands=['start'])
def start_message(message):
    markup = telegram_bot.create_inline_buttons(
        [
            'Jan', 'Feb', 'Mar', 'Apr',
            'May', 'June', 'July', 'Aug',
            'Sept', 'Oct', 'Nov', 'Dec'
        ],
        4
    )
    telegram_bot.send_message(
        message.chat.id,
        f"\U0001F4C5 Select month for the creating report",
        reply_markup=markup
    )
```
<img src="https://github.com/obervinov/telegram-package/blob/main/doc/inline_keyboard_example.png" width="750" title="inline_keyboard_example">
