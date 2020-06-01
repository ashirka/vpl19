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

import re, os

paradigm_adj = 'ый ий ой ая ое ые ие ого его ой ей ых их ому ему им ым ую юю ими ыми ом ем'

titles_number = {}
all_found_matches = {}

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
        if len(user_words) == 1:
            rex_user = ' ' + word1[:-1] + '[а-я]{0,3}' + ' '
            found_match = re.findall(rex_user, text, re.I)
            #print(found_match)
            all_found_matches[file] = found_match
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
            #rex_user = re.compile(rex_user)
            #print(rex_user)
            found_match = re.findall(rex_user, text, re.I)
            print(found_match)
            all_found_matches[file] = found_match
            found_numbers = len(found_match)
            titles_number[text_title] = [found_numbers]
            titles_number[text_title] += [file]

list_titles_number = list(titles_number.items())
list_titles_number.sort(key=lambda i: i[1])
list_titles_number = list_titles_number[::-1]

print(list_titles_number)
print(all_found_matches)

printed_text = ''
# need_words_1 = []
# need_words_2 = []

for found_text in list_titles_number:
    print(found_text)
    opened_file = found_text[1][1]
    with open(opened_file, encoding='utf-8') as info:
        info = info.read()
        text_parts = info
        context_need = []
        for index, word in enumerate(all_found_matches[opened_file]):
            if index == (len(all_found_matches[opened_file]) - 1):
                text_parts = text_parts.split(word, maxsplit=1)
                context_need += [text_parts[0] + word]
                context_need += [text_parts[1]]
            else:
                text_parts = text_parts.split(word, maxsplit=1)
                context_need += [text_parts[0] + word]
                text_parts = text_parts[1]
        #print(context_need)
        printed_text = ''
        for i_part, part in enumerate(context_need):
            list_part = part.split()
            n_words = len(list_part)
            if i_part == 0:
                if n_words >= 11:
                    need_words = list_part[-11:]
                    beginning_of_text = ' '.join(need_words)
                    printed_text += '... ' + beginning_of_text + ' '
                else:
                    printed_text += ' '.join(list_part) + ' '
            elif i_part == (len(context_need) - 1):
                if n_words >= 11:
                    need_words = list_part[:11]
                    printed_text += ' '.join(need_words) + '\n'
                else:
                    printed_text += ' '.join(list_part)+ '\n'
            else:
                if n_words >= 21:
                    need_words_1 = list_part[:11]
                    part_1 = ' '.join(need_words_1)
                    need_words_2 = list_part[-11:]
                    part_2 = ' '.join(need_words_2)
                    printed_text += part_1 + '...\n...' + part_2 + ' '
                else:
                    printed_text += ' '.join(list_part) + ' '
        milky_way = os.path.abspath(opened_file)
        print(milky_way)
        print(found_text[0])
        print(printed_text)

        if printed_text:
            print(printed_text)
        else:
            print('Совпадений не найдено :(')









