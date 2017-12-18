# -*- coding: utf-8 -*-

arr = ['Я', 'люблю', 'есть', 'люблю', 'любить', 'lюблю']
new_dict = []
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

tokens = []

for i in arr:
    if i not in tokens:
        tokens.append(i)

#for i in tokens:
 #   print(i)
  #  print(tokens.index(i))

for i in tokens:
    new_word = ''
    for j in i:
        #print(j)a
        if j.lower() in translit_dict:
            new_word += translit_dict[j.lower()]
        else:
            new_word += j.lower()
    print(new_word)
    new_dict.append(new_word)

for i in new_dict:
    print(i)

#if 'а' in translit_dict:
 #   print(translit_dict['а'])
