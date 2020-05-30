import random
import time  

birthday = input ('Когда вы родились?')

date = time.strftime("%d.%m.%Y", time.localtime()) 
print('Сегодняшняя дата:', date)
date = date.split('.') 

thirty_one_d = ['01', '03', '05', '07', '08', '10']
thirty_d = ['04', '06', '09', '11']
year_type = int(date[2]) % 4 

if (date[1] in thirty_d and date[0] == '30') or \
   (date[1] in thirty_one_d and date[0] == '31') or \
   (date[1] == '02' and year_type == 0 and date[0] == '29') or \
   (date[1] == '02' and year_type != 0 and date[0] == '28'):

    next_date = time.strptime('01 ' + str(int(date[1]) + 1) + ' ' + date[2], '%d %m %Y')
    next_date = time.strftime('%d.%m.%Y', next_date)
    print('Гороскоп составлен на следующую дату:', next_date)

elif date[0] == '31' and date[1] == '12':

    next_date = time.strptime('01 01 ' + str(int(date[2]) + 1), '%d %m %Y')
    next_date = time.strftime('%d.%m.%Y', next_date)
    print('Гороскоп составлен на следующую дату:', next_date) 

else:
    
    next_date = time.strptime(str(int(date[0]) + 1) + ' ' + date[1] + ' ' + date[2], '%d %m %Y')
    next_date = time.strftime('%d.%m.%Y', next_date)
    print('Гороскоп составлен на следующую дату:', next_date)

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

random_day = random.choice (['прекрасный', 'ужасный', 'приятный', 'удивительный', 'грустный', 'неприятный'])        
print ('Вы родились', birthday + '.', 'Значит ваш знак зодиака -', sign + '! Звёзды предсказывают, что вас ждёт', random_day, 'день.')

if random_day == 'прекрасный' or random_day == 'приятный' or random_day == 'удивительный':
    
    random_health = random.choice (['наконец осуществить поездку о которой мечтали.','забыть о походе к врачам на ближайший месяц.','почувствовать себя свободным от болей, которые преследовали вас в последние дни.','провести время на открытом воздухе.','поучавтвовать в интересном соревновании.'])
    print ('Здоровье не должно вас подвести, вы сможете', random_health)
    
    random_love = random.choice (['- ваш шанс найти свою вторую половинку или привнести новое в старые отношения.','- идеальная возможность провести романтический вечер с любимым человеком или питомцем!','может начаться необычном образом, например с завтрака в постель.'])
    print ('На любовном фронте дела также обстоят не хуже.', 'Этот день', random_love)

    random_family = random.choice (['останутся такими же тёплыми, как и раньше.', 'станут ещё крепче. Возможно, стоит устроить совместный поход в кино.','никак не повлияют на вас день, вы в праве делать всё, что хотите.'])
    print ('Отношения с семьёй', random_family)

elif random_day == 'ужасный' or random_day == 'грустный' or random_day == 'неприятный':
    
    random_health = random.choice (['Не советуем находится вдалеке от дома, поскольку опасность можт подстерегать на любом шагу.','Не стоит браться за физические упражнения в связи с высокой вероятностью травмы.','Сделайте себе чай и оградите себя от забот, которые вредят вашему состоянию.','Старайтесь оградить себя от выхда на улицу, учитывая высокий риск заболеть.'])
    print ('К ссожалению, здоровье может повести вас в любой момент.', random_health)
    
    random_love = random.choice (['лучше не спорить со своей второй половинкой, так как это может обратиться в огромный скандал.','лучше побыть наедине с собой, а также осуществить планы, связанные лично с вами.','попробуйте поговорить со своим партнёром, возможно его или её что-то висльно беспокоит.'])
    print ('Амур покинул вас.', 'В этот день', random_love)

    random_family = random.choice (['Не выводите своих родственников из себя, иначе ваши отношения могут испортиться навсегда.', 'Дайте своим родственникам немного личного пространства, возможно вы слишком активно вторгаетесь в их личную жизнь.','Попробуйте провести время со своими самыми близкими родственниками, им может не хватать вашего внимания.'])
    print ('Семейные узы также находятся в опасности.', random_family)
    
    

