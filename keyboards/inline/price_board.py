from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def price_keyboard():
    pricekeyboard = InlineKeyboardMarkup()

    change_language = InlineKeyboardButton(text="Tilni tanlang", callback_data="change_language")
    python = InlineKeyboardButton(text="Python", callback_data="python_language")
    js = InlineKeyboardButton(text="JavaScript", callback_data="js_language")
    php = InlineKeyboardButton(text="PHP", callback_data="php_language")

    pricekeyboard.add(change_language)
    pricekeyboard.row(python, js, php)

    return pricekeyboard


