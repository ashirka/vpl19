import time 


# Определяем текущую дату с помощью модуля time 

date = time.strftime("%d.%m.%Y", time.localtime()) # результат вида - дд.мм.гггг.
print('Сегодняшняя дата:', date)
date = date.split('.') # результат вида - ['дд', 'мм', 'гггг']


# Распределяем месяцы по количеству дней в них + определяем, високосный ли год

thirty_one_d = ['01', '03', '05', '07', '08', '10']
thirty_d = ['04', '06', '09', '11']
year_type = int(date[2]) % 4 # если год делится на 4 без остатка, то он високосный (28 + 1 дней в феврале)


# Если сегодня последний день месяца (кроме декабря), то следующий день будет вида - 01.текущий_месяц+1.гггг

if (date[1] in thirty_d and date[0] == '30') or \
   (date[1] in thirty_one_d and date[0] == '31') or \
   (date[1] == '02' and year_type == 0 and date[0] == '29') or \
   (date[1] == '02' and year_type != 0 and date[0] == '28'):

    next_date = time.strptime('01 ' + str(int(date[1]) + 1) + ' ' + date[2], '%d %m %Y')
    next_date = time.strftime('%d.%m.%Y', next_date)
    print('Гороскоп составлен на следующую дату:', next_date)


# Если сегодня 31 декабря, то следующий день будет вида - 01.01.текущий_год+1

elif date[0] == '31' and date[1] == '12':

    next_date = time.strptime('01 01 ' + str(int(date[2]) + 1), '%d %m %Y')
    next_date = time.strftime('%d.%m.%Y', next_date)
    print('Гороскоп составлен на следующую дату:', next_date) 


# Если сегодня не последний день месяца, то следующий день будет вида - текущий_день+1.мм.гггг

else:
    
    next_date = time.strptime(str(int(date[0]) + 1) + ' ' + date[1] + ' ' + date[2], '%d %m %Y')
    next_date = time.strftime('%d.%m.%Y', next_date)
    print('Гороскоп составлен на следующую дату:', next_date)


    


