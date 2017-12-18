# -*- coding: utf-8 -*-
import re
a = ['иду','идет','шла','шел']
b = ['смеется','смеялась','смеюсь','смеялся', 'курила']
c = 'Она шла, смеялась. Она шла смеялась ха. Она шла, звонила по телефону, кричала.'
punct = ['.','!','?']

c = c.split()
sentence = []
text = []

for i in c:
    if i[-1] in punct:
        sentence.append(i[:-1])
        sentence.append(i[-1])
        text.append(sentence)
        sentence = []
    else:
        sentence.append(i)

print(text)

new_text = []

for i in text:
    sent = []
    for j in range(len(i)-1):
        if i[j].strip(',') in a and i[j+1] in b:
            if len(i[j]) > len(i[j].strip(',')):
                kkk = i[j]
                i.insert(i.index(i[j]), i[j][:-1])
                i.remove(i[j+1])
                break


print(text)

#_________________________________________________________working on the array^


def serial_const(sent):
    print(sent)
    sent = sent.split()
    for j in range(len(sent) - 1):
            if sent[j].strip(',') in a and sent[j + 1] in b:
                if len(sent[j]) > len(sent[j].strip(',')):
                    kkk = sent[j]
                    sent.insert(sent.index(sent[j]), sent[j][:-1])
                    sent.remove(sent[j + 1])
                    return sent

serial_const('Я давно шла, курила')


#_________________________________________________________function for one sentence^

a = open('first_verbs.txt', encoding='utf-8-sig')
a = a.read()
a = re.sub('\\n',' ',a)
a = re.split(', ', a)

b = open('second_verbs.txt', encoding='utf-8-sig')
b = b.read()
b = re.sub('\\n',' ',b)
b = re.split(', ', b)

c = open('turgenev.txt', encoding='utf-8-sig')
c = c.read()
c = c.split()
punct = ['.','!','?']

sentence = []
text = []

for i in c:
    if i[-1] in punct:
        sentence.append(i[:-1])
        sentence.append(i[-1])
        text.append(sentence)
        sentence = []
    else:
        sentence.append(i)

#print(text)

kkk = ''
for i in text:
    for j in range(len(i)-1):
        if i[j].strip(',').lower() in a and i[j+1] in b:
            #print('yes')
            if len(i[j]) > len(i[j].strip(',')):
                i.insert(i.index(i[j]), i[j][:-1])
                i.remove(i[j+1])
                print(('serial construction: '), (i))
                break

#print(text)

#________________________________________________________working with dictionaries and text as a corpus ^