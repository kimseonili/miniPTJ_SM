import pandas as pd
import numpy as np
import csv
import re

data = pd.read_csv('/Users/babywalnut/Desktop/Gwangju_Project/naverSearchedKeyword16.csv', encoding='cp949', header=None)
df = pd.DataFrame(data)

df.columns=['month','date','keywords']

p = re.compile(r'[\[\]]')
df['keywords']= [p.sub('', x) for x in df['keywords'].tolist()]
# start_month, start_date = map(int, input('start : ').split())
# end_month, end_date = map(int, input('end : ').split())

# condition_1 = (df['month'] == start_month) & (df['date'] == start_date)
# condition_2 = (df['month'] == end_month) & (df['date']== end_date)
# start_df = df[condition_1]
# end_df = df[condition_2]

splited_keywords=[]

for i in df['keywords']:
    splited_keywords.append(list(i.split(', ')))

count_list=[]
for i in splited_keywords:
    count_list = Counter(i)
    count_dict = dict(count_list)
    # mask = np.array(Image.open('/Users/babywalnut/Downloads/코로나바이러스.jpg'))
    my_wc = WordCloud(font_path="/Users/babywalnut/Library/Fonts/NanumSquareRoundEB.ttf",background_color='white')
    plt.imshow(my_wc.generate_from_frequencies(count_list))
    plt.axis('off')
    plt.show()
