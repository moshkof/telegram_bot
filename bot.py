from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
# from token import TOKEN
import config

bot = Bot(token=config.TOKEN)

dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = "Привет, "
    sent_message = await bot.send_message(chat_id, text=(text + message.chat.last_name + " " + message.chat.first_name + "!"))
    print(sent_message.to_python())

executor.start_polling(dp)
