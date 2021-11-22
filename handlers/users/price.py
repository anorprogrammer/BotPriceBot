from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from keyboards.inline.price_board import price_keyboard

from loader import dp


@dp.message_handler(Command(commands="price"))
async def bot_start(message: types.Message):
    await message.answer(f"Tanlang !", reply_markup=price_keyboard())