from aiogram import types

from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):

    # поучим chat_id и текст
    chat_id = message.from_user.id
    text = message.text

    # поучим объект бота из модуля loader
    from loader import bot

    await bot.send_message(chat_id=chat_id, text=text)