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
async def command_start(message: types.Message):
    button=KeyboardButton("помощь")
    keyboard=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(button)
    await message.reply("Привет, это мой магазин, в котором ты найдёшь ессе, сочинения, доклады, конспекты и т.д."+"Для получения     более подробной информации нажми кнопку 'помощь'", reply_markup=keyboard)
@dp.message_handler()
async def command(message: types.Message):
    if message.text=='помощь':
        button_help=KeyboardButton("Выбрать документ")
        keyboard=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(button_help)
        await message.answer("Следуйте подсказкам снизу", reply_markup=keyboard)
#Почему то не работает message.text=='Выбрать документ' в третьем асинхронном процессе
#@dp.message_handler()
#async def command_doc(message: types.Message)
    elif message.text=='Выбрать документ':
        button_soch=KeyboardButton("Сочинение, ессе")
        button_doc=KeyboardButton("Документы(Рефераты, Проекты, Работы)")
        button_pres=KeyboardButton("Презентации")
        keyboard1=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard1.add(button_soch, button_doc, button_pres)
        await message.answer("Выберете нужный товар", reply_markup=keyboard1)
    elif message.text=='Сочинение, ессе':
        button_soch=KeyboardButton("Сочинение")
        button_esse=KeyboardButton("Ессе")
        button_back=KeyboardButton("Назад")
        keyboard2=ReplyKeyboardMarkup()
        keyboard2.add(button_soch, button_esse, button_back)
        await message.answer("По кнопкам вы можете закзать сочинение или ессе", reply_markup=keyboard2)
    elif message.text=='Документы(Рефераты, Проекты и др.)':
        button_ref=KeyboardButton("Реферат")
        button_proekt=KeyboardButton("Проект")
        button_rab=KeyboardButton("Другой документ")
        button_back=KeyboardButton("Назад")
        keyboard3=ReplyKeyboardMarkup()
        keyboard3.add(button_ref, button_proekt, button_rab, button_back)
        await message.answer("По кнопкам ниже вы можете заказать реферат, проект, работа", reply_markup=keybard3)
    elif message.text=='Презентации':
        button_pres=KeyboardButton("Презентация")
        button_back=KeyboardByutton("Назад")
        keyboard4=ReplyKeyboardMarkup()
        keyboard4.add(button_pres, button_back)
        await message.answer("По кнопкам ниже можно заказать презентацию")
    data_payed=[]#то что человек уже купил
    data_willpay=[]#то что человек собираеться купить
    if message.text=='Сочинение' or message.text=='Ессе' or message.text=='Реферат' or message.text=='Проект' or message.text=='Другой документ' or message.text=='Презентация':
        key_basket=KeyboardButton("Перейти в корзину")
        key_add=KeyboardButton("Выбрать ещё товар")
        keyboard=ReplyKeyboardMarkup()
        keyboard.add(key_basket, key_add)
        await message.answer("Товар добален в корзину", reply_markup=keyboard)
        if message.text=='Сочинение':
            data_willpay.append(message.text)
        elif message.text=='Ессе':
            data_willpay.append(message.text)
        elif message.text=='Реферат':
            data_willpay.append(message.text)
        elif message.text=='Проект':
            data_willpay.append(message.text)
        elif message.text=='Другой документ':
            data_willpay.append(message.text)
        elif message.text=='Презентация':
            data_willpay.append(message.text)
    elif message.text=='Назад':
        button_soch=KeyboardButton("Сочинение, ессе")
        button_doc=KeyboardButton("Документы(Рефераты, Проекты, Работы)")
        button_pres=KeyboardButton("Презентации")
        keyboard1=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard1.add(button_soch, button_doc, button_pres)
        await message.answer("Выберете нужный товар", reply_markup=keyboard1)
    elif message.text=='Выбрать ещё товар':
        button_soch=KeyboardButton("Сочинение, ессе")
        button_doc=KeyboardButton("Документы(Рефераты, Проекты, Работы)")
        button_pres=KeyboardButton("Презентации")
        keyboard1=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard1.add(button_soch, button_doc, button_pres)
        await message.answer("Выберете нужный товар", reply_markup=keyboard1)
    print(data_willpay)







if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)
