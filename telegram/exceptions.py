"""
Custom exceptions for the Users package.
"""


class VaultInstanceNotSet(Exception):
    """
    Raised when the Vault instance is not set.

    Args:
        message (str): The error message.

    Example:
        >>> try:
        ...     raise VaultInstanceNotSet("Vault instance not set")
        ... except VaultInstanceNotSet as e:
        ...     print(e)
        Vault instance not set
    """
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class BotNameNotSet(Exception):
    """
    Raised when the bot name is not set.

    Args:
        message (str): The error message.

    Example:
        >>> try:
        ...     raise BotNameNotSet("Bot name not set")
        ... except BotNameNotSet as e:
        ...     print(e)
        Bot name not set
    """
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class InvalidTokenConfiguration(Exception):
    """
    Raised when the token is not set.

    Args:
        message (str): The error message.

    Example:
        >>> try:
        ...     raise InvalidTelegramTokenConfiguration("Telegram token not set")
        ... except InvalidTelegramTokenConfiguration as e:
        ...     print(e)
        Telegram token not set
    """
    def __init__(self, message):
        self.message = message
        super().__init__(message)
