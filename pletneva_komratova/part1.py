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
