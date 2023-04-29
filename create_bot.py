from linecache import getline
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


admin_id = int(getline('admin_id.txt',1).strip())
storage = MemoryStorage()

token = str(getline('token.txt',1).strip())
token_for_test = str(getline('token_for_test.txt',1).strip())

bot = Bot(token)
dp = Dispatcher(bot, storage = storage)