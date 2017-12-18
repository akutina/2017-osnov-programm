import sys

punct = ['-','"',':',';']
tokens = []

for c in sys.stdin.readlines(): #I read every line (sentence) in the text
    sent = [] #here is my array for each sentence
    index = 1 #here is index which is 1 at the first step
    if c != '\n': #if the sentence is not empty
        for i in c.split(' '): #for each word in sentence
            if i[-1] not in punct: #if its last symbol is not in punct
                sent.append([index, i]) # I append i with its index to sent and change index for the next token
                index+=1
            if i[-1] in punct: #else
                sent.append([index, i[:-1]]) #append the word with its index
                index+=1
                sent.append([index, i[-1]]) #append the punct with its index
                index+=1
    tokens.append(sent) #here I append the [sent] array to [tokens] array to have structure like
    #[[1, 'blabla'],[2, '-'],[3...]...]] etc.

for i in tokens: #here I print sentences with devided tokens
    print(i)

for i in tokens: #here I print all the tokens separately
    for j in i:
        print(j)

