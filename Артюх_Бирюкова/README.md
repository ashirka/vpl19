# Cловарь коллокатов
### О том, как функционирует наш код
Конечная цель нашего проекта - написание программы, позволяющей создавать словари коллокатов (слова в которых ранжируются по частоте встречаемости) по имеющимся текстовому файлу и ключевому слову. Подробный разбор нашего кода:
* Импортированы модуль *re* и *Counter*  из модуля *collections*:
***
    import re
    from collections import Counter

* Программа принимает на вход путь к текстовому файлу и записывает в переменную *text* его содержимое:
***
    file = input('Please set the path to the file: ')
    text = open(file, encoding='utf-8').read().lower()
    
* Используя регулярное выражение, избавились от лишних символов в текстовом файле, полученный список со словами записали в новую переменную *text1*:
***
    text1 = re.findall(r'\w+', text)

* Программа принимает на вход слово. Предварительно создали два пустых списка, в которых будут храниться слова, встречающиеся в тексте слева и справа от ключевого слова соответственно:
***
    word = input('Please type any word: ')
    before = []
    after = []
    
* Создали цикл, позволяющий искать коллокаты для ключевого слова, после чего коллокаты записываются в созданный нами ранее словарь. С помощью *Counter* создаётся словарь, коллокаты в котором ранжируются по частоте встречаемости. Результат выводится на экран:
***
    for i, m in enumerate(text1):
    if m == word:
        beforeword = text1[i - 1]
        afterword = text1[i + 1]
        before.append(beforeword)
        after.append(afterword)
        before_coll = Counter(before)
        after_coll = Counter(after)
        all = before + after
        all_coll = Counter(all)
    print('Words left statistics: ', before_coll, '\n')
    print('Words right statistics: ', after_coll, '\n')
    print('All words statistics: ', all_coll)

