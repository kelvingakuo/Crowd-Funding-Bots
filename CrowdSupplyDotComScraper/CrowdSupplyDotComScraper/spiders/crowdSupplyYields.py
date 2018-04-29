import scrapy
from scrapy import Request

class CrowdSupplyYields(scrapy.Spider):
	name = 'crowdsupplyyields'

	start_urls = [
		'https://www.crowdsupply.com/archive',
		'https://www.crowdsupply.com/crowdfunding',
		'https://www.crowdsupply.com/available'
	]

	def parse(self,response):
		allProjects = response.css('a.project-tile')
		baseUrl = 'https://www.crowdsupply.com'

		for project in allProjects:
			origi = project.css('a::attr(href)').extract_first() 
			destination = baseUrl+origi

			item = dict()
			item['projectLink'] = destination
			item['source'] = baseUrl

			request = scrapy.Request(url=destination, callback = self.parseProfile)
			request.meta['item'] = item

			yield request

		nextPage = response.css('li.next a::attr(href)').extract_first()
		if nextPage is not None:
			yield response.follow(nextPage, self.parse)


	def parseProfile(self, response):
		fullname = response.css('div#creator div.project-owner h4::text').extract_first()
		if fullname is not None:
			firstName = fullname.split( )[0]
			lastName = fullname.split( )[1]
		else:
			firstName = " "
			lastName = " "

		item = response.meta['item']
		item['website'] = response.css('div#creator p.creator-block-metadata a::attr(href)').extract_first()
		item['First Name'] = firstName
		item['Last Name'] = lastName

		yield item
		





