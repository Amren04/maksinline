from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URL_JIHC, URL_APPLE, URL_JHC, URL_CLOCK
from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="Collection", callback_data=buy_callback.new(item_name="pear", quantity=1))
choice.insert(buy_pear)

buy_alarm = InlineKeyboardButton(text="Adress", callback_data=buy_callback.new(item_name="alarm", quantity=1))
choice.insert(buy_alarm)

buy_clock = InlineKeyboardButton(text="Woman", callback_data=buy_callback.new(item_name="clock", quantity=1))
choice.insert(buy_clock)

buy_apples = InlineKeyboardButton (text="Man", callback_data="buy:apple:5")
choice.insert(buy_apples)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")
choice.insert(cancel_button)

pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Visit", url=URL_JIHC)
    ]
])
alarm_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Visit", url=URL_JHC)
    ]
])
clock_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Visit", url=URL_CLOCK)
    ]
])
apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_APPLE)
    ]
])