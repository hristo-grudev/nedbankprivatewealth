import scrapy

from scrapy.loader import ItemLoader
from ..items import NedbankprivatewealthItem
from itemloaders.processors import TakeFirst


class CentralbankSpider(scrapy.Spider):
	name = 'nedbankprivatewealth'
	start_urls = ['https://nedbankprivatewealth.com/insights/']

	def parse(self, response):
		post_links = response.xpath('//div[@class="jet-engine-listing-overlay-wrap"]/div/div/div/section/div/div/div/div/div/section//a')
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h1//text()').get()
		description = response.xpath('/html/body/div[2]/div/div/section[2]/div/div/div[2]/div/div//text()[normalize-space() and not(ancestor::table)]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//div[@class="jet-listing-dynamic-field__content"]/text()').get()

		item = ItemLoader(item=NedbankprivatewealthItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
