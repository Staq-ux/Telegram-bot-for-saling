import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from config_shop import TOKEN
logging.basicConfig(level=logging.INFO)

API_TOKEN=TOKEN
bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)
@dp.message_handler(content_types=['document'])
async def doc_handler(message: types.Message):
    doc_data=[]
    data_file=types.mixins.Downloadable.get_file
    print(data_file)
    file_id=message.document.file_id
    file_name=message.document.file_name
    doc_data.append(file_name)
    doc_data.append(file_id)
    print(doc_data)
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    button=KeyboardButton("/Что_дальше")
    keyboard=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(button)
    await message.reply("Привет, это мой магазин, в котором ты найдёшь ессе, сочинения, доклады, конспекты и т.д."+" Для получения более подробной информации наажми кнопку 'Что дальше?'", reply_markup=keyboard)
    await bot.send_message(message.from_user.id, "Готово")
@dp.message_handler(commands=['Что_дальше'], content_types=['text'], )
async def help(message: types.Message):
    await message.reply("РАБОТАЕТ")




if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)
