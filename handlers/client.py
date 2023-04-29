from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext, Dispatcher
from create_bot import bot
from keyboards import keybutton_start, keybutton_gen, keybutton_length
from password_gen import password_gen
from random import randint
import re


wodrs_for_cancel = ['отмена',
                    'отменить',
                    'отмени',
                    'cancel',
                    'отбой',
                    'стоп',
                    'stop']

class FSMClient(StatesGroup):
    difficult = State()
    length = State()

async def user_check(user_id: str):
    filepath = 'users_id.txt'
    user_id = str(user_id)
    
    with open(filepath, 'r') as file:
        if user_id + '\n' in file.read():
            return
        else:
            await write_user_id(user_id, filepath)

async def write_user_id(user_id: str, filepath: str):
    with open(filepath, 'a') as file:
        user_id = user_id + '\n'
        file.write(user_id)

async def start(message: types.Message):
    message_for_user = 'Привет!\nЯ могу генерировать пароли различной сложности, а именно:\nпростой, сложный или очень сложный с заданной тобою длиной'

    await user_check(message.from_user.id)
    await bot.send_message(message.chat.id,
                            message_for_user,
                            reply_markup=keybutton_start)

async def help(message: types.Message):
    message_for_user = 'Данный бот генерирует по три пароля за раз, всё, что от тебя требуется, так это выбрать сложность и ввести желаемую длину, если выбрал не ту сложность, то нажми "Отмена"'
    await bot.send_message(message.chat.id,
                            message_for_user,
                            reply_markup=keybutton_start)

async def choice(message: types.Message):
    await FSMClient.difficult.set()

    message_for_user = '''Выбери сложность пароля, либо введи вручную'''
    await bot.send_message(message.chat.id, 
                            message_for_user,
                            reply_markup=keybutton_gen)

async def generate_pass(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['difficult'] = message.text
    await FSMClient.next()

    await FSMClient.length.set()

    message_for_user = '''Теперь напиши длину желаемого пароля в соответствии с ограничениями:\nпростой пароль: от 8 до 10 символов\nсложный пароль: от 8 до 24 символов\nочень сложный пароль: от 8 до 24 символов'''
    await bot.send_message(message.chat.id, 
                            message_for_user,
                            reply_markup=keybutton_length)

async def passwords(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['length'] = message.text
    
    async with state.proxy() as data:
        for i in range(0, 3):
            
            if data['length'] == 'Случайная длина':
                generated_pass = password_gen(type = data['difficult'], length = randint(8,24))
            else:
                regex = '\d+'
                length = data['length']

                length = re.search(regex, length).group(0)
                generated_pass = password_gen(type = data['difficult'], length = int(length))

            await bot.send_message(message.chat.id,
                                    generated_pass,
                                    reply_markup=keybutton_length)

    #await state.finish()

async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await  state.get_state()
    
    if current_state is None:
        return
    await state.finish()
    await message.reply('Отменено', reply_markup=keybutton_start)


def register_handlers_client(dp: Dispatcher):
    #Начало работы
    dp.register_message_handler(start,          commands='start',                                               state=None)
    dp.register_message_handler(help,           content_types=['text'], regexp='Помощь',                        state=None)

    #Машина состояний
    dp.register_message_handler(choice,         content_types=['text'], regexp='Придумай пароль',               state=None)
    dp.register_message_handler(generate_pass,  content_types=['text'], regexp='Простой|Сложный|Очень сложный', state=FSMClient.difficult)
    dp.register_message_handler(passwords,      content_types=['text'], regexp='\d+|Случайная длина',           state=FSMClient.length)

    #Выход из машины состояний
    dp.register_message_handler(cancel_handler, commands='Отмена',                                              state='*',)
    dp.register_message_handler(cancel_handler, Text(equals=wodrs_for_cancel, ignore_case=True),                state='*')