import re
from collections import Counter

file = input('Please set the path to the file: ')
text = open(file, encoding='utf-8').read().lower()
text1 = re.findall(r'\w+', text)
word = input('Please type any word: ')
before = []
after = []
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
