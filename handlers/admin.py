from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext, Dispatcher
from create_bot import bot
from keyboards import keybutton_admin, keybutton_admin_cancel, keybutton_start, message_dict
from linecache import getline
from dictionary import words_update


admin_id = int(getline('admin_id.txt',1).strip())

wodrs_for_cancel = ['отмена',
                    'отменить',
                    'отмени',
                    'cancel',
                    'отбой',
                    'стоп',
                    'stop']

class FSMAdmin(StatesGroup):
    words = State()

async def start(message: types.Message):
    'Проверка пользователя'

    if message.from_user.id == admin_id:
        message_for_admin = 'Обновить словарь или создать сообщение для всех?'
        
        await bot.send_message(admin_id,
                                message_for_admin,
                                reply_markup=keybutton_admin)

async def vocabulary(message: types.Message):

    if message.from_user.id == admin_id:
        await FSMAdmin.words.set()

        message_for_admin = 'Какие слова добавить в словарь? Пиши английскими буквами через пробел или с переносом строки'
        await bot.send_message(admin_id,
                                message_for_admin,
                                reply_markup=keybutton_admin_cancel)

async def vocabulary_update(message: types.Message, state: FSMContext):

    if message.from_user.id == admin_id and message.text != message_dict['cancel']:

        async with state.proxy() as data:
            data['words'] = message.text
        
        message_for_admin = words_update(data['words'])

        await bot.send_message(admin_id,
                                message_for_admin,
                                reply_markup=keybutton_admin)
        await state.finish()

    elif message.from_user.id == admin_id and message.text == message_dict['cancel']:
        await cancel_handler(message, state)

# ! Недоделланная функция!
async def message_for_all_users(message: types.Message):

    if message.from_user.id == admin_id:
        message_for_admin = 'Данный функционал еще не доделан!'

        await bot.send_message(admin_id,
                                message_for_admin,
                                reply_markup=keybutton_admin_cancel)

async def help(message: types.Message):
    
    if message.from_user.id == admin_id:
        message_for_admin = 'В панели админа можно обновить словарь и создать сообщение для всех'

        await bot.send_message(admin_id,
                                message_for_admin,
                                reply_markup=keybutton_admin)

async def cancel_handler(message: types.Message, state: FSMContext):
    
    if message.from_user.id == admin_id:

        # current_state = await state.get_state()
        # if current_state is None:
        #     return
        await state.finish()
        await bot.send_message(admin_id,'Операция отменена', reply_markup=keybutton_start)

def register_handlers_client(dp: Dispatcher):
    
    dp.register_message_handler(start,                  commands='admin',                                                   state=None)
    dp.register_message_handler(help,                   content_types=['text'], regexp=message_dict['help'])

    dp.register_message_handler(message_for_all_users,  content_types=['text'], regexp=message_dict['for all'],             state=None)

    dp.register_message_handler(vocabulary,             content_types=['text'], regexp=message_dict['update vocabulary'],   state=None)
    dp.register_message_handler(vocabulary_update,      content_types=['text'],                                             state=FSMAdmin.words)

    dp.register_message_handler(cancel_handler,         content_types=['text'], regexp=message_dict['cancel'])
    dp.register_message_handler(cancel_handler,         Text(equals=wodrs_for_cancel, ignore_case=True),                    state='*')