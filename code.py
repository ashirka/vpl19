text = input('Please set the path to the file: ')
text2 = open(text, encoding='utf-8').read()
text3 = text2.split('')
print(text3)
word = input('Please type any word: ')

