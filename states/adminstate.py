from aiogram.dispatcher.filters.state import StatesGroup, State


class myadminstate(StatesGroup):
    back = State()
    kuryer = State()
    date = State()