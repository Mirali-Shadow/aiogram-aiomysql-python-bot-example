from aiogram import types
import utils.db_api.db
from dispatcher import dp
from aiogram.filters import CommandStart


@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    await message.answer(await utils.db_api.db.commands.get_rows())
