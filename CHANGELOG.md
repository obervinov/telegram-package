# Change Log
All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).



## v1.0.2 - 2023-03-29
### What's Changed
**Full Changelog**: https://github.com/obervinov/telegram-package/compare/v1.0.1...v1.0.2 by @obervinov in https://github.com/obervinov/telegram-package/pull/2
#### 🐛 Bug Fixes
* renamed the directory with the code to the name of the module - `telegram`
* fixed errors in the doc string and the general code format
#### 📚 Documentation
* updated and expanded the documentation in the file [README.md](https://github.com/obervinov/telegram-package/blob/v1.0.2/README.md)
#### 💥 Breaking Changes
* [changed the structure](https://github.com/obervinov/telegram-package/tree/v1.0.2#-data-structure-in-vault) of storing **bot token**
* removed `bot_name` argument in `TelegramBot.__init__`
* renamed argument `vault` -> `vault_client` and added new `parse_mode` in method `__init__()`
* added a new method [`create_inline_buttons()`](https://github.com/obervinov/telegram-package/blob/v1.0.2/telegram/telegram.py#L40) to create online keyboard buttons sent by the bot
#### 🚀 Features
* updated [GitHub Actions](https://github.com/obervinov/_templates/tree/v1.0.2) version to `v1.0.2`
* added [Tests](https://github.com/obervinov/telegram-package/tree/v1.0.2/tests)
* added logging events



## v1.0.1 - 2023-03-02
### What's Changed
**Full Changelog**: https://github.com/obervinov/telegram-package/compare/v1.0.0...v1.0.1 by @obervinov in https://github.com/obervinov/telegram-package/pull/1
#### 🐛 Bug Fixes
* updated the code in accordance with the recommendations of **flake8** and **pylint**
* adjusted [pyproject.toml](https://github.com/obervinov/telegram-package/blob/main/pyproject.toml) and [setup.py](https://github.com/obervinov/telegram-package/blob/main/setup.py) for package delivery
#### 📚 Documentation
* updated and expanded the documentation in the file [README.md](https://github.com/obervinov/telegram-package/blob/main/README.md)
#### 💥 Breaking Changes
* global **code recycling**: _removed old artifacts_ and _more comments added to the code_
#### 🚀 Features
* added github actions: **flake8**, **pylint** and **create release**
* added [SECURITY](https://github.com/obervinov/telegram-package/blob/main/SECURITY.md)
* added [ISSUE_TEMPLATE](https://github.com/obervinov/telegram-package/tree/main/.github/ISSUE_TEMPLATE)
* added [PULL_REQUEST_TEMPLATE](https://github.com/obervinov/telegram-package/tree/main/.github/PULL_REQUEST_TEMPLATE)
* added [CODEOWNERS](https://github.com/obervinov/telegram-package/tree/main/.github/CODEOWNERS)
* added [dependabot.yml](https://github.com/obervinov/telegram-package/tree/main/.github/dependabot.yml)



## v1.0.0 - 2022-11-04
### What's Changed
**Full Changelog**: https://github.com/obervinov/telegram-package/commits/v1.0.0
#### 💥 Breaking Changes
* Module release