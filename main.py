#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from PIL import Image
import pytesseract
from IzakayaSQLHelper import IzakayaSQLhelper


class crawlIzakaya:
    def __init__(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)
        self.browser.get("http://www.ipeen.com.tw/search/taipei/000/1-0-2-15/")

    def Go(self,url):
        self.browser.get(url)

    def TotlePageNUM(self):
        elem = self.browser.find_element_by_xpath(".//*[@data-label='最尾頁']")

        # get the attribute value
        link = elem.get_attribute('href')
        url, page = link.split("=")
        return int(page)

    def ScreenToOcr(self, imgID, background):
        # screenshot
        # valiCode
        self.browser.save_screenshot('sc.png')
        imgelement = imgID
        location = imgelement.location
        size = imgelement.size
        rangle = (int(location['x']),
                  int(location['y']),
                  int(location['x'] + size['width']),
                  int(location['y'] + size['height']+2)
                  )

        i = Image.open("sc.png")
        Lim = i.crop(rangle)
        # Lim = Lim.convert('L')
        Lim = Lim.resize((84*4, 14*4), Image.ANTIALIAS)
        Lim.save('lim.png')
        txt = pytesseract.image_to_string(Lim).replace(" ","")
        return txt

    def main(self):
        # 項目
        items = self.browser.find_elements_by_xpath(".//*[@class='serItem']")
        # print items
        t = len(items)
        # 店家名稱 //h3//*
        # 地址 //*[@class='basic']//span
        # 電話 //*[@class='basic']//img

        for x in range(t):

            titles = items[x].find_elements_by_xpath(".//h3/*")
            tlist = []
            for spen in range(len(titles)):
                tlist.append(titles[spen].text)
            title = " ".join(tlist)

            try:
                address = items[x].find_element_by_xpath(".//*[@class='basic']//span").text
            except:
                address = "地址已換"

            try:
                phoneobj = items[x].find_element_by_xpath(".//*[@class='basic']//img")
                phone = self.ScreenToOcr(imgID=phoneobj, background="note")
            except:
                phone = u"暫無資料"

            print(title, phone, address)
            # if IzakayaSQLHelper().select(title) == None:
            #     IzakayaSQLHelper().insert(title,phone,address)
            # else:
            #     print (u"%s已存在" % title)

if __name__ == '__main__':

    crawlIzakaya = crawlIzakaya()

    pages = crawlIzakaya.TotlePageNUM()

    for page in range(1,pages+1):
        print("頁數:", page)
        if page == 1:
            pass
        else:
            crawlIzakaya.Go("http://www.ipeen.com.tw/search/taipei/000/1-0-2-15/?p=%s" % str(page))
        crawlIzakaya.main()
