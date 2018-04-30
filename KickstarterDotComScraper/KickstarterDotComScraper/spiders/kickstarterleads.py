import scrapy
import json

class GetKickstarterLeads(scrapy.Spider):
	name = 'kickstarterleads'
	baseURL ="https://www.kickstarter.com/discover/advanced?google_chrome_workaround&woe_id=0&staff_picks=1&raised=1&sort=end_date&seed=2541711&page={}"
	start_urls = [baseURL.format('1')]

	def parse(self, response):
		baseURL ="https://www.kickstarter.com/discover/advanced?google_chrome_workaround&woe_id=0&staff_picks=1&raised=1&sort=end_date&seed=2541711&page={}"
		currentPage = response.url
		pageNumber = int(currentPage[-1:]) #Extract page number as last char on the URL
		data = json.loads(response.body)

		for project in data.get('projects', []):
			item = dict()
			item['link'] = project.get('urls', {}).get('web', {}).get('project')
			item['source'] = 'kickstarter.com'
			fullname = project.get('creator', {}).get('name')
			if fullname is not None:
				if(len(fullname.split( ))>1):
					firstName = fullname.split( )[0]
					lastName = fullname.split( )[1]
				else:
					lastName = " "
			else:
				firstName = " "
				lastName = " "
			item['firstname'] = firstName
			item['lastname'] = lastName


			follow = project.get('creator', {}).get('urls', {}).get('web',{}).get('user')+"/about"
			request = scrapy.Request(url = follow, callback=self.parseProfile)
			request.meta['item'] = item
			yield request

		if (data['has_more']):
			nxt = str(pageNumber + 1)
			getNxtJSON = baseURL.format(nxt)
			yield scrapy.Request(url=getNxtJSON , callback=self.parse)

	def parseProfile(self, response):
		item = response.meta['item']

		links = response.css('ul.menu-submenu li')		

		n = 0
		sites = []
		while n<len(links):
			website = links[n].css('a::attr(href)').extract_first()
			sites.append(website)
		item['website'] = sites



		yield item


		



