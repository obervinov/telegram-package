# Change Log
All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).


## v3.0.5 - 2026-09-17
### What's Changed
#### 🐛 Bug Fixes
* `.github/workflows`: move the reusable workflows to `obervinov/_templates@v4.0.0`. Node 20 is removed from the Actions runner on 2026-09-23, and the pinned templates still called `actions/create-release` (`runs.using: node12`, archived) along with a set of `node20` actions — releases and checks in this repository would stop running.
#### 📚 Documentation
* `README.md`: fix the usage examples against the actual API — `TelegramBot`'s first positional argument is `name`, so `TelegramBot(vault_client)` raised `VaultInstanceNotSet`, and `create_inline_markup` is a `TelegramBot` method rather than a `telebot.TeleBot` one. Also terminates the messages-template heredoc and aligns the template alias with the one the example renders.


## v3.0.4 - 2025-12-24
### What's Changed
**Full Changelog**: https://github.com/obervinov/telegram-package/compare/v3.0.3...v3.0.4 by @obervinov in https://github.com/obervinov/telegram-package/pull/78
#### 🚀 Features
* upgrade dev dependencies versions to latest versions


## v3.0.3 - 2025-12-24
### What's Changed
**Full Changelog**: https://github.com/obervinov/telegram-package/compare/v3.0.2...v3.0.3 by @obervinov in https://github.com/obervinov/telegram-package/pull/77
#### 🚀 Features
* upgrade dependencies versions to latest versions
* fix CodeQl analysis warnings


## v3.0.2 - 2025-07-11
### What's Changed
**Full Changelog**: https://github.com/obervinov/telegram-package/compare/v3.0.1...v3.0.2 by @obervinov in https://github.com/obervinov/telegram-package/pull/61
#### 🚀 Features
* bump dependencies versions to latest versions


## v3.0.1 - 2025-02-17
### What's Changed
**Full Changelog**: https://github.com/obervinov/telegram-package/compare/v3.0.0...v3.0.1 by @obervinov in https://github.com/obervinov/telegram-package/pull/55
#### 🚀 Features
* bump dependencies version
* bump workflows version to `2.1.1`


## v3.0.0 - 2024-10-17
### What's Changed
**Full Changelog**: https://github.com/obervinov/telegram-package/compare/v2.0.1...v3.0.0 by @obervinov in https://github.com/obervinov/telegram-package/pull/47
#### 💥 Breaking Changes
* bump python version to `3.12`
#### 🚀 Features
* bump dependencies version
* bump workflows version to `2.0.0`


## v2.0.1 - 2024-08-25
### What's Changed
**Full Changelog**: https://github.com/obervinov/telegram-package/compare/v2.0.0...v2.0.1 by @obervinov in https://github.com/obervinov/telegram-package/pull/44
#### 🐛 Bug Fixes
* [Bug: Attempting to delete a message that does not exist causes the bot to crash ](https://github.com/obervinov/telegram-package/issues/43)


## v2.0.0 - 2024-08-23
### What's Changed
**Full Changelog**: https://github.com/obervinov/telegram-package/compare/v1.2.0...v2.0.0 by @obervinov in https://github.com/obervinov/telegram-package/pull/42
#### 💥 Breaking Changes
* Bump vault-package version to `3.0.0` (this version contains major changes)
#### 🐛 Bug Fixes
* Fix security vulnerabilities in dependencies
#### 🚀 Features
* Bump workflows version to `1.2.8`
* Bump vault-package version to `3.0.0`
* Bump transitive dependencies version
#### 📚 Documentation
* Small fixes in documentation


## v1.2.0 - 2024-03-22
### What's Changed
**Full Changelog**: https://github.com/obervinov/telegram-package/compare/v1.1.3...v1.2.0 by @obervinov in https://github.com/obervinov/telegram-package/pull/25
#### 🐛 Bug Fixes
* [Dependency graph does not work correctly, sort it out and fix it network/dependencies](https://github.com/obervinov/telegram-package/issues/25)
* [Add class parameters for exception handling](https://github.com/obervinov/telegram-package/issues/19)
#### 🚀 Features
* [Merge all workflows to single file](https://github.com/obervinov/telegram-package/issues/22)
* [Migration from pip to poetry](https://github.com/obervinov/telegram-package/issues/3)
* [Add more useful methods for typical bots](https://github.com/obervinov/telegram-package/issues/26)
* [Add default size in method parameter](https://github.com/obervinov/telegram-package/issues/20)
* [Add support environment variable `TELEGRAM_BOT_NAME`](https://github.com/obervinov/telegram-package/issues/28)
#### 📚 Documentation
* [Fix documentation](https://github.com/obervinov/telegram-package/issues/21)
* [Change the order of changes by sections in `CHANGELOG.md`](https://github.com/obervinov/telegram-package/issues/23)


## v1.1.3 - 2023-06-20
### What's Changed
**Full Changelog**: https://github.com/obervinov/telegram-package/compare/v1.1.2...v1.1.3 by @obervinov in https://github.com/obervinov/telegram-package/pull/18
#### 🐛 Bug Fixes
* [Fix badge with tests in README.md](https://github.com/obervinov/telegram-package/issues/15)
* [Fix the error that caused the workflow create_release to run twice - at pr/main](https://github.com/obervinov/telegram-package/issues/16)
#### 🚀 Features
* [Bump vault-package to v2.0.1](https://github.com/obervinov/telegram-package/issues/17)


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
