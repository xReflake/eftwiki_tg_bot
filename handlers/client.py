from aiogram import types, Dispatcher
import keyboard.client_kb
import parse_info.parsing
import requests
from bs4 import BeautifulSoup as BS
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
        link = 'https://escapefromtarkov.fandom.com/ru/wiki/%D0%9F%D0%BE%D1%80%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5'
        r = requests.get(link)
        soup = BS(r.content, 'lxml')
        parse_name = parse_info.parsing.parse_name_quest(link,soup)
        page_h1 = soup.find("div", class_="mw-parser-output")
        page_h1 = page_h1.text.strip()
        photo = open('C:\MyProject\TG_bot\photo\qv_mechanic\qv1.png', 'rb')
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption='*** НАЗВАНИЕ КВЕСТА ***\n' +
                    parse_name + '\n'
                    '*** ЦЕЛИ ***''\n'
                    + parse_info.parsing.parse_target(link,soup) +
                    '\n\n'
                    '*** НАГРАДА ***''\n'
                    + parse_info.parsing.parse_reward(link,soup) +
                    ''
                    , reply_markup=keyboard.client_kb.mechanicMenu1
        )
        await bot.send_message(message.from_user.id, '*** Выполнение ***')
        photo = open('C:\MyProject\TG_bot\photo\qv_mechanic\qv1\qv1_1.jpg', 'rb')
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption='·Место стоянки Егеря на карте'
            , reply_markup=keyboard.client_kb.mechanicMenu1
        )
        photo = open('C:\MyProject\TG_bot\photo\qv_mechanic\qv1\qv1_2.png', 'rb')
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption='·Расположение стоянки относительно самолета'
            , reply_markup=keyboard.client_kb.mechanicMenu1
        )
        photo = open('C:\MyProject\TG_bot\photo\qv_mechanic\qv1\qv1_3.png', 'rb')
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption='·Само послание'
            , reply_markup=keyboard.client_kb.mechanicMenu1
        )
        #await bot.send_message(message.from_user.id, 'Ссылка на видео')

    # КВЕСТ МЕХАНИКА 2
    elif message.text == 'Оружейник. Часть 1 (МР-133)':
        photo = open('C:\MyProject\TG_bot\photo\qv_mechanic\qv2.jpg', 'rb')
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption='*** ЦЕЛИ ***'
                    '\n·Модифицировать МР-133 до требуемых параметров'
                    '\n\n'
                    '*** НАГРАДА ***'     
                    '\n·+3 200 EXP'
                    '\n·Механик Rep +0.02'
                    '\n·20 000 руб.'
                        '\n·21 000 руб. с Разведцентр УР 1'
                        '\n·23 000 руб. с Разведцентр УР 2'
                    '\n·Винтовка Молот ВПО-215 "Горностай" .366 ТКМ'
                    '\n·20x .366 ТКМ БП-М'
                    , reply_markup=keyboard.client_kb.mechanicMenu1
        )
        await bot.send_message(message.from_user.id, '*** Выполнение ***')
        await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=qoWuU-nVoGI')
    # КВЕСТ МЕХАНИКА 3
    elif message.text == 'Оружейник. Часть 2 (АКС-74У)':
        photo = open('C:\MyProject\TG_bot\photo\qv_mechanic\qv3.jpg', 'rb')
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption='*** ЦЕЛИ ***'
                    '\n·Модифицировать АКС-74У до требуемых параметров'
                    '\n\n'
                    '*** НАГРАДА ***'     
                    '\n·+6 000 EXP'
                    '\n·Механик Rep +0.02'
                    '\n·60 000 руб.'
                        '\n·63 000 руб. с Разведцентр УР 1'
                        '\n·69 000 руб. с Разведцентр УР 2'
                    '\n·2x Конденсаторы'
                    '\n·2x Пучок проводов'
                    , reply_markup=keyboard.client_kb.mechanicMenu1
        )
        await bot.send_message(message.from_user.id, '*** Выполнение ***')
        await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=5Gd7xbWyggk&t=18s')
    # КВЕСТ МЕХАНИКА 4
    elif message.text == 'Оружейник. Часть 3 (MP5)':
        photo = open('C:\MyProject\TG_bot\photo\qv_mechanic\qv4.jpg', 'rb')
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption='*** ЦЕЛИ ***'
                    '\n·Модифицировать MP5 до требуемых параметров'
                    '\n\n'
                    '*** НАГРАДА ***'
                    '\n·+5 900 EXP'
                    '\n·Механик Rep +0.03'
                    '\n·500 евро'
                    '\n·526 евро с Разведцентр УР 1'
                    '\n·575 евро с Разведцентр УР 2'
                    '\n·Пистолет-пулемет ПП-19-01 "Витязь" 9x19 Зенит'

            , reply_markup=keyboard.client_kb.mechanicMenu1
        )
        await bot.send_message(message.from_user.id, '*** Выполнение ***')
        await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=07WuNthNw9I')
    # КВЕСТ МЕХАНИКА 5
    elif message.text == 'Оружейник. Часть 4 (M4A1)':
        photo = open('C:\MyProject\TG_bot\photo\qv_mechanic\qv5.jpg', 'rb')
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption='*** ЦЕЛИ ***'
                    '\n·Модифицировать M4A1 до требуемых параметров'
                    '\n\n'
                    '*** НАГРАДА ***'
                    '\n·+7 000 EXP'
                    '\n·Механик Rep +0.03'
                    '\n·800 евро'
                    '\n·840 евро с Разведцентр УР 1'
                    '\n·920 евро с Разведцентр УР 2'
                    '\n·1x Монета биткоина'

            , reply_markup=keyboard.client_kb.mechanicMenu1
        )
        await bot.send_message(message.from_user.id, '*** Выполнение ***')
        await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=nlPlns8x5pI')
    # КВЕСТ МЕХАНИКА 6
    elif message.text == 'Оружейник. Часть 5 (ДВЛ-10)':
        photo = open('C:\MyProject\TG_bot\photo\qv_mechanic\qv6.jpg', 'rb')
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption='*** ЦЕЛИ ***'
                    '\n·Модифицировать ДВЛ-10 до требуемых параметров'
                    '\n\n'
                    '*** НАГРАДА ***'
                    '\n·+10 700 EXP'
                    '\n·Механик Rep +0.03'
                    '\n·200 000 руб.'
                    '\n·210 000 руб. с Разведцентр УР 1'
                    '\n·230 000 руб. с Разведцентр УР 2'
                    '\n·2x Пакет саморезов'
                    '\n·1х Электродрель'
                    '\n·1x Металлическая топливная канистра'
            , reply_markup=keyboard.client_kb.mechanicMenu1
        )
        await bot.send_message(message.from_user.id, '*** Выполнение ***')
        await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=Tpb78U-jPBo')
    # КВЕСТ МЕХАНИКА 7
    elif message.text == 'Оружейник. Часть 6 (R11 RSASS)':
        photo = open('C:\MyProject\TG_bot\photo\qv_mechanic\qv7.jpg', 'rb')
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption='*** ЦЕЛИ ***'
                    '\n·Модифицировать R11 RSASS до требуемых параметров'
                    '\n\n'
                    '*** НАГРАДА ***'
                    '\n·+11 700 EXP'
                    '\n·Механик Rep +0.03'
                    '\n·1 000 евро'
                    '\n·1 050 евро с Разведцентр УР 1'
                    '\n·1 150 евро с Разведцентр УР 2'
                    '\n·2x Монета биткоина'
            , reply_markup=keyboard.client_kb.mechanicMenu1
        )
        await bot.send_message(message.from_user.id, '*** Выполнение ***')
        await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=cOmLOEebals')
    # КВЕСТ МЕХАНИКА 8
    elif message.text == 'Оружейник. Часть 7 (Remington M870)':
        photo = open('C:\MyProject\TG_bot\photo\qv_mechanic\qv8.jpg', 'rb')
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption='*** ЦЕЛИ ***'
                    '\n·Модифицировать Remington Model 870 до требуемых параметров'
                    '\n\n'
                    '*** НАГРАДА ***'
                    '\n·+12 000 EXP'
                    '\n·Механик Rep +0.03'
                    '\n·100 000 руб.'
                    '\n·105 000 руб. с Разведцентр УР 1'
                    '\n·115 000 руб. с Разведцентр УР 2'
                    '\n·1x Пистолет Glock 17 9x19 Fisher'
            , reply_markup=keyboard.client_kb.mechanicMenu1
        )
        await bot.send_message(message.from_user.id, '*** Выполнение ***')
        await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=BY3Qi_X2htg')
        # КВЕСТ МЕХАНИКА 9
    # КВЕСТ МЕХАНИКА 9
    elif message.text == 'Оружейник. Часть 8 (АКМ)':
        photo = open('C:\MyProject\TG_bot\photo\qv_mechanic\qv9.jpg', 'rb')
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption='*** ЦЕЛИ ***'
                    '\n·Модифицировать АКМ до требуемых параметров'
                    '\n\n'
                    '*** НАГРАДА ***'
                    '\n·+13 000 EXP'
                    '\n·Механик Rep +0.03'
                    '\n·1 500 евро'
                    '\n·1575 евро с Разведцентр УР 1'
                    '\n·1725 евро с Разведцентр УР 2'
                    '\n·2x Монета биткоина'
            , reply_markup=keyboard.client_kb.mechanicMenu1
        )
        await bot.send_message(message.from_user.id, '*** Выполнение ***')
        await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=Eyk8qzZmTx0')
        # КВЕСТ МЕХАНИКА 10
    # КВЕСТ МЕХАНИКА 10
    elif message.text == 'Оружейник. Часть 9 (АКС-74Н)':
        photo = open('C:\MyProject\TG_bot\photo\qv_mechanic\qv10.jpg', 'rb')
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption='*** ЦЕЛИ ***'
                    '\n·Модифицировать АКС-74Н до требуемых параметров'
                    '\n\n'
                    '*** НАГРАДА ***'
                    '\n·+17 000 EXP'
                    '\n·500 евро'
                    '\n·525 евро с Разведцентр УР 1'
                    '\n·575 евро с Разведцентр УР 2'
                    '\n·Механик Rep +0.03'
                    '\n·1x Colt M4A1 5.56x45 SOPMOD II'
            , reply_markup=keyboard.client_kb.mechanicMenu2
        )
        await bot.send_message(message.from_user.id, '*** Выполнение ***')
        await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=LYbfWr7xoNg')
    # КВЕСТ МЕХАНИКА 11
    elif message.text == 'Оружейник. Часть 10 (АК-105)':
        photo = open('C:\MyProject\TG_bot\photo\qv_mechanic\qv11.jpg', 'rb')
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption='*** ЦЕЛИ ***'
                    '\n·Модифицировать АК-105 до требуемых параметров'
                    '\n\n'
                    '*** НАГРАДА ***'
                    '\n·+13 300 EXP'
                    '\n·Механик Rep +0.03'
                    '\n·2x Кейс для патронов'
                    '\n·Разблокирует покупку Colt M4A1 5.56x45 SOPMOD I на LL3'
                    '\n·Разблокирует покупку 5.7x28мм R37.F на LL4'
            , reply_markup=keyboard.client_kb.mechanicMenu2
        )
        await bot.send_message(message.from_user.id, '*** Выполнение ***')
        await bot.send_message(message.from_user.id, 'Youtube')
    # КВЕСТ МЕХАНИКА 12
    elif message.text == 'Оружейник. Часть 11 (АС Вал)':
        photo = open('C:\MyProject\TG_bot\photo\qv_mechanic\qv11.jpg', 'rb')
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption='*** ЦЕЛИ ***'
                    '\n·Модифицировать АС Вал до требуемых параметров'
                    '\n\n'
                    '*** НАГРАДА ***'
                    '\n·+13 300 EXP'
                    '\n·Механик Rep +0.03'
                    '\n·2x Кейс для патронов'
                    '\n·Разблокирует покупку Colt M4A1 5.56x45 SOPMOD I на LL3'
                    '\n·Разблокирует покупку 5.7x28мм R37.F на LL4'
            , reply_markup=keyboard.client_kb.mechanicMenu2
        )
        await bot.send_message(message.from_user.id, '*** Выполнение ***')
        await bot.send_message(message.from_user.id, 'Youtube')
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start','help'])
    dp.register_message_handler(eft_all_command)