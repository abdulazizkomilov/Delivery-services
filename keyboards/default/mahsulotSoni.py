from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = []

for i in range(0, 3):
    if i == 1:
        keyboard.append(
            KeyboardButton(text=f'Boshqa')
        )


mah_miqdori = ReplyKeyboardMarkup(
    keyboard=[
        keyboard,
        [
            KeyboardButton(text='🏠 Bosh menyu')
        ]
    ],
    resize_keyboard=True,
    row_width=2

)


mah_miqdori_rus = ReplyKeyboardMarkup(
    keyboard=[
        keyboard,
        [
            KeyboardButton(text='🏠 Главное меню')
        ]
    ],
    resize_keyboard=True,
    row_width=2

)
