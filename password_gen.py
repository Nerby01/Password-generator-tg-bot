import hashlib, time, random
from linecache import getline, checkcache, clearcache


filepath = './dictionary/words.txt'

def password_gen(type: str='Простой', length: int=8) -> str:
    
    '''Генерация пароля типов простой, сложный или очень сложный с заданной длиной'''

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    password = ''

    if length > 24:
        length = 24
    elif length < 8:
        length = 8
    
    match type.lower():

        case 'простой':
            
            checkcache(filepath)

            random.seed(time.time()*1000, version=2)
            rand_int = str(random.random())[2:5]

            word_list = words_gen()

            password = str(word_list[0] + rand_int + word_list[1])[:10]

            clearcache()

        case 'сложный':

            checkcache(filepath)

            random.seed(time.time()*1000, version=2)
            rand_int = str(random.random())[2:6]
            rand_int_2 = str(random.random())[2:15]

            word_list = words_gen()

            password = str(word_list[0] + rand_int + word_list[1]+rand_int_2)[:length]

            clearcache()

        case 'очень сложный':

            curr_time = round(time.time()*1000)
            hash = str(hashlib.md5(str(curr_time).encode()).hexdigest())[:length]
            for i in alphabet:
                password = hash.replace(i,i.upper(),1)
                if password != hash:
                    break

    return password

def words_gen() -> list:
    '''Выбор случайных слов из текстового файла'''

    line_count = sum(1 for line in open(filepath))
    first_word = getline(filepath, random.randint(0, line_count), ).capitalize().strip()
    second_word = getline(filepath, random.randint(0, line_count)).capitalize().strip()

    if first_word == '': first_word = 'EmptyWord'
    elif second_word == '': second_word = 'EmptyWord'

    return [first_word, second_word]
# a = password_gen('сложный',25)
# print(a)