import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice, pear_keyboard, apples_keyboard
from loader import dp, bot

@dp.message_handler(Command("start"))
async def show_items(message: Message):
    await message.answer(text="Choose one of them", reply_markup=choice)

@dp.callback_query_handler(text_contains="pear")
async def buying_pear(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"{callback_data=}")
        await call.message.answer("You choose visit site. Good luck.", reply_markup=pear_keyboard)

@dp.callback_query_handler(text_contains="alarm")
async def buying_pear(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"{callback_data=}")
        await call.message.answer("You choose visit site. Good luck.", reply_markup=pear_keyboard)

@dp.callback_query_handler(text_contains="clock")
async def buying_pear(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"{callback_data=}")
        await call.message.answer("You choose visit site. Good luck.", reply_markup=pear_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name="apple"))
async def buying_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"{callback_data=}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"You choose APPLE. Good luck.", reply_markup=apples_keyboard)

@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.answer("You've canceled!", show_alert=True)
