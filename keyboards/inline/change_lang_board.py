from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def changelangkeyboard():
    changelangkeyboard = InlineKeyboardMarkup(row_width=1)

    uzbek = InlineKeyboardButton(text="๐บ๐ฟ O'zbekcha", callback_data="uz_lang")
    russian = InlineKeyboardButton(text="๐ท๐บ ะ ัััะบะธะน", callback_data="ru_lang")
    english = InlineKeyboardButton(text="๐ฌ๐ง English", callback_data="en_lang")

    changelangkeyboard.add(uzbek, russian, english)

    return changelangkeyboard