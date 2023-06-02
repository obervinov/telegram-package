"""
This test is necessary to check the returned markup buttons.
"""
test_buttons_list = [
    'Jan', 'Feb', 'Mar', 'Apr',
    'May', 'June', 'July', 'Aug',
    'Sept', 'Oct', 'Nov', 'Dec'
]


def test_create_inline_markup_3(telegram_client):
    """
    A test to check whether the returned object matches the passed keyboard size: 3
    """
    markup = telegram_client.create_inline_markup(
        test_buttons_list,
        3
)
    assert isinstance(markup, telegram_client.telegram_types.InlineKeyboardMarkup)
    for row in markup.keyboard:
        assert len(row) == 3


def test_create_inline_markup_4(telegram_client):
    """
    A test to check whether the returned object matches the passed keyboard size: 4
    """
    markup = telegram_client.create_inline_markup(
        test_buttons_list,
        4
    )
    assert isinstance(markup, telegram_client.telegram_types.InlineKeyboardMarkup)
    for row in markup.keyboard:
        assert len(row) == 4

