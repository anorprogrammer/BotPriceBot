from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def changelangkeyboard():
    changelangkeyboard = InlineKeyboardMarkup(row_width=1)

    uzbek = InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uz_lang")
    russian = InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru_lang")
    english = InlineKeyboardButton(text="🇬🇧 English", callback_data="en_lang")

    changelangkeyboard.add(uzbek, russian, english)

    return changelangkeyboard