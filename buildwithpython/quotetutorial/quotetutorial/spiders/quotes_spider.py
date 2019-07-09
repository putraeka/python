import scrapy

class quoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    
    def parse(self, response):
        # title_home = response.css('title::text').extract()
        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:
            title = quotes.css("span.text::text").extract()
            author = quotes.css(".author::text").extract()
            tags = quotes.css(".tag::text").extract()
            yield {
                'title': title,
                'author': author,
                'tags': tags
                }