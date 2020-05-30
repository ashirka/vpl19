'''здеся будет наш суперкоТ
Создать базу текстов (минимум 10). Программа принимает на вход
слово или сочетание слов, после чего выводит путь к текстовым файлам,
где встречается это слово (сочетание слов), и отрывки из этих файлов,
где встречается слово (слово + 10-15 слов вокруг). Выводные данные должны
быть ранжированы: чем чаще в данном тексте встретилось данное слово,
тем выше текст в выдаче'''
'''Схема работы:
1. экслауэр - перевод ответа в нижние буковки
2. открываем текстовый файл, ищем слово/слова, считаем кол-во, кидаем в список (или словарь как пойдет)
3. выводим название файла - название статьи - отрывок с искомым словом (сколько слов найдено - столько и 
отрывков) -  название другого файла и тд. по частоте встречания

мы разделяем по регулярке слова, потом у нас есть список со строками, и мы из них вычленяем по 10 слов
с первой строки - с конца, с последней строки - с начала, в остальных - с обеихь сторон при эжтом если там меньше 20
слов, то мы выдергиваем всю эту строку'''

import re

paradigm_adj = 'ый ий ой ая ое ые ие ого его ой ей ых их ому ему им ым ую юю ими ыми ом ем'

titles_number = {}

user = input('Поиск по слову (сочетанию слов):  ')
user = user.lower()
n = user.count(' ')
if n == 0:
    word1 = user
    user_words = [word1]
elif n == 1:
    word1, word2 = user.split()
    user_words = [word1, word2]
elif n == 2:
    word1, word2, word3 = user.split()
    if len(word1) <= 2:
        word1 = word2
        word2 = word3
        user_words = [word1, word2]
    elif len(word2) <= 2:
        word2 = word3
        user_words = [word1, word2]

for i in range(1, 12):
    file = 'text_' + str(i) + '.txt'
    with open(file, encoding='utf-8') as text:
        text = text.read()
        needless_tag = r'^\[a-z]+'
        text = re.sub(needless_tag, '', text)
        regex_title = r'^.+$'
        text_title = re.search(regex_title, text, re.M)
        text_title = text_title.group()
        #text = text.lower()
        if len(user_words) == 1:
            rex_user = ' ' + word1[:-1] + '[а-я]{0,3}' + ' '
            #regex_user = re.compile(rex_user)
            found_match = re.findall(rex_user, text, re.I)
            #print(found_match)
            found_numbers = len(found_match)
            titles_number[text_title] = [found_numbers]
            titles_number[text_title] += [file]
        elif len(user_words) == 2:
            if (word1[-3:] in paradigm_adj) or (word2[-3:] in paradigm_adj):
                if word1[-3:] in paradigm_adj:
                    rex_user = word1[:-3] + '[а-я]{0,3}' + '\s(\S)*( )*' + word2[:-1] + '[а-я]{0,3}'
                elif word2[-3:] in paradigm_adj:
                    rex_user = word1[:-1] + '[а-я]{0,3}' + '\s(\S)*( )*' + word2[:-3] + '[а-я]{0,3}'
            elif (word1[-2:] in paradigm_adj) or (word2[-2:] in paradigm_adj):
                rex_user = word1[:-2] + '[а-я]{0,3}' + '\s(\S)*( )*' + word2[:-2] + '[а-я]{0,3}'
            else:
                rex_user = word1[:-1] + '[а-я]{0,3}' + '\s(\S)*( )*' + word2[:-1] + '[а-я]{0,3}'
            #regex_user = re.compile(rex_user)
            found_match = re.findall(rex_user, text, re.I)
            #print(found_match)
            found_numbers = len(found_match)
            titles_number[text_title] = found_numbers
        #list = text.split()
        #print(list)
        '''gh = r'(\W*[А-Яа-яA-Za-zё\d]+\W*){3}холод'
        jaerbf = re.findall(gh, text)
        print(jaerbf)'''


list_titles_number = list(titles_number.items())
list_titles_number.sort(key=lambda i: i[1])
list_titles_number = list_titles_number[::-1]

print(list_titles_number)





