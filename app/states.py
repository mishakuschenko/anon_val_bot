from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

class Start(StatesGroup):
    anon_message = State()


