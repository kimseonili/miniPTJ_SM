import requests
from bs4 import BeautifulSoup
import re
import json

def toStr(num):
    if num < 10:
        return '0'+str(num)
    return str(num)

#####################################################
keyword = '전광훈' #### 검색할 키워드
sMonth = toStr(1) #### 검색 시작 월
eMonth = toStr(2) #### 검색 종료 월
sDay = toStr(1) #### 검색 시작 일
eDay = toStr(1) #### 검색 종료 일
targetIdx = 10 #### 검색할 뉴스 개수. 4000이 최댓값
######################################################

def likeCount(keyword, sMonth, eMonth, sDay, eDay, targetIdx) :


    news = []
    for idx in range(0, targetIdx, 10):
        print(idx // 10, '페이지')
        response = requests.get('https://search.naver.com/search.naver?where=news&query=\"' + keyword + '\"&pd=3&ds=2020.' +
                                sMonth+'.' + sDay + '&de=2020.' + eMonth + '.' + eDay + '&refresh_start=0&pd=3&start='+str(idx))
        soup = BeautifulSoup(response.text, "html.parser")
        newsList = soup.findAll("a", {'class': '_sp_each_url'})
        if len(newsList) == 0:
            break
        for i in newsList:
            if i['href'].startswith('https://news.naver.com/'):
                news.append(i['href'])
                print(i['href'])

    rating = {'like' : 0, 'want' : 0, 'sad' : 0, 'angry' : 0, 'warm': 0}


    for i in news:
        oid = i.split('&')[-2][4:]
        aid = i.split('&')[-1][4:]

        params = (
            ('q', 'NEWS[ne_'+oid+'_' + aid +']|NEWS_SUMMARY'+oid+'_' + aid +']|NEWS_MAIN[ne_'+oid+'_' + aid +']'),
        )

        response = requests.get('https://news-like.naver.com/v1/search/contents',  params=params)
        data =  json.loads(response.text)
        likeData = data['contents'][0]['reactions']
        for j in likeData :
            key = j['reactionType']
            value = j['count']
            if type(value) == type('asd') :
                value = int(value)
            rating[key] += value
    return rating

print(likeCount(keyword, sMonth, eMonth, sDay, eDay, targetIdx))