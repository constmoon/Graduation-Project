import urllib.request
from  bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class googleImageCrawler():

    CHROMDRIVER_PATH = "/usr/local/bin/chromedriver"
    DATA_PATH = "./images/resha/"
    URL = "https://www.google.com/imghp?hl=en"
    KEYWORD_LIST = "레인보우샤베트"


    def __init__(self):
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        self.keyword_list = googleImageCrawler.KEYWORD_LIST.split(',')
        self.scrollDown_count = 12
        self.image_num = 535
        self.driver.get(googleImageCrawler.URL)
        self.startCrawling()    # start crawling


    def startCrawling(self):
        count = len(self.keyword_list)
        start_time = time.time()
        for _ in range(count):
            try:
                if len(self.keyword_list) != 0:
                    self.searchKeyword()
                    self.scrollDown()
                    images = self.scrapingImage()
                    self.saveImage(images)
                    print("{}% complete ...".format(int((_+1) / count * 100)))
                else:
                    self.driver.quit() # quit all browser. close()는 하나만 종료
                    return
            except:
                print("Error")
                continue


    def searchKeyword(self):
        keyword = self.keyword_list.pop()
        elem = self.driver.find_element_by_id("lst-ib") # 구글 검색 input form의 id
        elem.send_keys(keyword)
        elem.submit()



    def clickMoreButton(self):
        self.driver.find_element_by_id('smb').send_keys(Keys.ENTER)


    def scrollDown(self): # 스크롤 -> 해당 위치에 있는 이미지를 모두 크롤링
        for i in range(0, self.scrollDown_count):
            time.sleep(1.5)
            self.driver.find_element_by_xpath("//body").send_keys(Keys.END)
            if i==2:
                try:
                    time.sleep(1)
                except:
                    self.clickMoreButton()
                    continue


    def scrapingImage(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        params = [] # 이미지 리스트
        imgList = soup.find_all("img", class_="rg_ic rg_i") # image의 class가 rg_ic rg_i

        for img_data in imgList:
            try:
                params.append(img_data["src"])
            except:
                continue

        return params


    def saveImage(self, images):
        for image in images:
            # 파일명 지정
            # request 과정을 통해 이미지 데이터를 가져온다
            urllib.request.urlretrieve(image, googleImageCrawler.DATA_PATH + str(self.image_num) + ".jpg")
            self.image_num += 1


Crawler = googleImageCrawler()
