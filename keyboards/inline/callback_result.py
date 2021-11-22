from aiogram.types import CallbackQuery
from loader import dp


@dp.callback_query_handler(text="change_language")
async def buy_books(call: CallbackQuery):
    await call.answer(text="Tilni tanlang", show_alert=False)
    await call.answer(cache_time=60)