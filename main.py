import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, F, types
import aiohttp

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7804030886:AAFmqYAPW08gRlS6N6ASwqp5GXNPyifcS64")
dp = Dispatcher()

asyncio.run(dp.start_polling(bot))
