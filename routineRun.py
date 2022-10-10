# 使用twisted 來實現 daily routine 的目標
from twisted.internet import reactor, task
from scrapy.crawler import CrawlerRunner
# 找到clawer.py 中的 BahaCrawler() 來使用
from Baha.spiders.clawer import BahaCrawler

# 可自由調整時間
timeSet = 60

def runCrawl():

    CrawlerRunner().crawl(BahaCrawler) # == 在cmd輸入：scrapy crawl Baha (BahaCrawler 中的 name 變數)


#　LoopingCall(...) : call function reaptedly
loop = task.LoopingCall(runCrawl)
# start(...) : 間隔多久(seconds)
loop.start(timeSet)

reactor.run()