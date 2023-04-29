from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

message_dict = {'for all': 'Сообщение для всех',
                'update vocabulary': 'Обновить словарь',
                'cancel': 'Отмена операции',
                'help': 'Помочь'}

button_message_for_all = KeyboardButton(message_dict['for all'])
button_update_words = KeyboardButton(message_dict['update vocabulary'])
button_cancel = KeyboardButton(message_dict['cancel'])
button_help = KeyboardButton(message_dict['help'])

keybuttons_admin = [button_message_for_all,
                    button_update_words,
                    button_cancel,
                    button_help]


keybutton_admin         = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keybutton_admin_cancel  = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

for button in keybuttons_admin:
    keybutton_admin.insert(button)

keybutton_admin_cancel.insert(button_cancel)