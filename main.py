import logging
from os import replace
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext 
from button import menu,ichimliklar,kochataomi,ovqat,zakaz
from statelar import Translate
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    user = message.from_user.first_name
    await message.answer(f"Assalomu aleykum {user}😊\nTarjima turini tanlang", reply_markup=menu)
@dp.message_handler(Text(equals="Menu"))
async def jjj(message):
    await message.answer('Menu',reply_markup=ovqat)

@dp.message_handler(Text(equals="Ko`chataomlari"))
async def ff(message):
    await message.answer('Nechta buyurtma qilasiz?',reply_markup=kochataomi)
@dp.message_handler(Text(equals="Pitsa"))
async def ffw(message):
    await message.answer('Nechta buyurtma qilasiz?')
    await Translate.pitsaset.set()
@dp.message_handler(Text(equals="Lavash"))
async def wwwww(message):
    await message.answer('Nechta buyurtma qilasiz?')
    await Translate.lavashset.set()
@dp.message_handler(Text(equals="Gamburger"))
async def wwwww(message):
    await message.answer('Nechta buyurtma qilasiz?')
    await Translate.gamburgerset.set()
@dp.message_handler(Text(equals="Shaverma"))
async def www(message):
    await message.answer('Nechta buyurtma qilasiz?')
    await Translate.shavermaset.set()
@dp.message_handler(Text(equals="Hot-dog"))
async def ffwww(message):
    await message.answer('Nechta buyurtma qilasiz?')
    await Translate.hotdogset.set()
@dp.message_handler(Text(equals="Somsa"))
async def fwf(message):
    await message.answer('Nechta buyurtma qilasiz?')
    await Translate.somsaset.set()
@dp.message_handler(state=Translate.pitsaset)
async def ss(message,state:FSMContext):
    await message.answer(int(message.text)*12000,reply_markup=zakaz)
@dp.message_handler(state=Translate.hotdogset)
async def ssk(message,state:FSMContext):
    await message.answer(int(message.text)*10000,reply_markup=zakaz)
@dp.message_handler(state=Translate.somsaset)
async def sssk(message,state:FSMContext):
    await message.answer(int(message.text)*8000,reply_markup=zakaz)
@dp.message_handler(state=Translate.lavashset)
async def ssssk(message,state:FSMContext):
    await message.answer(int(message.text)*22000,reply_markup=zakaz)
@dp.message_handler(state=Translate.shavermaset)
async def ssske(message,state:FSMContext):
    await message.answer(int(message.text)*12000,reply_markup=zakaz)
@dp.message_handler(state=Translate.gamburgerset)
async def ssske4(message,state:FSMContext):
    await message.answer(int(message.text)*15000,reply_markup=zakaz)

@dp.message_handler(Text(equals='Manzilimni yuborish'))
async def ffff(message):
    await message.send_location(message.from_user.id)

@dp.message_handler(Text(equals="Ichimliklar"))
async def ff(message):
    await message.answer('Nechta buyurtma qilasiz?',reply_markup=ichimliklar)
@dp.message_handler(Text(equals="Coca-cola"))
async def ffw(message):
    await message.answer('Nechta buyurtma qilasiz?')
    await Translate.colaset.set()
@dp.message_handler(Text(equals="Fanta"))
async def ffw(message):
    await message.answer('Nechta buyurtma qilasiz?')
    await Translate.fantaset.set()
@dp.message_handler(Text(equals="Sprite"))
async def ffw(message):
    await message.answer('Nechta buyurtma qilasiz?')
    await Translate.spriteset.set()
@dp.message_handler(Text(equals="Pepsi"))
async def ffw(message):
    await message.answer('Nechta buyurtma qilasiz?')
    await Translate.pepsiset.set()
@dp.message_handler(state=Translate.colaset)
async def sssd(message,state:FSMContext):
    # if int(message.text)>0:
    await message.answer(int(message.text)*8000)
@dp.message_handler(state=Translate.fantaset)
async def sssd(message,state:FSMContext):
    await message.answer(int(message.text)*9000)
@dp.message_handler(state=Translate.spriteset)
async def sssd(message,state:FSMContext):
    await message.answer(int(message.text)*9000,reply_markup=zakaz)
@dp.message_handler(state=Translate.pepsiset)
async def sssd(message,state:FSMContext):
    await message.answer(int(message.text)*9000)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

