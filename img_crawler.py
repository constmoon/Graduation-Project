import requests
from bs4 import BeautifulSoup
import json

class Crawler:
    def __init__(self):
        self.url = "https://www.google.co.kr/search"
        self.keyword ="q="
        self.searchType = "tbm=isch"
        self.headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"  #clientinfo
        self.session = requests.Session()


    def search(self,keyword_):
        targetUrl = self.url + "?" + self.keyword + keyword_ + "&" + self.searchType
        print(targetUrl)
        response = self.session.get(targetUrl, headers ={"User-agent": self.headers})
        soup = BeautifulSoup(response.text, "html.parser")
        sourpResult = soup.findAll("div", {"class": "rg_meta notranslate"})

        for i in range(300):
            link, type = json.loads(sourpResult[i].text)["ou"], json.loads(sourpResult[i].text)["ity"]
            print(link + " : " + type)
            fileinstance = open("./images/gim/" + str(i)+ "."+ type,'wb')
            img_response = self.session.get(link)

            fileinstance.write(img_response.content)   # content: image, text: text
        print(response.text)

googleCrawler = Crawler()
googleCrawler.search("김치찌개")