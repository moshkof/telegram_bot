from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
# from token import TOKEN
import config

<<<<<<< HEAD
bot = Bot(token=config.TOKEN)
=======
bot = Bot(token="1611700510:AAH5poM-n5bLAHaxcTsBzSOCk38Qa64gsSE")
>>>>>>> 72930c95a759056635418865b2a3b670efa893a2

dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = "Привет, "
    sent_message = await bot.send_message(chat_id, text=(text + message.chat.last_name + " " + message.chat.first_name + "!"))
    print(sent_message.to_python())

<<<<<<< HEAD
executor.start_polling(dp)
=======
executor.start_polling(dp)
>>>>>>> 72930c95a759056635418865b2a3b670efa893a2
