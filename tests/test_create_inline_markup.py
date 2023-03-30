"""
This test is necessary to check the returned markup buttons.
"""
from unittest.mock import Mock
from telegram.telegram import TelegramBot

mock_vault = Mock()
telegram_client = TelegramBot(mock_vault)

buttons_list = [
    'Jan', 'Feb', 'Mar', 'Apr',
    'May', 'June', 'July', 'Aug',
    'Sept', 'Oct', 'Nov', 'Dec'
]


def test_create_inline_markup_3(
    size: int = 3
):
    """
    The function checks that the returned inline keyboard markup object
    matches the specified parameters.
    """
    markup = telegram_client.create_inline_markup(
        buttons_list,
        size
    )
    assert isinstance(markup, telegram_client.telegram_types.InlineKeyboardMarkup)
    for row in markup.keyboard:
        assert len(row) == size


def test_create_inline_markup_4(
    size: int = 4
):
    """
    The function checks that the returned inline keyboard markup object
    matches the specified parameters.
    """
    markup = telegram_client.create_inline_markup(
        buttons_list,
        size
    )
    assert isinstance(markup, telegram_client.telegram_types.InlineKeyboardMarkup)
    for row in markup.keyboard:
        assert len(row) == size
