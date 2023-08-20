from aiogram.dispatcher.filters.state import StatesGroup, State

class CommentData(StatesGroup):
    # Foydalanuvchi buyerda 3 ta holatdan o'tishi kerak
    comment = State() # ism

