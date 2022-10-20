from aiogram import types, Dispatcher

import keyboard.client_kb
from create_bot import dp, bot
# @dp.message_handler(commands=['start','help'])
async def commands_start(message : types.Message):
    try:
        photo = open('C:\MyProject\TG_bot\photo\logo_tarkov.jpg','rb')
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption='- Эй, {0.first_name}!\nЯ вижу у тебя долгий путь.\nЗагляни к нам в лагерь и узнаешь много интересного!'.format(message.from_user),reply_markup = keyboard.client_kb.mainMenu
        )
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/EFT_WikiBot')

async def eft_all_command(message : types.Message):
    if message.text == '📌 Квесты':
        await bot.send_message(message.from_user.id, '📌 Квесты', reply_markup=keyboard.client_kb.questMenu)

    elif message.text == '⛺Главное меню':
        await bot.send_message(message.from_user.id, '⛺Главное меню',reply_markup=keyboard.client_kb.mainMenu)

    elif message.text == '📚 Информация':
        await bot.send_message(message.from_user.id, '🛠В разработке')

    elif message.text == '⏩Назад к квестам':
        await bot.send_message(message.from_user.id, '⏩Назад к квестам',reply_markup=keyboard.client_kb.questMenu)


    #ТЕРАПЕВТ
    elif message.text == '💊Терапевт':
        await bot.send_message(message.from_user.id, '💊Терапевт',reply_markup=keyboard.client_kb.terapevtMenu1)

    elif message.text == '💊2/5➡':
        await bot.send_message(message.from_user.id, '💊2/5➡',reply_markup=keyboard.client_kb.terapevtMenu2)
    elif message.text == '⬅1/5💊':
        await bot.send_message(message.from_user.id, '⬅1/5💊', reply_markup=keyboard.client_kb.terapevtMenu1)



    # МЕХАНИК
    elif message.text == '🔧Механик':
        await bot.send_message(message.from_user.id, '🔧Механик',reply_markup=keyboard.client_kb.mechanicMenu1)
    elif message.text == '🔧2/5➡':
        await bot.send_message(message.from_user.id, '🔧2/5➡',reply_markup=keyboard.client_kb.mechanicMenu2)
    elif message.text == '🔧3/5➡':
        await bot.send_message(message.from_user.id, '🔧3/5➡', reply_markup=keyboard.client_kb.mechanicMenu3)
    elif message.text == '🔧4/5➡':
        await bot.send_message(message.from_user.id, '🔧4/5➡', reply_markup=keyboard.client_kb.mechanicMenu4)
    elif message.text == '🔧5/5➡':
        await bot.send_message(message.from_user.id, '🔧5/5➡', reply_markup=keyboard.client_kb.mechanicMenu5)


    elif message.text == '⬅1/5🔧':
        await bot.send_message(message.from_user.id, '⬅1/5🔧', reply_markup=keyboard.client_kb.mechanicMenu1)
    elif message.text == '⬅2/5🔧':
        await bot.send_message(message.from_user.id, '⬅2/5🔧', reply_markup=keyboard.client_kb.mechanicMenu2)
    elif message.text == '⬅3/5🔧':
        await bot.send_message(message.from_user.id, '⬅3/5🔧', reply_markup=keyboard.client_kb.mechanicMenu3)
    elif message.text == '⬅4/5🔧':
        await bot.send_message(message.from_user.id, '⬅4/5🔧', reply_markup=keyboard.client_kb.mechanicMenu4)
    # КВЕСТЫ МЕХАНИКА
    # КВЕСТ МЕХАНИКА 1
    elif message.text == 'Поручение':
        photo = open('C:\MyProject\TG_bot\photo\qv_mechanic\qv1.png', 'rb')
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption='*** ЦЕЛИ ***'
                    '\n·Найти место стоянки Егеря'
                    '\n·Найти послание от Егеря'
                    '\n·Передать послание Механику'
                    '\n\n'
                    '*** НАГРАДА ***'     
                    '\n·+4 500 EXP Механик'
                    '\n·Механик Rep +0.03'
                    '\n·30 000 руб.'
                        '\n·31 500 руб. с Разведцентр УР 1'
                        '\n·34 500 руб. с Разведцентр УР 2'
                    '\n·+ Начало квестовой линейки у Егеря'
                    '\n\n'
                    '*** Выполнение ***'
                    '\n·Ссылка на видео'
                    , reply_markup=keyboard.client_kb.mechanicMenu1
        )
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start','help'])
    dp.register_message_handler(eft_all_command)