from aiogram import F, Router
from aiogram.filters import CommandStart, Command 
from aiogram.types import Message
from lib.utils import ReadText
from lib.utils import  mas_of_id , tme_url
from states import *

re = ReadText()
router = Router()

@router.message(CommandStart())
async def start(message: Message, state: FSMContext) -> None: 
	await state.set_state(Start.anon_message)
    whom_to_send_id = message.get_args() 
    user_id = message.from_user.id
    
    if user_id not in mas_of_id:

        NEW_URL = tme_url(user_id)

        await message.answer(f"{re.get_text("texts/start_message.txt")}+{NEW_URL}")

    
# Проверяет наличие пользователя в списках юзеров, создает ссылку если нужно и переносит на состояние снизу

@router.message(Start.anon_message)
async def send_anon_message(message: Message) -> None:
    pass

# Декоратор для состояния отправки сообщения 
