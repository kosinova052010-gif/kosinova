# Імпортуємо бібліотеки
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart

# Сюди вставляємо свій токен з BotFather
API_TOKEN = "8639073581:AAHFutVM4byP0sjt9VKpAW2zeh9OlweCleI"

# Створюємо бота і диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Що таке океан?")],
        [KeyboardButton(text="Цікавий факт")],
        [KeyboardButton(text="Допомога")]
    ],
    resize_keyboard=True
)



# Обробник команди /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привіт! Я твій помічник з океанології!", reply_markup=keyboard)


@dp.message()
async def handle_message(message: Message):
    if message.text == "Що таке океан?":
        await message.answer("Океан — це величезна маса солоної води, яка покриває більшу частину Землі 🌍")

    elif message.text == "Цікавий факт":
        await message.answer("Найглибше місце в океані — Маріанська западина (~11 км) 😮")

    elif message.text == "Допомога":
        await message.answer("Натискай кнопки і дізнавайся більше про океан 🌊")

    else:
        await message.answer("Я не зрозумів 😅 Спробуй натиснути кнопку")

# Головна функція для запуску бота
async def main():
    await dp.start_polling(bot)


# Запускаємо
if __name__ == "__main__":
    asyncio.run(main())
