# Tutorial(使用教學)📝  

### 🌳環境設定(Env Setting)  
**如果可以，使用 VS Code，以方便跟著我接下來的步驟**  
在 cmd 中打上：  
```pip install Scrapy```  
```pip install BeautifulSoup4```  
```pip install twisted```  

### 👀**成果預覽畫面(Preview)**：  
![img](https://i.imgur.com/mdxCfEh.png)

## 👌**使用說明(Features)**:  
1. 找到：Bahamut-Crawler-To-Gmail-main -> Baha -> spiders -> **clawer** 並打開找到"***categorys***"  
![img](https://i.imgur.com/slBZIrk.png)
在這裡可以挑選日後要在巴哈上取得的資料  

2. 在**clawer**檔案中中找到"***titles***"，並依自己需求替換成"***categorys***"中你喜歡的板的名稱**(全名)**  
![img](https://i.imgur.com/h7PS3Bm.png)
我拿：場外休息區 作範例("***categorys***"中的第一個)  

3. 找到 # send email 那行，我們要設定誰要接收到巴哈的資料  
![img](https://i.imgur.com/xul7CL0.png)
email_sender = '\<sender>\' 中的 **\<sender\>** 替換成**發送mail的帳號**( ‼一定要是gmail，否則後續會出錯)  
email_password = '\<password>\' ：第4步會詳細解釋該替換成甚麼  
email_receiver = '\<receiver>\' 中的 **\<receiver\>** 替換成**接收mail的帳號**(任何mail帳號都可、也可和 **email_sender** 一樣)  

4. 設定password  
先到 https://myaccount.google.com/ 中，點選左方欄位的**安全性**  
![img](https://i.imgur.com/2vFeCvf.png)
往下滑並找到 **登入 Google** 欄位中的 **兩步驟驗證**，並完成設定  
接著，到 https://myaccount.google.com/apppasswords 中，找到名為**選取應用程式**並點選其中的**其他(自訂名稱)**  
![img](https://i.imgur.com/IeY4v1x.png)
名稱隨意取，之後按下**產生**就來到以下畫面  
![img](https://i.imgur.com/YEBMbLD.png)
右上角黃色格子內的是你的**email_password**，將他複製並將 email_password = '\<password>\' 中的 **\<password\>** 改成你**複製的代碼**即可  

5. 在 Bahamut-Crawler-To-Gmail-main -> Baha -> rutineRun 中打開**rutineRun**，你會看到程式碼中有一變數**timeSet**  
![img](https://i.imgur.com/ZXqh9qy.png)
你可以改成你要的數字，取決於你想**間格多少秒接收到一次新的data**

6. 在**rutineRun**中，於terminal中執行以下指令：  
```python routineRun.py```  
![img](https://i.imgur.com/toMXxSi.png)
之後去看你設定接收mail的那隻帳號，就會發現到你所設定版面的全新資訊瞜❤️  


If you have any feedbacks, just contact me (≧∀≦)
