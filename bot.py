import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import requests

# Создаем экземпляр бота и диспетчера
bot = Bot(token="TOKEN")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Обработчик команды /memes
@dp.message_handler(commands=['memes'])
async def send_random_meme(message: types.Message):
    # Получаем рандомный мем
    meme_url = get_random_meme()
    
    # Отправляем мем пользователю
    await bot.send_photo(message.chat.id, meme_url)

# Функция для получения рандомного мема
def get_random_meme():
    # Получаем список мемов с помощью API Imgflip
    response = requests.get("https://api.imgflip.com/get_memes")
    memes = response.json()['data']['memes']
    
    # Выбираем рандомный мем из списка
    random_meme = random.choice(memes)
    
    # Возвращаем URL мема
    return random_meme['url']

# Запускаем бота
if __name__ == '__main__':
    asyncio.run(dp.start_polling())
