import requests
from bs4 import BeautifulSoup
import csv

f = open('naverSearchedKeyword.csv','w',newline='')
wr = csv.writer(f)



headers = {
    'authority': 'datalab.naver.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://datalab.naver.com/keyword/realtimeList.naver?age=40s&datetime=2020-03-02T15%3A18%3A00&groupingLevel=0&news=2',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NRTK=ag#20s_gr#0_ma#-2_si#-2_en#-2_sp#-2; NID_AUT=uCu9XVwzszVbbRRyqhJfBcaf6ZmkaWn8c8j3HTnh5evGiJeQuCCd4KP4WOk8vJ0R; NID_JKL=Bx5L3SR5iqL0LSsQQELWuoLp6kVPZSrh42Uq2L054cM=; ASID=3a78904e00000173065ae2720000004a; MM_NEW=1; NFS=2; MM_NOW_COACH=1; NNB=2WB2COMNMUKV6; _ga_4BKHBFKFK0=GS1.1.1597672842.2.1.1597672844.58; nx_ssl=2; _ga=GA1.2.406437722.1593356627; _datalab_cid=50000008; NID_SES=AAABjReiEwnUNw/omP/80Vb0BQtd1UnnQ0wYY27jfUNu8+ind8DS81HOnOwUEfTE+N+3sOvef3dBWE736TQ+eBIc9k7mxy4GY9jXNezd5ZWkSd4MRCEo8H8Ei6sk4LKBSWnwd452v22zwGWJlC+amR3qwIkXlvesPPYBipfiG4EC+XE144Yr2sgUDHnrUT5HFxsblKaapFYccegkrt7HMqz1TkplZ2POuhj2uec52Wtw9Psf2Yt0GLLMMCfdEPQBC5n3Yb7gWv308fMTgb57+hQZKlDDio8xtMFIt6MtSmfy0/L2G1V8OQ+D+s9J3rBm/YdRyVEBjnRzliFyudHfq75BSkIexw5yDjVkgewUsSyC5pjPjq3BG+Gi3e5Y2hddJzTtOC2hc1K6kgzUatm1RuUr3ZcGmq9zZWAaAo7l8M34O3jvU/6tFTJhktXIQFWAgwM0aZH09NPMCfscEKsHAtaYBIizREm0LRGdIfwF4JikwacG1d0lsQ4z15UOUd4EAFvgjzx1C3mroNVi+pxcdsjpJrA=; page_uid=U03lmlprvxsss514Us0ssssssvl-014433; BMR=s=1598939291004&r=https%3A%2F%2Fm.blog.naver.com%2Fqfree6818%2F221304043254&r2=https%3A%2F%2Fwww.google.com%2F',
}
day = [30] # 크롤링 종료 일
sday = [1] # 크롤링 시작 일
for m in range(1,6) :
    monthStr = '0' + str(m)
    for d in range(1, day[0] + 1) :
        dayStr = str(d)
        if len(dayStr) == 1 :
            dayStr = '0' + dayStr
        keyword = []

        print(m, "월", d, "일")
        for i in range(24) :
            hourStr = str(i)
            if len(hourStr) == 1 :
                hourStr = '0' + hourStr
            for j in range(0, 60, 10) :
                minStr = str(j)
                if len(minStr) == 1 :
                    minStr = '0' + minStr
                params = (
                    ('age', 'all'),
                    ('datetime', '2020-'+monthStr+'-'+dayStr+'T'+ hourStr + ':' + minStr + ':00'),
                    ('groupingLevel', '0'),
                    ('news', '2'),
                )

                
                response = requests.get('https://datalab.naver.com/keyword/realtimeList.naver', headers=headers, params=params)
                soup = BeautifulSoup(response.text, "html.parser")
                result = soup.select('span.item_title')
                for i in result : 
                    keyword.append(i.text)
        wr.writerow([monthStr, dayStr , keyword])
f.close()
