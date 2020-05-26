'''здеся будет наш суперкоТ
Создать базу текстов (минимум 10). Программа принимает на вход
слово или сочетание слов, после чего выводит путь к текстовым файлам,
где встречается это слово (сочетание слов), и отрывки из этих файлов,
где встречается слово (слово + 10-15 слов вокруг). Выводные данные должны
быть ранжированы: чем чаще в данном тексте встретилось данное слово,
тем выше текст в выдаче'''
'''Схема работы:
1. эслауэр - перевод ответа в нижние буковки
2. открываем текстовый файл, ищем слово/слова, считаем кол-во, кидаем в список (или словарь как пойдет)
3. выводим название файла - название статьи - отрывок с искомым словом (сколько слов найдено - столько и 
отрывков) -  название другого файла и тд. по частоте встречания'''
import re

titles_number = {}

user = input('Поиск по слову (сочетанию слов):  ')
user = user.lower()

for i in range(1, 12):
    file = 'text_' + str(i) + '.txt'
    with open(file, encoding='utf-8') as text:
        text = text.read()
        needless_tag = r'^\[a-z]+'
        text = re.sub(needless_tag, '', text)
        regex_title = r'^.+$'
        text_title = re.search(regex_title, text, re.M)
        text_title = text_title.group()
        text = text.lower()
        rex_user = ' ' + user[:-1] + '[а-я]{0,3}' + ' '
        regex_user = re.compile(rex_user)
        found_match = re.findall(regex_user, text)
        found_numbers = len(found_match)
        titles_number[text_title] = found_numbers

list_titles_number = list(titles_number.items())
list_titles_number.sort(key=lambda i: i[1])
list_titles_number = list_titles_number[::-1]

print(list_titles_number)





