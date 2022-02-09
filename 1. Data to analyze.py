import os
import pandas as pd
import csv
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist
import math
from textblob import TextBlob as tb
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer


### 초록 텍스트 클리닝
df = pd.read_csv('raw_data.csv', encoding='cp1252')
df = df.dropna(subset=['Abstract']) #Abstract가 nan인 rows 날리기
df = df.drop_duplicates(subset=['Abstract']) #같은 Abstract인 rows 날리기
df = df.drop_duplicates(subset=['Title']) #같은 Title인 rows 날리기

#아티클만 남기기
df = df[df.Type != 'Book Review']
df = df[df.Type != 'Correction']
df = df[df.Type != 'Editorial Material']
df = df[df.Type != 'Letter']
df = df[df.Type != 'Meeting Abstract']
df = df[df.Type != 'News Item']
df = df[df.Type != 'Review']

#국가정보 추출
Corresponding_Address_Country = [str(a).rpartition(',')[-1][1:-1] for a in df.Corresponding_Address]
temp = []
for w in Corresponding_Address_Country:
    if 'USA' in w:
        w = 'USA'
    temp.append(w)
Corresponding_Address_Country = temp
df.Corresponding_Address = Corresponding_Address_Country

df.to_csv('data_to_analyze.csv')

### 연구영역 별 빈도 계산
WoS_Research_Area = df['WoS Research Area']
list_WoS_Research_Area = []
for w in WoS_Research_Area:
    temp = str(w).split('; ')
    list_WoS_Research_Area.extend(temp)
s=set(list_WoS_Research_Area)
set_WoS_Research_Area = list(s)

fd = FreqDist(list_WoS_Research_Area)
freq_WoS_Research_Area = [[k, fd[k]] for k in fd]
AFinfo = ['Area', 'Freq']
df3 = pd.DataFrame(freq_WoS_Research_Area)
df3.to_csv('freq_WoS_Research_Area.csv', index=False, header=AFinfo)

### 교신저자 소속 국가 별 빈도 계산
WoS_Research_Area = df['Corresponding_Address']
list_WoS_Research_Area = []
for w in WoS_Research_Area:
    temp = str(w).split('; ')
    list_WoS_Research_Area.extend(temp)
s=set(list_WoS_Research_Area)
set_WoS_Research_Area = list(s)

fd = FreqDist(list_WoS_Research_Area)
freq_WoS_Research_Area = [[k, fd[k]] for k in fd]
AFinfo = ['Area', 'Freq']
df3 = pd.DataFrame(freq_WoS_Research_Area)
df3.to_csv('freq_Corresponding_Address.csv', index=False, header=AFinfo)

### 저널 별 빈도 계산
WoS_Research_Area = df['Source']
list_WoS_Research_Area = []
for w in WoS_Research_Area:
    temp = str(w).split('; ')
    list_WoS_Research_Area.extend(temp)
s=set(list_WoS_Research_Area)
set_WoS_Research_Area = list(s)

fd = FreqDist(list_WoS_Research_Area)
freq_WoS_Research_Area = [[k, fd[k]] for k in fd]
AFinfo = ['Area', 'Freq']
df3 = pd.DataFrame(freq_WoS_Research_Area)
df3.to_csv('freq_Journal.csv', index=False, header=AFinfo)

### 키워드 별 빈도 계산
WoS_Research_Area = df['Keywords']
list_WoS_Research_Area = []
for w in WoS_Research_Area:
    temp = str(w).split('; ')
    list_WoS_Research_Area.extend(temp)
s=set(list_WoS_Research_Area)
set_WoS_Research_Area = list(s)

fd = FreqDist(list_WoS_Research_Area)
freq_WoS_Research_Area = [[k, fd[k]] for k in fd]
AFinfo = ['Area', 'Freq']
df3 = pd.DataFrame(freq_WoS_Research_Area)
df3.to_csv('freq_Keyword.csv', index=False, header=AFinfo)

### Author 별 빈도 계산
WoS_Research_Area = df['Authors']
list_WoS_Research_Area = []
for w in WoS_Research_Area:
    temp = str(w).split('; ')
    list_WoS_Research_Area.extend(temp)
s=set(list_WoS_Research_Area)
set_WoS_Research_Area = list(s)

fd = FreqDist(list_WoS_Research_Area)
freq_WoS_Research_Area = [[k, fd[k]] for k in fd]
AFinfo = ['Area', 'Freq']
df3 = pd.DataFrame(freq_WoS_Research_Area)
df3.to_csv('freq_Author.csv', index=False, header=AFinfo)

### Year 별 빈도 계산
WoS_Research_Area = df['Year']
list_WoS_Research_Area = []
for w in WoS_Research_Area:
    temp = str(w).split('; ')
    list_WoS_Research_Area.extend(temp)
s=set(list_WoS_Research_Area)
set_WoS_Research_Area = list(s)

fd = FreqDist(list_WoS_Research_Area)
freq_WoS_Research_Area = [[k, fd[k]] for k in fd]
AFinfo = ['Area', 'Freq']
df3 = pd.DataFrame(freq_WoS_Research_Area)
df3.to_csv('freq_Year.csv', index=False, header=AFinfo)

