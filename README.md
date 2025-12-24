# Telegram Package
[![Release](https://github.com/obervinov/telegram-package/actions/workflows/release.yaml/badge.svg)](https://github.com/obervinov/telegram-package/actions/workflows/release.yaml)
[![CodeQL](https://github.com/obervinov/telegram-package/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/obervinov/telegram-package/actions/workflows/github-code-scanning/codeql)
[![Tests and checks](https://github.com/obervinov/telegram-package/actions/workflows/pr.yaml/badge.svg)](https://github.com/obervinov/telegram-package/actions/workflows/pr.yaml)

![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/obervinov/telegram-package?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/obervinov/telegram-package?style=for-the-badge)
![GitHub Release Date](https://img.shields.io/github/release-date/obervinov/telegram-package?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/obervinov/telegram-package?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/obervinov/telegram-package?style=for-the-badge)

## <img src="https://github.com/obervinov/_templates/blob/main/icons/book.png" width="25" title="about"> About this project
This is an additional implementation compared to the **telebot** module.

This module is designed for quick initialization, authorization, rendering various _buttons/widgets_ and sending stylized messages for telegram-bots.


## <img src="https://github.com/obervinov/_templates/blob/main/icons/requirements.png" width="25" title="functions"> Supported functions
- Creating a connection to the telegram api and initializing the objects necessary for the bot to function (_parser_, _format_, _types_, _etc_)
- Generating an inline keyboard button with a matrix of the specified size from the passed elements
- Starting the bot polling process
- Sending or editing a stylized message to a user
- Deleting a message from chat
- Interception of invoked exceptions


## <img src="https://github.com/obervinov/_templates/blob/main/icons/requirements.png" width="25" title="functions"> Data structure in Vault
The structure of storing the bot token in the **Vault**
Configuration path: `${mount_point}/configuration/telegram`
```json
{
    "token": "1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZ"
}
```


The `policy` required by the module when interacting with **Vault**.
An example of a policy with all the necessary rights and a description can be found [here](tests/vault/policy.hcl).

## <img src="https://github.com/obervinov/_templates/blob/main/icons/stack2.png" width="20" title="install"> Installing with Poetry
```bash
tee -a pyproject.toml <<EOF
[tool.poetry]
name = myproject"
version = "1.0.0"
description = ""

[tool.poetry.dependencies]
python = "^3.12"
telegram = { git = "https://github.com/obervinov/telegram-package.git", tag = "v3.0.3" }

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
EOF

poetry install
```

## <img src="https://github.com/obervinov/_templates/blob/main/icons/config.png" width="25" title="usage"> Usage example
### Environment variables
| Name  | Description | Default value |
| ------------------- | ----------------- | ------ |
| `TELEGRAM_BOT_NAME` | Telegram bot name | `None` |

1. Create messages template file
```bash
tee -a configs/messages.json <<EOF
{
    "templates": {
        "test_message": {
            "text": "Hi, <b>{0}</b>! {1}\nAccess for your account - allowed {2}",
            "args": ["username", ":raised_hand:", ":unlocked:"]
        }
    }
}
```

- Simple usage
    ```python
    # import module
    from telegram import TelegramBot

    # init class objects
    telegram = TelegramBot(vault_client)
    bot = telegram.telegram_bot

    # decorator
    @bot.message_handler(commands=['start'])
    def start_message(message):
        telegram.send_styled_message(
            message.chat.id,
            messages_template={
                'alias': 'hello_message',
                'kwargs': {
                    'username': message.from_user.first_name
                }
            }
        )  
    
    # run bot pulling
    telegram.launch_bot()
    ```

- With inline keyboard
    ```python
    # import module
    from telegram import TelegramBot

    # init class objects
    telegram_bot = TelegramBot(vault_client).telegram_bot

    # decorator
    @telegram_bot.message_handler(commands=['start'])
    def start_message(message):
        markup = telegram_bot.telegram.create_inline_markup(
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

    # run bot pulling
    telegram.launch_bot()
    ```
    <img src="https://github.com/obervinov/telegram-package/blob/main/doc/inline_keyboard_example.png" width="750" title="inline_keyboard_example">


## <img src="https://github.com/obervinov/_templates/blob/main/icons/github-actions.png" width="25" title="github-actions"> GitHub Actions
| Name  | Version |
| ------------------------ | ----------- |
| GitHub Actions Templates | [v2.1.1](https://github.com/obervinov/_templates/tree/v2.1.1) |
