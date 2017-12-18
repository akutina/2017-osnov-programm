# -*- coding: utf-8 -*-

import re, codecs
text = codecs.open('wiki.txt', 'r', encoding='utf-8')
text = text.read()
text = re.sub('\\n\\n',' ',text)
text = re.sub('  ',' ',text)
sentences = re.split(' *[\.\?!][\'"\)\]]* *', text)
#for i in sentences:
 #   print (i)
  #  print('end')