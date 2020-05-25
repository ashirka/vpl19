import time
date = input ('Когда вы родились?')#не знаю, может прописать тип "Число и месяц когда вы родились", так как год нам не важен
if '.' in date:
    date = date.split ('.')
else:
    date = date.split ()
if date[1].isdigit () == False:
    if 'январ' in date[1].lower ():
        date [1] = "01"
    elif 'феврал' in date[1].lower ():
        date [1] = "02"
    elif 'март' in date[1].lower ():
        date [1] = "03"
    elif 'апрел' in date[1].lower ():
        date [1] = "04"
    elif 'май' in date[1].lower or 'мая' in date[1].lower ():
        date [1] = "05"
    elif 'июн' in date[1].lower ():
        date [1] = "06"
    elif 'июл' in date[1].lower ():
        date [1] = "07"
    elif 'август' in date[1].lower ():
        date [1] = "08"
    elif 'сентябр' in date[1].lower ():
        date [1] = "09"
    elif 'октябр' in date[1].lower ():
        date [1] = "10"
    elif 'ноябр' in date[1].lower ():
        date [1] = "11"
    elif 'декабр' in date[1].lower ():
        date [1] = "12"
        """
        
aries = 
taurus =
gemini =
cancer =
leo =
virgo =
libra =
scorpio =
sagittarius =
capricorn =
aquarius =
pisces = 
"""
