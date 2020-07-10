import scrapy

class NaverNewsSpider(scrapy.Spider):
    name = "navernews"
    start_urls = [
        'https://news.naver.com/main/home.nhn'
    ]

    def parse(self, response):
        headline = response.css("div#main_content div.main_component")[0]
        titles = headline.css("ul.hdline_article_list div.hdline_article_tit a.lnk_hdline_article::text").getall()
        for title in titles:
            yield {
                'title': title.strip()
            }