from datetime import datetime
import pytz
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def adminbut(chat_id, lang, id):
    but = types.InlineKeyboardMarkup()

    but.add(types.InlineKeyboardButton('☑️Tasdiqlash', callback_data=f'confirm,{chat_id, lang, id}'),
            types.InlineKeyboardButton('✖️Bekor qilish', callback_data=f'calcel,{chat_id, lang, id}'))
    but.add(types.InlineKeyboardButton('🛵Kuryer qo\'shish', callback_data=f'kuryer,{chat_id, lang, id}'),
            types.InlineKeyboardButton('⏱Vaqt belgilash', callback_data=f'date,{chat_id, lang, id}'))

    return but


def adminupdatebut(data, kuryer, adddate):
    date = datetime.now(pytz.timezone('Asia/Tashkent')).strftime('%Y-%m-%d, %H:%M')
    but = types.InlineKeyboardMarkup()

    but.add(types.InlineKeyboardButton('✅Tasdiqlandi', callback_data="confirmed"),
            types.InlineKeyboardButton('✖️Bekor qilish', callback_data=data.replace('confirm,', 'calcel,')))
    but.add(types.InlineKeyboardButton(f'🕒 Tasdiqlash {date}', callback_data='0'))

    if kuryer:
        but.add(types.InlineKeyboardButton(f'👨‍💼 Kuryer {kuryer}', callback_data='0'))

    if adddate:
        but.add(types.InlineKeyboardButton(f'⏱ Yetkazib berish {adddate}', callback_data='0'))

    return but


def admincancelbut(data):

    date = datetime.now(pytz.timezone('Asia/Tashkent')).strftime('%Y-%m-%d, %H:%M')
    but = types.InlineKeyboardMarkup()
    but.add(types.InlineKeyboardButton('☑️Tasdiqlash',
                                       callback_data=data.replace('calcel,', 'confirm,')),
            types.InlineKeyboardButton('❌Bekor qilindi', callback_data='end'))
    but.add(types.InlineKeyboardButton(f'🕒 Bekor qilish {date}', callback_data='0'))

    return but


def adminback():
    but = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='⬅️ Orqaga')

            ],
        ],
        resize_keyboard=True
    )
    return but


def adminbacked(data):

    but = types.InlineKeyboardMarkup()
    but.add(types.InlineKeyboardButton('☑️Tasdiqlash', callback_data=data.replace('kuryer,', 'confirm,')),
            types.InlineKeyboardButton('✖️Bekor qilish', callback_data=data.replace('kuryer,', 'calcel,')))
    but.add(types.InlineKeyboardButton('🛵Kuryer qo\'shish', callback_data=data.replace('kuryer,', 'kuryer,')),
            types.InlineKeyboardButton('⏱Vaqt belgilash', callback_data=data.replace('kuryer,', 'date,')))

    return but


def AdminAddKur(data, message):

    but = types.InlineKeyboardMarkup()
    but.add(types.InlineKeyboardButton('☑️Tasdiqlash', callback_data=data.replace('kuryer,', 'confirm,')),
            types.InlineKeyboardButton('✖️Bekor qilish', callback_data=data.replace('kuryer,', 'calcel,')))
    but.add(types.InlineKeyboardButton('✅Kuryer qo\'shildi', callback_data="kuryeraded"),
            types.InlineKeyboardButton('⏱Vaqt belgilash', callback_data=data.replace('kuryer,', 'date,')))
    but.add(types.InlineKeyboardButton(f'Kuryer: {message}', callback_data=data.replace('kuryer,', 'kuryerclear,')))

    return but


def AdminAdDate(data, message, date):

    but = types.InlineKeyboardMarkup()
    but.add(types.InlineKeyboardButton('☑️Tasdiqlash', callback_data=data.replace('date,', 'confirm,')),
            types.InlineKeyboardButton('✖️Bekor qilish', callback_data=data.replace('date,', 'calcel,')))
    but.add(types.InlineKeyboardButton('✅Kuryer qo\'shildi', callback_data='kuryeraded'),
            types.InlineKeyboardButton('✅Vaqt belgilandi', callback_data='dateadd'))
    but.add(types.InlineKeyboardButton(f'Kuryer: {message}', callback_data=data.replace('date,', 'kuryerclear,')))
    but.add(types.InlineKeyboardButton(f'Vaqt: {date}', callback_data=data.replace('date,', 'dateclear,')))

    return but


def AdminbackDate(data, message):

    but = types.InlineKeyboardMarkup()
    but.add(types.InlineKeyboardButton('☑️Tasdiqlash', callback_data=data.replace('date,', 'confirm,')),
            types.InlineKeyboardButton('✖️Bekor qilish', callback_data=data.replace('date,', 'calcel,')))
    but.add(types.InlineKeyboardButton('🛵Kuryer qo\'shish', callback_data=data.replace('date,', 'kuryer,')),
            types.InlineKeyboardButton('✅Vaqt belgilandi', callback_data='dateadd'))
    but.add(types.InlineKeyboardButton(f'Vaqt: {message}', callback_data=data.replace('date,', 'dateclear,')))

    return but


def admindateback(data):

    but = types.InlineKeyboardMarkup()
    but.add(types.InlineKeyboardButton('☑️Tasdiqlash', callback_data=data.replace('date,', 'confirm,')),
            types.InlineKeyboardButton('✖️Bekor qilish', callback_data=data.replace('date,', 'calcel,')))
    but.add(types.InlineKeyboardButton('🛵Kuryer qo\'shish', callback_data=data.replace('date,', 'kuryer,')),
            types.InlineKeyboardButton('⏱Vaqt belgilash', callback_data=data.replace('date,', 'date,')))

    return but
