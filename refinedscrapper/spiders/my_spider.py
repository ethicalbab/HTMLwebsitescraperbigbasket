import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from time import sleep, time  

class BigBasketSpider(scrapy.Spider):
    name = "bigbasket"
    start_urls = [
        'https://www.bigbasket.com/cl/fruits-vegetables/?nc=nb&page=2',
    ]

    def __init__(self):
        self.driver = webdriver.Chrome()  

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        print("Automatically scrolling for 60 seconds to load images...")
        self.driver.get(response.url)
        sleep(5)  

        end_time = time() + 1680  
        while time() < end_time:
            self.scroll_down()
            sleep(4.0)  

        category = response.url.split('/')[4].replace('-', ' ')
        sel = Selector(text=self.driver.page_source)

        items = sel.css('div.SKUDeck___StyledDiv-sc-1e5d9gk-0.eA-dmzP')

        for item in items:
            brand = item.css('h3 a span::text').get()
            product_name = item.css('h3 a div h3::text').get()
            discounted_price = item.css('div.Pricing___StyledDiv-sc-pldi2d-0.bUnUzR span.Label-sc-15v1nk5-0.Pricing___StyledLabel-sc-pldi2d-1.gJxZPQ.AypOi::text').get()
            original_price = item.css('div.Pricing___StyledDiv-sc-pldi2d-0.bUnUzR span.Label-sc-15v1nk5-0.Pricing___StyledLabel2-sc-pldi2d-2.gJxZPQ.hsCgvu::text').get()
            image_url = item.css('img::attr(src)').get()

            yield {
                'category': category,
                'brand': brand,
                'product_name': product_name,
                'discounted_price': discounted_price,
                'original_price': original_price,
                'image_url': image_url,
            }

        next_page = sel.css('li.next a::attr(href)').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 800);") 

    def closed(self, reason):
        self.driver.quit() 
