import ssl
from tkinter.tix import Form
from venv import create
import scrapy
import sys  # 關閉程式用的
from email.message import EmailMessage
import ssl
import smtplib

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
    "One Punch Man：英雄之路": 75542,
    "17守望傳說 Guardian Tales": 38113,
    "天堂 W": 71905,
    "Steam 綜合討論板": 60599,
    "APEX 英雄": 36072,
    "流亡黯道 Path of Exile": 18966,
    "三國志幻想大陸": 73165,
    "斯普拉遁（漆彈大作戰） 系列": 26487,
    "貓咪大戰爭（にゃんこ大戦争": 23772,
    "彈射世界": 37689,
    "Fate/Grand Order": 26742,
    "明日方舟": 33651,
    "第七史詩": 34880,
    "暗黑破壞神": 742,
    "NS / Nintendo Switch": 31587,
    "傳說對決 Arena of Valor": 30518,
    "鬥陣特攻": 27362,
    "PS5 / PlayStation5": 60645,
    # 33
}

url = 'https://forum.gamer.com.tw/B.php?bsn={}'

title = "場外休憩區"

print("-------------------------")
    # 在 categorys 中尋找編號
target = categorys.get(title)
if (target != None):
    # url 合併
    final_url = url.format(target)
else:
    sys.exit("你所輸入的版名目前沒有收納喔~敬請期待日後更新")

# 開啟/創建 test.text 文件夾

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
        file = open("test.txt", mode="w", encoding="utf-8")
        content = ''
        for i in titles:
            if(i.p != None):
                content += f"{i.p.text}\n"
                print(i.p.text)
                file.write(i.p.text)
                file.write("\n")
        content += f"{final_url}"
        file.write(final_url)
        file.close()

        # send email
        email_sender = '<sender>'
        email_password = '<yourpassword>'
        email_receiver = '<receiver>'
        subject = '巴哈爬蟲結果'
        body = content
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())


    
# 執行：scrapy crawl <name> (ex: Baha)

# you have to run the reactor yourself