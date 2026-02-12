# Імпортуємо бібліотеки
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

# Сюди вставляємо свій токен з BotFather
API_TOKEN = "8249532278:AAGszkVYltFKP_7uSPvw_Fd9jKP5dxrZn-Q"

# Створюємо бота і диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Обробник команди /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привіт! Я твій перший бот!")


# Головна функція для запуску бота
async def main():
    await dp.start_polling(bot)


# Запускаємо
if __name__ == "__main__":
    asyncio.run(main())