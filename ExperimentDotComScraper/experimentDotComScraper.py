from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import requests
import urllib2
import time
import csv
import sys

def elementExistsByTag(tag, parent):
	try:
		parent.find_element_by_tag_name(tag)
	except NoSuchElementException:
		return False
	return True

def showMoreButton(className, parent):
	try:
		parent.find_element_by_css_selector(className)
	except NoSuchElementException:
		return False
	return True

def scrollToBottom(driver):
	lastHeight = driver.execute_script('return document.body.scrollHeight')
	k = 0
	while True:
		driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
		time.sleep(15)
		k = k+1
		
		newHeight = driver.execute_script('return document.body.scrollHeight')
		if newHeight == lastHeight:
			if showMoreButton('.btn.btn-primary.btn-lg.show-more', driver):
				if(k>=30):
					break
				else:
					driver.find_element_by_css_selector('.btn.btn-primary.btn-lg.show-more').click()
			else:	
				break
		else:
			lastHeight = newHeight

def scrapePage(driver, source):
	time.sleep(5)

	projects = driver.find_elements_by_xpath('//div[@data-source="discover"]')

	with open('experimentdotcom.csv','a') as dump:
		writer = csv.writer(dump)
		writer.writerow(['Source', 'Project Link', 'First Name', 'Last Name', 'Organisation'])

		for project in projects:
			link = project.find_element_by_class_name('project-card-content').find_element_by_tag_name('h3').find_element_by_tag_name('a').get_attribute('href')

			fullName = project.find_element_by_class_name('project-card-footer').find_element_by_class_name('researcher-info').find_element_by_class_name('researcher-description').find_element_by_tag_name('a').text.encode('ascii','ignore').decode('ascii')
			if(len(fullName.split( ))>1):
				firstName = fullName.split( )[0]
				lastName = fullName.split( )[1]
			else:
				firstName = fullName.split( )[0]
				lastName = " "

			institution = project.find_element_by_class_name('project-card-footer').find_element_by_class_name('researcher-info').find_element_by_class_name('researcher-institution').find_element_by_class_name('institution')

			if elementExistsByTag('a', institution):
				place = institution.find_element_by_tag_name('a').text.encode('ascii','ignore').decode('ascii')
			else:
				place = institution.text.encode('ascii','ignore').decode('ascii')


			writer.writerow([source, link, firstName, lastName, place])




path = 'path/to/chromedriver.exe'
url = 'https://experiment.com/discover'
driver = webdriver.Chrome(path)
driver.get(url)

driver.maximize_window()
scrollToBottom(driver)
scrapePage(driver, url)
driver.quit()

