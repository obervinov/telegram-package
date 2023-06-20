# Change Log
All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).


## v1.1.3 - 2023-06-20
### What's Changed
**Full Changelog**: https://github.com/obervinov/telegram-package/compare/v1.1.2...v1.1.3 by @obervinov in https://github.com/obervinov/telegram-package/pull/18
#### 🐛 Bug Fixes
* [Fix badge with tests in README.md](https://github.com/obervinov/telegram-package/issues/15)
* [Bump vault-package to v2.0.1](https://github.com/obervinov/telegram-package/issues/17)
#### 🚀 Features
* [Fix the error that caused the workflow create_release to run twice - at pr/main](https://github.com/obervinov/telegram-package/issues/16)


## v1.1.2 - 2023-06-18
### What's Changed
**Full Changelog**: https://github.com/obervinov/telegram-package/compare/v1.1.1...v1.1.2 by @obervinov in https://github.com/obervinov/telegram-package/pull/14
#### 🐛 Bug Fixes
* [Fix work with transit dependencies in setup.py](https://github.com/obervinov/telegram-package/issues/13)


## v1.1.1 - 2023-06-03
### What's Changed
**Full Changelog**: https://github.com/obervinov/telegram-package/compare/v1.1.0...v1.1.1 by @obervinov in https://github.com/obervinov/telegram-package/pull/11
#### 🐛 Bug Fixes
* [Fixed install_requires and dependency_links in setup.py](https://github.com/obervinov/telegram-package/issues/8)
#### 📚 Documentation
* [Updated documentation: PR template](https://github.com/obervinov/telegram-package/issues/10)
#### 🚀 Features
* [Bumped telebot dependency version to 4.12.0](https://github.com/obervinov/telegram-package/issues/12)
* [Rewrited tests for this module](https://github.com/obervinov/telegram-package/issues/5)
* [Updated workflows for this module: tests, checks, dependencies and create release](https://github.com/obervinov/telegram-package/issues/6)
* [Added support for the new version of the vault-package:v2.0.0 ](https://github.com/obervinov/telegram-package/issues/7)


## v1.1.0 - 2023-03-29
### What's Changed
**Full Changelog**: https://github.com/obervinov/telegram-package/compare/v1.0.1...v1.1.0 by @obervinov in https://github.com/obervinov/telegram-package/pull/2
#### 🐛 Bug Fixes
* renamed the directory with the code to the name of the module - `telegram`
* fixed errors in the doc string and the general code format
#### 📚 Documentation
* updated and expanded the documentation in the file [README.md](https://github.com/obervinov/telegram-package/blob/v1.0.2/README.md)
#### 💥 Breaking Changes
* [changed the structure](https://github.com/obervinov/telegram-package/tree/v1.0.2#-data-structure-in-vault) of storing **bot token**
* removed `bot_name` argument in `TelegramBot.__init__`
* renamed argument `vault` -> `vault_client` and added new `parse_mode` in method `__init__()`
* added a new method [`create_inline_markup()`](https://github.com/obervinov/telegram-package/blob/v1.0.2/telegram/telegram.py#L40) to create online keyboard buttons sent by the bot
#### 🚀 Features
* updated [GitHub Actions](https://github.com/obervinov/_templates/tree/v1.0.2) version to `v1.0.2`
* added [Tests](https://github.com/obervinov/telegram-package/tree/v1.0.2/tests)



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
