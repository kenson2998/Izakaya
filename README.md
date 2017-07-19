[爬取練習]居酒屋清單
===

### 爬取對象：

[愛評網](http://www.ipeen.com.tw/search/taipei/000/1-0-2-15/)

![](https://i.imgur.com/6o0Fti8.jpg)


### 環境：

```
python3.6
selenium 2.53.2
pillow
pytesseract 
```


### 初步實現：
因網頁中的電話號碼是圖片格式的關係，無法直接取得文字，所以使用selenium獲取圖片在用OCR進行解析，在速度上不是很有效率，還有很多地方需要完善。

![](https://i.imgur.com/PwUoTL6.png)
