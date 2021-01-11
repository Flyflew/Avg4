import requests
from bs4 import BeautifulSoup
import googletrans
from opencc import OpenCC
cc = OpenCC('s2t')

pNoIntStart = 71252
pNoIntEnd = 71176
pName = "我是大變"

for i in range(pNoIntEnd, pNoIntStart+1):
    pNo = str(i)
    translator = googletrans.Translator()

    r = requests.get("http://www.dushu369.com/shici/HTML/" + pNo + ".html")
    r.encoding = 'gb2312'

    soup = BeautifulSoup(r.text, "html.parser")  # 將網頁資料以html.parser

    poem = soup.select("td.cntitle")
    for s in poem:
        pName = cc.convert(s.text)
        print(pName+" ◎徐志摩")

    poem = soup.select("td.content")
    for s in poem:
        fo = open('◎徐志摩 '+pName+'.txt', 'w', encoding='utf-8')
        fo.write(cc.convert(s.text))
        print("done")
        fo.close()
