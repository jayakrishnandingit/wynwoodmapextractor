import scrapy
from wynwoodmapextractor.items import ArtistItem


class WynWoodMapSpider(scrapy.Spider):
    name = 'wynwoodmap'
    start_urls = ['http://wynwoodmap.com/']

    def parse(self, response):
        options = response.xpath('//select/option')
        for index, option in enumerate(options):
            each_artist_item = ArtistItem()
            each_artist_item['name'] = option.xpath('text()').extract().pop()
            each_artist_item.save()
            yield each_artist_item
