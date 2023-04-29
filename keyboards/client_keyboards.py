from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_start = KeyboardButton('Придумай пароль')
button_help = KeyboardButton('Помощь')

button_easy = KeyboardButton('Простой')
button_difficult = KeyboardButton('Сложный')
button_very_difficult = KeyboardButton('Очень сложный')
button_cancel = KeyboardButton('Отмена')


button_int = KeyboardButton('Случайная длина')

keybuttons_start = [button_start,
                    button_help]

keybuttons_gen = [button_easy,
                    button_difficult,
                    button_very_difficult,
                    button_cancel]

keybuttons_length = [button_int,
                    button_cancel]

keybutton_start = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keybutton_gen = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keybutton_length = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

for button in keybuttons_start:
    keybutton_start.insert(button)

for button in keybuttons_gen:
    keybutton_gen.insert(button)

for button in keybuttons_length:
    keybutton_length.insert(button)

# await message.reply(reply_text, reply_markup=types.ReplyKeyboardRemove())