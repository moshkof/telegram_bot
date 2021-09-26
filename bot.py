from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
# from token import TOKEN
import config

bot = Bot(token=config.TOKEN)

dp = Dispatcher(bot, run_tasks_by_default=True)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = "Привет, "
    greeting = "На связи с Вами Сергей Мошков!\nЭто бот, который был рожден 26 сентября 2021 года.\nОн будет способен на многое..."
    sent_message = await bot.send_message(chat_id,
                                          text=(text + message.chat.last_name + " " + message.chat.first_name + "!"))
    print(sent_message.to_python())
    # await bot.send_photo(chat_id, photo="https://sun9-17.userapi.com/impg/-16hFI5UPGx1HzcsH9pWS7CRbVJVDkeLAClqaQ/ro1psdJ4XCw.jpg?size=1620x2160&quality=96&sign=c19c87b3705232e52861b07c40478d00&type=album")
    sent_photo = await bot.send_photo(chat_id,
                                      photo="https://sun9-35.userapi.com/impg/fiFPU2a13im1Ui-G1JrACnyXoQQdZ_bWsdjSig/AsVqVJU5iV8.jpg?size=2560x1920&quality=95&sign=1b282e772d8ea4a8327db48ef9200c0d&type=album")
    await bot.send_message(chat_id, text=greeting)
    print(sent_photo.to_python())


executor.start_polling(dp)
