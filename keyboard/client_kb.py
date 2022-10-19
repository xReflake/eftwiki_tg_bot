from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

btnMainMenu = KeyboardButton('⏩Главное меню')
#MainMenu
btnInfo = KeyboardButton('📚 Информация')
btnQuest = KeyboardButton('📌 Квесты')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnQuest)


#QuestMenu
btnPrapor = KeyboardButton ('🔫Прапор')
btnTerapevt = KeyboardButton ('💊Терапевт')
btnSkypjik = KeyboardButton ('🛒Скупщик')
btnLijnik = KeyboardButton ('🗻Лыжник')
btnMirotvorec = KeyboardButton ('🎯Миротворец')
btnMechanic = KeyboardButton ('🔧Механик')
btnBarahol = KeyboardButton ('🧻Барахольщик')
btnEgor = KeyboardButton ('🪓Егерь')
questMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPrapor, btnTerapevt, btnSkypjik, btnLijnik, btnMirotvorec, btnMechanic, btnBarahol, btnEgor, btnMainMenu)