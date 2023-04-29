def rus_number_match(text: str) -> bool:
    alphabett=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    return not alphabett.isdisjoint(text.lower())
    
def number_match(text: str) -> bool:
    numbers=set('1234567890')
    return not numbers.isdisjoint(text.lower())

def words_update(words: str) -> str:
    'Обновляет словарь для генерации паролей'

    file_path = './dictionary/words.txt'

    if rus_number_match(words) == True:
        return 'Словарь не обновлен!\nНужно написать на английском языке и не использовать цифры'
    elif number_match(words) == True:
        return 'Словарь не обновлен!\nНельзя использовать цифры'
        
    words = '\n' + words.strip().replace(' ', '\n')

    with open(file_path, 'a') as words_file:
        words_file.write(words)
    return 'Словарь обновлен'