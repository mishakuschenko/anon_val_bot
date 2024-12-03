from aiogram import F, Router
from aiogram.filters import CommandStart, Command 
from aiogram.types import Message
from lib.utils import ReadText

re = ReadText()
router = Router()

@router.message(CommandStart())
async def start(message: Message) -> None: 
	await message.answer(f"{re.get_text("texts/start_message.txt")}")
    print("Привет Денис")



