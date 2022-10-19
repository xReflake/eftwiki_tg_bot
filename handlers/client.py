from aiogram import types, Dispatcher

import keyboard.client_kb
from create_bot import dp, bot

# @dp.message_handler(commands=['start','help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, '- Эй, {0.first_name}!\nЯ вижу у тебя долгий путь.\nЗагляни к нам в лагерь и узнаешь много интересного!'.format(message.from_user),reply_markup = keyboard.client_kb.mainMenu)
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/EFT_WikiBot')

async def eft_all_command(message : types.Message):
    if message.text == '📌 Квесты':
        await bot.send_message(message.from_user.id, '📌 Квесты', reply_markup=keyboard.client_kb.questMenu)

    elif message.text == '⏩Главное меню':
        await bot.send_message(message.from_user.id, '⏩Главное меню',reply_markup=keyboard.client_kb.mainMenu)

    elif message.text == '📚 Информация':
        await bot.send_message(message.from_user.id, '🛠В разработке')
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start','help'])
    dp.register_message_handler(eft_all_command)