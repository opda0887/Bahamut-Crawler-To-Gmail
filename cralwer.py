    # 進入cmd先打上：pip install fake-useragent (之後的headers會用上)
import dictionary
# 取得目標 url
    # 發起請求使用urllib庫的request請求模塊與 parse 模塊
from urllib import request
url = 'https://forum.gamer.com.tw/B.php?bsn={}'
title = input('你想要查詢什麼(先在dictionary上找到你想要的版，然後複製版的名字並貼上)：')
    # quote()對字符串進行編碼
target = dictionary.categorys.get(title)
if (target != None):
    
    final_url = url.format(target)

    # 假裝成使用者
    from fake_useragent import UserAgent
    ua = UserAgent().edge

    # 重新建構url資訊
    req = request.Request(final_url, headers={"User-Agent": ua})

    # 處理目標url
        # urlopen()向URL發送請求，返回響應對象
    response = request.urlopen(req)
        # 提取響應內容
            # decode('utf-8'): 字節碼轉換為字串
    html = response.read().decode('utf-8')

    # ----- 正式開始 -----
    import bs4
    root = bs4.BeautifulSoup(html, "html.parser")
    titles = root.find_all("div", class_="b-list__tile")
    for i in titles:
        if(i.p != None):
            print(i.p.text)
    print(final_url)

else:
    print("你所輸入的版名目前沒有收納喔~敬請期待日後更新")