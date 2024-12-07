from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm import FSMContext
from lib.utils import ReadText
from lib.utils import mas_of_id, tme_url
from states import Start

re = ReadText()
router = Router()

@router.message(CommandStart())
async def start(message: Message, state: FSMContext) -> None: 
    await state.set_state(Start.anon_message)
    whom_to_send_id = message.get_args() 
    user_id = message.from_user.id
    
    if user_id not in mas_of_id:
        NEW_URL = tme_url(user_id)
        await message.answer(f"{re.get_text('texts/start_message.txt')} + {NEW_URL}")

@router.message(Start.anon_message)
async def send_anon_message(message: Message, state: FSMContext) -> None:
    user_data = await state.get_data()
    whom_to_send_id = user_data.get('whom_to_send_id')  

    if whom_to_send_id:
        try:
            await message.bot.send_message(whom_to_send_id, message.text)
            await message.answer("Сообщение отправлено!")
        except Exception as e:
            await message.answer(f"Не удалось отправить сообщение: {str(e)}")
    else:
        await message.answer("ID получателя не найден. Пожалуйста, попробуйте заново.")

    await state.clear()

