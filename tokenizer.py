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
print(len(words))

for i in words:
    i = i.strip(' *[\.\?!][\'"\)\]]* *"("%')
    i = i.lower().strip(' *[\.,\?!><//\\][\'"\;:)\]]* *"("%')
    if i not in tokens:
        tokens.append(i) #there is a problem with —, “ and » symbols, smth is wrong with encoding, I can't insert them into the strip thing
        #print(i)


for i in tokens:
    print(i, tokens.index(i))

