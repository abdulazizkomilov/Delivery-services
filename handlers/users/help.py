from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from keyboards.default.newkeyboards import menu
from loader import dp
from states.orderState import RegOrderData, OrderData


@dp.message_handler(commands='developer')
async def show_menu(message: Message):
    await message.answer(f"Sizga ham shunday bot yoki har qanday bot yaratish "
                         f"kerak bo'lsa biz bilan bog'laning: @abdulaziz9963", reply_markup=menu)


@dp.message_handler(commands='developer', state=OrderData)
async def show_menu(message: Message, state: FSMContext):
    await message.answer(f"Sizga ham shunday bot yoki har qanday bot yaratish "
                         f"kerak bo'lsa biz bilan bog'laning: @abdulaziz9963", reply_markup=menu)
    await state.finish()


@dp.message_handler(commands='developer', state=RegOrderData)
async def show_menu(message: Message, state: FSMContext):
    await message.answer(f"Sizga ham shunday bot yoki har qanday bot yaratish "
                         f"kerak bo'lsa biz bilan bog'laning: @abdulaziz9963", reply_markup=menu)
    await state.finish()
