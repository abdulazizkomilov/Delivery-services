import requests
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from keyboards.default.newkeyboards import menu
from keyboards.inline.admin import adminupdatebut, admincancelbut, \
    adminback, adminbacked, AdminAddKur, AdminAdDate, \
    admindateback, AdminbackDate
from loader import dp
from data.config import ADDRES
from save import OrderConfirm, OrderCalcel, Orderdate, OrderKuryer, OrderKuryerClear, OrderCleardate
from states.adminstate import myadminstate


@dp.callback_query_handler(text_startswith='confirm,')
async def Admincall(call: CallbackQuery):
    chat_id = call.data.strip(f"confirm\(\)\'uzb\',").split(',')[0]
    lang = call.data.strip(f"confirm\(\)\'\',").split('\'')[1]
    pk = call.data.strip(f"calcel\(\)\'\',").split('\'')[3]

    data = requests.get(f'{ADDRES}order/{pk}').json()

    text = f'✅Buyurtma № #{pk}A\nSizning buyurtmangiz tasdiqlandi va biz sizga tez orada yetkazib beramiz.'
    text_ru = f'✅Заказ № #{pk}A\nВаш ваш заказ подтвержден, мы доставим вам в ближайшее время.'

    if data['kuryer']:
        text_ru += f"\n\n<b>🚚Курьер</b>: {data['kuryer']}"
        text += f"\n\n<b>🚚Yetkazib beruvchi</b>: {data['kuryer']}"

    if data['date']:
        text += f"\n\n⏱<b>Yetkazib berish vaqti</b>: {data['date']}"
        text_ru += f"\n\n<b>⏱Срок поставки</b>: {data['date']}"

    if lang == 'rus':
        await dp.bot.send_message(chat_id=chat_id,
                                  text=text_ru, parse_mode='HTML')
    else:
        await dp.bot.send_message(chat_id=chat_id,
                                  text=text, parse_mode='HTML')
    OrderConfirm(pk)
    await dp.bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                           message_id=call.message.message_id,
                                           inline_message_id=call.message.chat.id,
                                           reply_markup=adminupdatebut
                                           (call.data, data['kuryer'],
                                            data['date'])
                                           )


@dp.callback_query_handler(text='confirmed')
async def Adminconfirmed(call: CallbackQuery):
    await call.answer(text="Mahsulot tasdiqlangan!", show_alert=True)


@dp.callback_query_handler(text_startswith='calcel,')
async def AdminCancel(call: CallbackQuery, state: FSMContext):
    chat_id = call.data.strip(f"calcel\(\)\'uzb\',").split(',')[0]
    lang = call.data.strip(f"calcel\(\)\'\',").split('\'')[1]
    pk = call.data.strip(f"calcel\(\)\'\',").split('\'')[3]
    OrderCalcel(pk)

    await dp.bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                           message_id=call.message.message_id,
                                           inline_message_id=call.message.chat.id,
                                           reply_markup=admincancelbut(call.data))

    if lang == 'rus':
        await dp.bot.send_message(chat_id=chat_id, text=f'❌Заказ № #{pk}A\nВаш заказ отменен!')
    else:
        await dp.bot.send_message(chat_id=chat_id,
                                  text=f'❌Buyurtma № #{pk}A\nSizning buyurtmangiz bekor qilindi!')
    await state.finish()


@dp.callback_query_handler(text_startswith='end')
async def AdminCanceled(call: CallbackQuery):
    await call.answer(text="Mahsulot bekor qilingan!", show_alert=True)


@dp.callback_query_handler(text_startswith='kuryer,')
async def AdminKuryer(call: CallbackQuery, state: FSMContext):
    pk = call.data.strip(f"kuryer\(\)\'\',").split('\'')[3]

    await state.update_data(
        {
            "pk": pk,
            "callmessage": call.message.text,
            "call.data": call.data
        }
    )

    await dp.bot.delete_message(call.message.chat.id, call.message.message_id)
    await dp.bot.send_message(chat_id=call.message.chat.id,
                              text=f"#{pk}A Buyurtmaga kuryer ma'lumotlarini yuboring!",
                              reply_markup=adminback())
    await myadminstate.back.set()


@dp.message_handler(state=myadminstate.back)
async def Adminback(message: Message, state: FSMContext):
    data = await state.get_data()

    callmessage = data.get("callmessage")
    calldata = data.get("call.data")
    pk = data.get("pk")

    date = requests.get(f'{ADDRES}order/{data.get("pk")}').json()['date']

    if message.text == '⬅️ Orqaga':
        await state.finish()
        await dp.bot.delete_message(message.chat.id, message.message_id)

        if date:
            await dp.bot.send_message(chat_id=message.chat.id,
                                      text="Kuryer qo'shish bekor qilindi",
                                      reply_markup=menu)

            await dp.bot.send_message(chat_id=message.chat.id,
                                      text=callmessage,
                                      reply_markup=AdminbackDate(calldata, date))
        else:
            await dp.bot.send_message(chat_id=message.chat.id,
                                      text="Kuryer qo'shish bekor qilindi",
                                      reply_markup=menu)

            await dp.bot.send_message(chat_id=message.chat.id,
                                      text=callmessage,
                                      reply_markup=adminbacked(calldata))
    else:
        OrderKuryer(pk, message.text)
        if date:
            await dp.bot.delete_message(message.chat.id, message.message_id)

            await dp.bot.send_message(chat_id=message.chat.id,
                                      text=f"Kuryer qo'shildi",
                                      reply_markup=menu)

            await dp.bot.send_message(chat_id=message.chat.id,
                                      text=callmessage,
                                      reply_markup=
                                      AdminAdDate(calldata.replace('kuryer,', 'date,'),
                                                  message.text, date),
                                      parse_mode='HTML')
        else:
            await dp.bot.delete_message(message.chat.id, message.message_id)

            await dp.bot.send_message(chat_id=message.chat.id,
                                      text=f"Kuryer qo'shildi",
                                      reply_markup=menu)

            await dp.bot.send_message(chat_id=message.chat.id,
                                      text=callmessage,
                                      reply_markup=AdminAddKur(calldata, message.text),
                                      parse_mode='HTML')
        await state.finish()


@dp.callback_query_handler(text_startswith='date,')
async def AdminKuryer(call: CallbackQuery, state: FSMContext):
    pk = call.data.strip(f"date\(\)\'\',").split('\'')[3]

    await state.update_data(
        {
            "pk": pk,
            "callmessage": call.message.text,
            "call.data": call.data
        }
    )

    await dp.bot.delete_message(call.message.chat.id, call.message.message_id)

    await dp.bot.send_message(chat_id=call.message.chat.id,
                              text=f"#{pk}A Buyurtmaga vaqt belgilang!",
                              reply_markup=adminback())
    await myadminstate.date.set()


@dp.message_handler(state=myadminstate.date)
async def AdminAddDate(message: Message, state: FSMContext):
    data = await state.get_data()

    callmessage = data.get("callmessage")
    calldata = data.get("call.data")
    pk = data.get("pk")

    kuryermessage = requests.get(f'{ADDRES}order/{pk}').json()['kuryer']

    if message.text == '⬅️ Orqaga':
        await state.finish()
        await dp.bot.delete_message(message.chat.id, message.message_id)

        if kuryermessage:
            await dp.bot.send_message(chat_id=message.chat.id,
                                      text=f"Vaqt belgilash bekor qilindi",
                                      reply_markup=menu)

            await dp.bot.send_message(chat_id=message.chat.id,
                                      text=callmessage,
                                      reply_markup=AdminAddKur
                                      (calldata, kuryermessage),
                                      parse_mode='HTML')
        else:
            await dp.bot.send_message(chat_id=message.chat.id,
                                      text="Vaqt belgilash bekor qilindi",
                                      reply_markup=menu)

            await dp.bot.send_message(chat_id=message.chat.id,
                                      text=callmessage,
                                      reply_markup=admindateback(calldata))
    else:
        Orderdate(pk, message.text)
        await dp.bot.delete_message(message.chat.id,
                                    message.message_id)

        if kuryermessage:
            await dp.bot.send_message(chat_id=message.chat.id,
                                      text=f"Vaqt qo'shildi",
                                      reply_markup=menu)

            await dp.bot.send_message(chat_id=message.chat.id,
                                      text=callmessage,
                                      reply_markup=AdminAdDate
                                      (calldata, kuryermessage, message.text),
                                      parse_mode='HTML')
        else:
            await dp.bot.send_message(chat_id=message.chat.id,
                                      text=f"Vaqt qo'shildi",
                                      reply_markup=menu)

            await dp.bot.send_message(chat_id=message.chat.id,
                                      text=callmessage,
                                      reply_markup=AdminbackDate
                                      (calldata, message.text),
                                      parse_mode='HTML')
        await state.finish()


@dp.callback_query_handler(text='kuryeraded')
async def AdminKureraded(call: CallbackQuery):
    await call.answer(text="Kuryer qo'shilgan! Agar o'zgartirmoqchi "
                           "bo'lsangiz qo'shilgan kuryer ustiga bosib "
                           "o'chiring va kuryerni qo'shing!", show_alert=True)


@dp.callback_query_handler(text='dateadd')
async def AdminKureraded(call: CallbackQuery):
    await call.answer(text="Vaqt belgilangan! Agar o'zgartirmoqchi "
                           "bo'lsangiz belgilangan vaqtni ustiga bosib "
                           "o'chiring va vaqt belgilang!", show_alert=True)


@dp.callback_query_handler(text_startswith='kuryerclear')
async def AdminKuryerClear(call: CallbackQuery):

    pk = call.data.strip(f"kuryerclear\(\)\'\',").split('\'')[3]
    date = requests.get(f'{ADDRES}order/{pk}').json()['date']

    OrderKuryerClear(pk)

    await dp.bot.delete_message(call.message.chat.id, call.message.message_id)

    if date:
        await dp.bot.send_message(chat_id=call.message.chat.id,
                                  text=call.message.text,
                                  reply_markup=AdminbackDate(
                                      call.data.replace('kuryerclear', 'date'), date))

    else:
        await dp.bot.send_message(chat_id=call.message.chat.id,
                                  text=call.message.text,
                                  reply_markup=adminbacked(
                                      call.data.replace('kuryerclear', 'kuryer')))


@dp.callback_query_handler(text_startswith='dateclear')
async def AdminKuryerClear(call: CallbackQuery):

    pk = call.data.strip(f"dateclear\(\)\'\',").split('\'')[3]
    kuryer = requests.get(f'{ADDRES}order/{pk}').json()['kuryer']

    OrderCleardate(pk)

    await dp.bot.delete_message(call.message.chat.id, call.message.message_id)
    if kuryer:
        await dp.bot.send_message(chat_id=call.message.chat.id,
                                  text=call.message.text,
                                  reply_markup=AdminAddKur(
                                      call.data.replace('dateclear', 'kuryer'), kuryer))

    else:
        await dp.bot.send_message(chat_id=call.message.chat.id,
                                  text=call.message.text,
                                  reply_markup=adminbacked(
                                      call.data.replace('dateclear', 'kuryer')))
