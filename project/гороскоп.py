data_rog= input('Здравствуйте! Чтобы узнать гороскоп на завтра введите дату рождения: ')
month1 = ['', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля','августа','сентября','октября','ноября', 'декабря']
if '.' in data_rog:
    data_rog = data_rog.split('.')
    day = int(data_rog [0])
    month = int(data_rog [1])
elif '/' in data_rog:
    data_rog = data_rog.split('/')
    day = int(data_rog [0])
    month = int(data_rog [1])
elif ' ' in data_rog:
    data_rog = data_rog.split(' ')
    day = int(data_rog [0])
    month = data_rog [1]
    for x in month1:
        if month==x:
            month = month1.index (x)
    month = int(month)
znak = ['','Козерог','Водолей','Рыбы','Овен','Телец','Близнецы','Рак','Лев','Дева','Весы','Скорпион','Стрелец']
if ((day>=22)and(month>=1)and(month<12)):
    zodiak =znak[month+1]
elif ((day<22)and(month == 1)or (month==12)and (day>=22)):
    zodiak=znak[1]
else:
    zodiak =znak[month]
print (zodiak)
import time, random
date = int(time.strftime('%d',time.localtime()))
month = int(time.strftime('%m',time.localtime()))
year = int(time.strftime('%Y',time.localtime()))
month31 = [1,3,5,7,8, 10, 12]
months = ['января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря']
#хочу из файла
box_horo = open('horo.txt', encoding='utf-8').read()
box_horo = box_horo[1:]
box_horo = box_horo.split('\n')
l = len(box_horo)
if date <= 27:
    date += 1
elif date < 31 and month in month31:
    date += 1
elif date == 31 and month in month31 and month != 12:
    date = 1
    month += 1
elif date == 31 and month in month31 and month == 12:
    date = 1
    month = 1
    year += 1
elif date < 30 and month not in month31 and month != 2:
    date += 1      
elif date == 30 and month not in month31:
    date = 1
    month += 1
elif date == 29 and month == 2:
    date = 1
    month += 1
elif date == 28 and month == 2:
    if year % 4 == 0:
        date +=1
    else:
        date = 1
        month += 1
horoscope = box_horo[random.randint(0,l-1)]
print('Гороскоп на', date, months[month-1], year, 'года.', horoscope)
