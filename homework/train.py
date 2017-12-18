import re
text = open('wiki.txt', encoding='utf-8-sig')
text = text.read()
text = re.sub('  ',' ',text)
str = re.sub('\\n\\n',' ',text)
#str1 = 'Я люблю есть. Она любит есть? Он - он любит есть! Она) любит есть.'
sentences = []
punct = ['.','!','?']
punct2 = [';',':','-','"', '(', ')', ',']
tokens = []
dict_tokens = {}
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

str = str.split()

def translit(word):
    new_word = ''
    for j in word:
        if j.lower() in translit_dict:
            new_word += translit_dict[j.lower()]
        else:
            new_word += j.lower()
    return(new_word)


tokens_for_sent = []
index = 1
for i in str:
    if len(i) > 1 and i[-1] not in punct:
            tokens_for_sent.append([index, i, translit(i)])
            index += 1
    elif len(i) > 1 and i[-1] in punct:
            tokens_for_sent.append([index, i[:-1], translit(i[:-1])])
            index += 1
            tokens_for_sent.append([index, i[-1], translit(i[-1])])
            tokens.append([tokens_for_sent])
            tokens_for_sent = []
            index = 1
    else:
        tokens_for_sent.append([index, i[-1], translit(i[-1])])
        index+=1

print(tokens)
#--------------------------------------------------------------Segmenter + tokeniser + translit

for i in tokens[1]:
    print('%s\t' % ('index'),('word'),('translit'), end='')
    print('\n')
    for j in i:
        for k in j:
            print('%s\t' % (k), end='')
        print('\n')

i = 0
for qq in tokens:
    for q in qq:
        if i < 100:
            print(q)
            i += len(q)
        else:
            break

#-------------------------------------------------------------Tokens for POS marking

lez_dict = [[[[1, 'Нептун:', 'neptun:', 'NOUN'], [2, 'Нептун', 'neptun', 'NOUN'], [3, '—', '—', 'PUNCT'], [4, 'Ракъинин', 'rakinin', 'ADJ'], [5, 'системада', 'sistemada', 'NOUN'], [6, 'планета', 'planeta', 'NOUN'], [7, '.', '.', 'PUNCT']],
[[1, 'Ё:', 'jo:', 'NOUN'], [2, 'Ё', 'jo', 'NOUN'], [3, 'А', 'a', 'PRON'], [4, '(кирилл):', '(kirill):', 'NOUN'], [5, 'А,', 'a,', 'PRON'], [6, 'а', 'a', 'PRON'], [7, '—', '—', 'PUNCT'], [8, '"А,', '"a,', 'PRON'], [9, 'а"', 'a"', 'PRON'], [10, 'садлагьай', 'sadlag′ai', 'NUM'], [11, 'гьарф', 'g′arf', 'VERB'], [12, 'лезги', 'lezgi', 'ADJ'], [13, 'алфибдин', 'alfibdin', 'NOUN'], [14, '.', '.', 'PUNCT']],
[[1, 'Ачух', 'achukh', 'ADJ'], [2, 'гьарф', 'g′arf', 'NOUN'], [3, 'я', 'ya', 'NOUN'], [4, '.', '.', 'PUNCT']],
[[1, 'Абажур:', 'abazhur:', 'NOUN'], [2, 'Абажур', 'abazhur', 'NOUN'], [3, '(),', '(),', 'PUNCT'], [4, '()', '()', 'PUNCT'], [5, '-', '-', 'PUNCT'], [6, 'гудай', 'gudai', 'VERB'], [7, 'лампадал', 'lampadal', 'NOUN'], [8, 'акьалжнавай', 'ak′alzhnavai', 'PART'], [9, 'парчадикай', 'parchadikai', 'ADJ'], [10, 'раснавай', 'rasnavai', 'PART'], [11, 'къалпагъ', 'kalpag', 'NOUN'], [12, '.', '.', 'PUNCT']],
[[1, 'Абдул', 'abdul', 'NOUN'], [2, 'Мухътедир', 'mukhtedir', 'NOUN'], [3, 'Айдунбекви:', 'aidunbekvi:', 'NOUN'], [4, 'Биография', 'biografiya', 'NOUN'], [5, '.', '.', 'PUNCT']],
[[1, 'Дагъустан', 'dagustan', 'ADJ'], [2, 'республикадин', 'respublikadin', 'ADJ'], [3, 'Самур', 'samur', 'NOUN'], [4, 'округдин', 'okrugdin', 'NOUN'], [5, 'Ахцегь', 'akhceg′', 'NOUN'], [6, 'хуьре,', 'khu′re,', 'NOUN'], [7, 'кесиб', 'kesib', 'ADJ'], [8, '—', '—', 'PUNCT'], [9, 'лежбердин', 'lezhberdin', 'NOUN'], [10, 'кӀвале', 'kӏvale', 'NOUN'], [11, 'хьана', 'kh′ana', 'VERB'], [12, '.', '.', 'PUNCT']],
[[1, '1898', '1898', 'NUM'], [2, 'йисалай,', 'iisalai,', 'ADV'], [3, 'Бакуда', 'bakuda', 'NOUN'], [4, 'нафтадин', 'naftadin', 'PART'], [5, 'промышленностда', 'promyshlennostda', 'NOUN'], [6, 'кӀвалахзва', 'kӏvalakhzva', 'NOUN'], [7, '.', '.', 'PUNCT']],
[[1, '1904', '1904', 'NUM'], [2, 'йисуз', 'iisuz', 'ADV'], [3, 'Коммунист', 'kommunist', 'ADJ'], [4, 'партиядин', 'partiyadin', 'NOUN'], [5, 'касарикай', 'kasarikai', 'NOUN'], [6, 'сад', 'sad', 'ADV'], [7, 'жезва', 'zhezva', 'NOUN'], [8, '.', '.', 'PUNCT']],
[[1, '«Гуммет»', '«gummet»', 'NOUN'], [2, 'социал', 'social', 'ADJ'], [3, '—', '—', 'PUNCT'], [4, 'демократик', 'demokratik', 'ADJ'], [5, 'кӀеретӀдин,', 'kӏeretӏdin,', 'NOUN'], [6, 'нафтадин', 'naftadin', 'PART'], [7, 'промышленностда', 'promyshlennostda', 'NOUN'], [8, 'кӀвалахзвабрин', 'kӏvalakhzvabrin', 'ADJ'], [9, 'садвалдин', 'sadvaldin', 'NOUN'], [10, 'ва', 'va', 'CONJ'], [11, '1906', '1906', 'NUM'], [12, 'йисуз', 'iisuz', 'ADV'], [13, '—', '—', 'PUNCT'], [14, '«Фаррук»', '«farruk»', 'NOUN'], [15, '—', '—', 'PUNCT'], [16, 'социал', 'social', 'ADJ'], [17, '—', '—', 'PUNCT'], [18, 'демократик', 'demokratik', 'ADJ'], [19, 'кӀретӀдин', 'kӏretӏdin', 'ADJ'], [20, 'актив', 'aktiv', 'NOUN'], [21, 'иштиракчи', 'ishtirakchi', 'NOUN'], [22, 'хьанва', 'kh′anva', 'VERB'], [23, '.', '.', 'PUNCT']],
[[1, 'Пачагьлугъ', 'pachag′lug', 'NOUN'], [2, 'паталай', 'patalai', 'PREP'], [3, 'са', 'sa', 'NUMB'], [4, 'шумуд', 'shumud', 'ADJ'], [5, 'сфер', 'sfer', 'NOUN'], [6, 'жазарих', 'zhazarikh', 'VERB'], [7, 'галукьнвайдия', 'galuk′nvaidiya', 'VERB'], [8, '.', '.', 'PUNCT']]]]

pos = []
for i in lez_dict:
    for k in i:
        for j in k:
            c = j[1].strip('»«:;"')
            pos.append([c, j[3]])

#print(pos)

dict_pos_words = {}
dict_pos = {}

#print(len(pos))

for i in pos:
    if i[1] not in dict_pos_words:
        dict_pos_words[i[1]] = 1
    else:
        j = dict_pos_words[i[1]] + 1
        dict_pos_words[i[1]] = j

for i in pos:
    if (i[0], i[1]) not in dict_pos_words:
        dict_pos_words[(i[0], i[1])] = 1
    else:
        j = dict_pos_words[(i[0], i[1])] + 1
        dict_pos_words[(i[0], i[1])] = j

for i in pos:
    if i[0] not in dict_pos_words:
        dict_pos_words[i[0]] = 1
    else:
        j = dict_pos_words[i[0]] + 1
        dict_pos_words[i[0]] = j


#print(dict_pos_words)

t = []
for i in pos:
    if i[1] not in t:
        t.append(i[1])

#print(t)

tt = []
for i in pos:
    if i not in tt:
        print(i)
        tt.append(i)

#print(tt)

print(('form'),('POS'),('count'),('p'))
for i in t:
    print(('--'), (i), (dict_pos_words[i]), (dict_pos_words[i] / 100))
for i in tt:
   print((i[0]), (i[1]), (dict_pos_words[i[0]]), (dict_pos_words[(i[0], i[1])] / dict_pos_words[i[0]]))


