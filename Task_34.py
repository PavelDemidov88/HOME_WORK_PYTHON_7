# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам 

def vowel_count_rus(text):
    vowels = "уеыаоэяиюё"
    vowel_count = sum(text.count(vowel) for vowel in vowels)
    return vowel_count

def div(a):
    ele = vowel_count_rus(a[0])
    chk = True
    for words in a:
        if ele != vowel_count_rus(words):
            chk = False
            break
    if (chk == True):
        print('Парам пам-пам')
    else:
        print('Пам парам')

verse = input('Введите куплет, слова через дефис, фразы через пробел: ')
verse = verse.lower()
f = verse.split()

div(f)
