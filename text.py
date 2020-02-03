from konlpy.tag import Twitter # 한글 형태소 추출
from collections import Counter # count

from wordcloud import WordCloud # 텍스트 시각화
import matplotlib.pyplot as plt # 시각화 패키지

import nltk # natural language toolkit
from nltk.corpus import stopwords
 
import matplotlib 
from IPython.display import set_matplotlib_formats

import requests # 웹 request 
from bs4 import BeautifulSoup # 웹 크롤링 패키지 

# url에서 source 가져오기
# res = requests.get('http://www.ciokorea.com/t/27240/%EB%8D%B0%EB%B8%8C%EC%98%B5%EC%8A%A4/129646')
res = requests.get('http://www.ciokorea.com/news/33848')
# res = requests.get('http://www.ciokorea.com/column/119945')

# html 객체로 변환
soup = BeautifulSoup(res.content, 'html.parser')

# 기사 본문 가져오기
html = soup.find(class_='node_body')

# 문자열로 변환
text = html.text

# 문자열을 리스트로 나누기
lists = text.split('\n')


twitter = Twitter() 
morphs = [] 
for sentence in lists: 
    morphs.append(twitter.pos(sentence)) 

print(morphs)

# 명사 전처리
noun_adj_adv_list=[] 
for sentence in morphs : 
    for word, tag in sentence : 
        if tag in ['Alpha'] and ("또" not in word)and ("등" not in word)and ("앞" not in word)and ("생" not in word)and ("를" not in word)and ("여기" not in word)and ("다른" not in word)and ("예" not in word)and ("은" not in word)and ("위해" not in word)and ("다음" not in word)and ("대한" not in word)and ("아주" not in word)and ("그" not in word)and ("도움" not in word)and ("약" not in word)and ("때문" not in word)and ("여러" not in word) and ("더" not in word) and ("이" not in word) and ("의" not in word) and ("및" not in word) and ("것" not in word) and ("내" not in word)and ("나" not in word)and ("수"not in word) and("게"not in word)and("말"not in word) : 
            noun_adj_adv_list.append(word) 
        if tag in ['Noun'] and ("또" not in word)and ("등" not in word)and ("앞" not in word)and ("생" not in word)and ("를" not in word)and ("여기" not in word)and ("다른" not in word)and ("예" not in word)and ("은" not in word)and ("위해" not in word)and ("다음" not in word)and ("대한" not in word)and ("아주" not in word)and ("그" not in word)and ("도움" not in word)and ("약" not in word)and ("때문" not in word)and ("여러" not in word) and ("더" not in word) and ("이" not in word) and ("의" not in word) and ("및" not in word) and ("것" not in word) and ("내" not in word)and ("나" not in word)and ("수"not in word) and("게"not in word)and("말"not in word) : 
            noun_adj_adv_list.append(word) 
print(noun_adj_adv_list)

# 글자 수 세기
count = Counter(noun_adj_adv_list)
words = dict(count.most_common())
print(words)

#word cloud show
matplotlib.rc('font',family = 'Malgun Gothic') 
set_matplotlib_formats('retina') 
matplotlib.rc('axes',unicode_minus = False)

wordcloud = WordCloud(font_path = './Arial.ttf', background_color='white',colormap = "Accent_r", width=1500, height=1000).generate_from_frequencies(words) 
plt.imshow(wordcloud) 
plt.axis('off') 
plt.show()








