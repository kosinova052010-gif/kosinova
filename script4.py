import asyncio
import random
from aiogram import Bot, Dispatcher
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)
from aiogram.filters import CommandStart, Command

API_TOKEN = "8639073581:AAHLnN4Y2YjQei32dByh8yj_M0GbRuUyH7c"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# 🔹 ЗВИЧАЙНА КЛАВІАТУРА
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="що таке океан?")],
        [KeyboardButton(text="цікавий факт")],
        [KeyboardButton(text="допомога")]
    ],
    resize_keyboard=True
)

# 🔹 ДАНІ КОРИСТУВАЧІВ
user_data = {}

# 🔹 ПИТАННЯ
quiz_questions = [
    {
        "question": "Який океан найбільший?",
        "options": ["Атлантичний", "Індійський", "Тихий"],
        "correct": "Тихий"
    },
    {
        "question": "Найглибше місце океану?",
        "options": ["Маріанська западина", "Бермудський трикутник", "Червоне море"],
        "correct": "Маріанська западина"
    },
    {
        "question": "Скільки океанів на Землі?",
        "options": ["3", "4", "5"],
        "correct": "5"
    }
]

# 🔹 ФАКТИ
facts = [
    "Океан покриває понад 70% Землі",
    "Маріанська западина глибша за Еверест",
    "У океані більше 200 000 видів",
    "Світіння океану — це біолюмінесценція",
    "Найбільша тварина — синій кит"
]

# 🔹 ФУНКЦІЯ ПИТАННЯ
def get_question(user_id):
    question = random.choice(quiz_questions)

    user_data[user_id]["correct"] = question["correct"]

    buttons = [
        [InlineKeyboardButton(text=opt, callback_data=f"answer:{opt}")]
        for opt in question["options"]
    ]

    return question["question"], InlineKeyboardMarkup(inline_keyboard=buttons)


# /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    name = message.from_user.first_name
    await message.answer(f"Привіт, {name}!", reply_markup=keyboard)


# /help
@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer("/play — вікторина\nНатискай кнопки")


# /play
@dp.message(Command("play"))
async def play_handler(message: Message):
    user_id = message.from_user.id
    name = message.from_user.first_name

    user_data[user_id] = {"score": 0}

    question, kb = get_question(user_id)

    await message.answer(f"{name}, починаємо вікторину! 🎮\n\n{question}", reply_markup=kb)


# 🔹 ВІДПОВІДЬ
@dp.callback_query(lambda c: c.data.startswith("answer:"))
async def handle_answer(callback: CallbackQuery):
    user_id = callback.from_user.id
    name = callback.from_user.first_name

    user_answer = callback.data.split(":")[1]
    correct = user_data[user_id]["correct"]

    if user_answer == correct:
        user_data[user_id]["score"] += 1
        text = f"{name}, правильно!\nРахунок: {user_data[user_id]['score']}"
    else:
        text = f"{name}, неправильно\nПравильна: {correct}"

    next_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Наступне питання", callback_data="next")]
        ]
    )

    await callback.message.answer(text, reply_markup=next_kb)
    await callback.answer()


# 🔹 НАСТУПНЕ ПИТАННЯ
@dp.callback_query(lambda c: c.data == "next")
async def next_question(callback: CallbackQuery):
    user_id = callback.from_user.id

    question, kb = get_question(user_id)

    await callback.message.answer(f"Наступне питання\n\n{question}", reply_markup=kb)
    await callback.answer()


# 🔹 ОБРОБКА КНОПОК
@dp.message()
async def handle_message(message: Message):
    name = message.from_user.first_name
    text = message.text.lower()

    if text == "що таке океан?":
        await message.answer(f"{name}, океан — це величезна маса солоної води")

    elif text == "цікавий факт":
        fact = random.choice(facts)
        await message.answer(f"{name}, {fact}")

    elif text == "допомога":
        await message.answer(f"{name}, напиши /play 🎮")

    else:
        await message.answer(f"{name}, я не зрозумів")


# запуск
async def main():
    print("Бот запущений 🚀")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


