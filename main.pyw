from aiogram.utils import executor
from create_bot import dp, bot, admin_id
from handlers import client, admin
from keyboards import keybutton_start, keybutton_gen, keybutton_length
from linecache import getline


async def on_startup(_):

    message_for_user = 'Бот снова онлайн'
    await bot.send_message(admin_id, text=message_for_user, reply_markup=keybutton_start)

async def on_shutdown(_):

    message_for_user = 'Бот ушел в оффлайн на обновление или техническое обслуживание'
    await bot.send_message(admin_id,text=message_for_user)

client. register_handlers_client(dp)
admin.  register_handlers_client(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)