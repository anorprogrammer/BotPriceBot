from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.change_lang_board import changelangkeyboard

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(text=f"Assalomu alaykum {message.from_user.get_mention()}!")
    await message.answer(text="Muloqot uchun tilni tanlang\n\n"
                              "Выберите язык для общения\n\n"
                              "Select language",
                         reply_markup=changelangkeyboard())