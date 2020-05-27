import time
birthday = input ('Когда вы родились?')# получается, пользователь вводит дату в формате дд.мм.гггг либо, например, 12 апреля 2012, с годом или без
if '.' in birthday:
    birthday = birthday.split ('.')
    day = birthday [0]
    month = birthday [1]
    birthday = '.'.join (birthday)
else:
    birthday = birthday.split ()
    day = birthday [0]
    month = birthday [1]
    birthday = ' '.join (birthday)
if month.isdigit () == False:
    if 'январ' in month.lower ():
        month = "01"
    elif 'феврал' in month.lower ():
        month = "02"
    elif 'март' in month.lower ():
        month = "03"
    elif 'апрел' in month.lower ():
        month = "04"
    elif 'май' in month.lower () or 'мая' in month.lower ():
        month = "05"
    elif 'июн' in month.lower ():
        month = "06"
    elif 'июл' in month.lower ():
        month = "07"
    elif 'август' in month.lower ():
        month = "08"
    elif 'сентябр' in month.lower ():
        month = "09"
    elif 'октябр' in month.lower ():
        month = "10"
    elif 'ноябр' in month.lower ():
        month = "11"
    elif 'декабр' in month.lower ():
        month = "12"
if day [0] == '0':
    day == day[1]
day = int(day)
sign = ''
if month == '01':
    if day <= 20:
        sign = 'Козерог'
    elif day > 20:
        sign = 'Водолей'
elif month == '02':
    if day <= 18:
        sign = 'Водолей'
    elif day > 18:
        sign = 'Рыбы'
elif month == '03':
    if day <= 20:
        sign = 'Рыбы'
    elif day > 20:
        sign = 'Овен'
elif month == '04':
    if day <= 19:
        sign = 'Овен'
    elif day > 19:
        sign = 'Телец'
elif month == '05':
    if day <= 20:
        sign = 'Телец'
    elif day > 20:
        sign = 'Близнецы'
elif month == '06':
    if day <= 21:
        sign = 'Близнецы'
    elif day > 21:
        sign = 'Рак'
elif month == '07':
    if day <= 22:
        sign = 'Рак'
    elif day > 22:
        sign = 'Лев'
elif month == '08':
    if day <= 22:
        sign = 'Лев'
    elif day > 22:
        sign = 'Дева'
elif month == '09':
    if day <= 22:
        sign = 'Дева'
    elif day > 22:
        sign = 'Весы'
elif month == '10':
    if day <= 23:
        sign = 'Весы'
    elif day > 23:
        sign = 'Скорпион'
elif month == '11':
    if day <= 22:
        sign = 'Скорпион'
    elif day > 22:
        sign = 'Стрелец'
elif month == '12':
    if day <= 21:
        sign = 'Стрелец'
    elif day > 21:
        sign = 'Козерог'
print ('Вы родились', birthday + '.', 'Значит ваш знак зодиака -', sign + '!')
