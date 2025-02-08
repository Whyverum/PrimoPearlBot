from enum import StrEnum
from aiogram.fsm.state import StatesGroup, State

class Survey(StatesGroup):
    full_name = State()
    age = State()
    email = State()
    sport = State()
    email_newsletter = State()


class Sports(StrEnum):
    tennis = "Теннис"
    football = "Футбол"
    fomula_one = "Гонки"
