import xlrd

excel = xlrd.open_workbook('./базарецептов.xlsx') #открываем нашу базу с рецептами (30 рецептов в excel таблице)
sheet = excel.sheet_by_index(0)

print(' Добро пожаловать в базу рецептов!\nЗдесь ты можешь найти рецепт, который подойдет именно тебе!')

print('\nВведи сюда продукты, которые у тебя есть, а мы подберем для тебя рецепт и подскажем, если что-то нужно докупить')

txt = input('\nТвои продукты (через пробел без знаков препинания): ')
punc = ',./;"[]!@$%^&*()_/*\+#' #знаки препинания
numbers = '01234456789' #цифры
for word in txt: #очищаем продукты, введенные пользователем, от знаков препинаний и цифр
    for symbol in word:
        if symbol in punc:
            txt = input('Эй, мы просили без знаков препинания! Введи еще раз: ')
        if symbol in numbers:
            txt = input('Нам не нужно количество ингредиентов, будет достаточно их названия: ')

if 'яйца' in txt: #если у пользователя несколько яиц, программа выведет в том числе рецепты, для которых необходимо одно яйцо
    txt = txt + ' яйцо'

txt = txt.lower().split() #уменьшаем все буквы и формируем список из продуктов, введенных пользователем

row = 0 #первая строка в таблице

def reading_row(): #функция проходит через строку в базе рецептов и выводит рецепт из этой строки, если находит хотя бы 1 совпадения со списком продуктов
    global row
    global col
    global cellvalue
    col =- 1 #колонка базы рецептов с отрицательным значением, к которой мы прибавим 1 в цикле
    while col < 3: 
        col += 1
        if col == 1:
            cell = sheet.cell(row,col)
            cellvalue = cell.value.lower().split(', ') #ячейку со списком ингредиентов превращаем в список
    match=list(set(txt) & set(cellvalue)) #список из пересечений списков с ингредиентами и продуктами в наличии
    if len(match) > 0: #если найдены совпадения (список match не пустой)
        name = sheet.cell_value(row, 0) #присваиваем переменной значение ячейки с названием блюда
        recipe = sheet.cell_value(row, 2) #присваиваем переменной значение ячейки с рецептом
        what_you_need = list(set(cellvalue) - set(txt)) #разность списков с ингредиентами и продуктами в наличии=список с продуктами, которые нужно докупить
        what_you_need = ', '.join(what_you_need) #объединяем элементы списка в строку
        print('\nВот что ты можешь приготовить!\n')
        print('\n', name, '\n')
        print('\nЧто необходимо докупить:\n', what_you_need)
        print('\nРецепт:', recipe)
    

while row < sheet.nrows: #проходимся по всем строкам
    reading_row()
    row += 1 #переходим на следующий ряд
