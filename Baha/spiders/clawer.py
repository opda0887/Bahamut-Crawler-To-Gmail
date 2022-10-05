import scrapy
import sys  # 關閉程式用的

    # 資料聚集處
categorys = {
    "場外休憩區": 60076,
    "RO仙境傳說：愛如初見（Ragnarok ORIGIN）": 37657,
    "神魔之塔": 23805,
    "原神": 36730,
    "英雄聯盟 League of Legends": 17532,
    "幻塔": 71040,
    "新楓之谷": 7650,
    "怪物彈珠": 25052,
    "電腦應用綜合討論": 60030,
    "電馭叛客(Cyberpunk) 2077": 23379,
    "鋼彈": 109,
}

url = 'https://forum.gamer.com.tw/B.php?bsn={}'
title = input('你想要查詢什麼(先在dictionary上找到你想要的版，然後複製版的名字並貼上)：')
print("-------------------------")
    # 在 categorys 中尋找編號
target = categorys.get(title)
if (target != None):
    # url 合併
    final_url = url.format(target)
else:
    sys.exit("你所輸入的版名目前沒有收納喔~敬請期待日後更新")

# 開啟/創建 test.text 文件夾
file = open("test.txt", mode="w", encoding="utf-8")

import bs4

class BahaCrawler(scrapy.Spider):
    # 創建三樣物件：
    # 1. 要運行時呼喚的name
    # 2. 設定要爬取的url
    # 3. 運行
    name = 'Baha'
    start_urls = [final_url]
    def parse(self, response):
        root = bs4.BeautifulSoup(response.body)
        titles = root.find_all("div", class_="b-list__tile")
        for i in titles:
            if(i.p != None):
                print(i.p.text)
                file.write(i.p.text)
                file.write("\n")
        file.close()    


# 執行：scrapy crawl <name> (ex: Baha)