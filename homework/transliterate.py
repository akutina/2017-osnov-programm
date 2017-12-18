# -*- coding: utf-8 -*-

import re, codecs
text = codecs.open('wiki.txt', 'r', encoding='utf-8')
text = text.read()
text = re.sub('\\n\\n',' ',text)
text = re.sub('\\n',' ',text)
text = re.sub('[0-9]','',text)
text = re.sub('[A-Z][a-z]*','',text)
words = re.split(' ', text)
tokens = []

translit_dict = {'а': 'a',
                'б': 'b',
                'в': 'v',
                'г': 'g',
                'д': 'd',
                'е': 'e',
                'ё': 'jo',
                'ж': 'zh',
                'з': 'z',
                'и': 'i',
                'й': 'i',
                'к': 'k',
                'л': 'l',
                'м': 'm',
                'н': 'n',
                'о': 'o',
                'п': 'p',
                'р': 'r',
                'с': 's',
                'т': 't',
                'у': 'u',
                'ф': 'f',
                'х': 'kh',
                'ц': 'c',
                'ч': 'ch',
                'ш': 'sh',
                'щ': 'shch',
                'ъ': '',
                'ы': 'y',
                'ь': '′',
                'э': 'e',
                'ю': 'ju',
                'я': 'ya'}

for i in words:
    i = i.strip(' *[\.\?!][\'"\)\]]* *"("%')
    i = i.lower().strip(' *[\.,\?!><//\\][\'"\;:)\]]* *"("%')
    if i not in tokens:
        tokens.append(i) #there is a problem with —, “ and » symbols, smth is wrong with encoding, I can't insert them into the strip thing
        #print(i)


for i in tokens:
    print(i, tokens.index(i))