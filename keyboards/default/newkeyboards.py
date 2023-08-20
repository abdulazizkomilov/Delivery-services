from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Xizmatlar')
        ],
        [
            KeyboardButton(text='⚙ Sozlamalar'),
            KeyboardButton(text='📞 Aloqaga chiqish')
        ]
    ],
    resize_keyboard=True
)

menu_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='услуги')
        ],
        [
            KeyboardButton(text='⚙ Настройки'),
            KeyboardButton(text='📞 Свяжитесь с нами')
        ]
    ],
    resize_keyboard=True
)
