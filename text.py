from konlpy.tag import Twitter 
from collections import Counter

file = open("./input.txt", 'r') 
lists = file.readlines() 
file.close()


twitter = Twitter() 
morphs = [] 
for sentence in lists: 
    morphs.append(twitter.pos(sentence)) 
    
print(morphs)

noun_adj_adv_list=[] 
for sentence in morphs : 
    for word, tag in sentence : 
        if tag in ['Noun'] and ("것" not in word) and ("내" not in word)and ("나" not in word)and ("수"not in word) and("게"not in word)and("말"not in word): 
            noun_adj_adv_list.append(word) 
    
print(noun_adj_adv_list)

count = Counter(noun_adj_adv_list)
words = dict(count.most_common())
print(words)




