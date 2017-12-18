import sys

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

for c in sys.stdin.readlines():
    for i in c.split(' '):
        trans_word = ''
        for k in i.lower():
            if k in translit_dict:
                trans_word+=translit_dict[k]
            else:
                trans_word += k
        tokens.append([i, trans_word])

for i in tokens:
    print(i, tokens.index(i))
