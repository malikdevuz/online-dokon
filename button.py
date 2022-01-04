from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiohttp.client import request

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Menu"), KeyboardButton(text="Malumot")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
ovqat = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ko`chataomlari"), KeyboardButton(text="Ichimliklar")],

    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
kochataomi = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Pitsa"), KeyboardButton(text="Lavash")],
        [KeyboardButton(text="Hot-dog"), KeyboardButton(text="Shaverma")],
        [KeyboardButton(text="Somsa"), KeyboardButton(text="Gamburger")],
        [KeyboardButton(text="Orqaga")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
ichimliklar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Coca-cola"), KeyboardButton(text="Pepsi")],
        [KeyboardButton(text="Fanta"), KeyboardButton(text="Sprite")],
        [KeyboardButton(text="Orqaga")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
zakaz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Manzilimni yuborish"), KeyboardButton(text="Bekor qilish",request_location=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    
)
