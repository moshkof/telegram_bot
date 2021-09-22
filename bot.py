from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor 
# from token import TOKEN

bot = Bot(token = "1611700510:AAH5poM-n5bLAHaxcTsBzSOCk38Qa64gsSE")

dp = Dispatcher(bot)

@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat_id
    text = "1611700510:AAH5poM-n5bLAHaxcTsBzSOCk38Qa64gsSE"
    sent_message = await bot.send_message(chat_id, text=text)
    print(sent_message.to_python())

executor.start_polling()