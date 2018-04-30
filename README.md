# Crowd-Funding-Bots
SET UP <br>
  1. <code>pip install scrapy</code> <br>
  2. <code>pip install selenium</code> <br>
  3. Download Selenium webdriver for Chrome <br><br>
  
USAGE <br>
  <b>1. kickstarter.com </b> <br>
      a) <code>cd KickstarterDotComScraper</code><br>
      b) <code>scrapy list</code><br>
      c) <code>scrapy crawl kickstarterleads -o nameOfFile.json</code><br><br>
          1.1 Limitation:<br>
            - Collects info for the first 240 projects under the filter 'Nearly Funded' only<br>
          1.2 Solution (to collect info about ALL projects): <br>
            - Replace lines 6 and 10 on kickstarterleads.py with: <b>baseURL = "https://www.kickstarter.com/discover/advanced?google_chrome_workaround&woe_id=0&sort=magic&seed=2541734&page={}<b> <br>
  
  <b>2. crowdsupply.com </b><br>
      a) <code>cd CrowdSupplyDotComScraper</code><br>
      b) <code>scrapy list</code><br>
      c) <code>scrapy crawl crowdsupplyyields -o nameOfFile.json</code><br><br>
          2.1 Limitations:<br>
            - Collects info for the projects under the filters 'Archived', 'Crowdfunding, 'Available' only <br>
          2.2 Solution (to collect info about ALL projects: <br>
            - To 'start_urls' on line 7 of CrowdSupplyYields.py add links to other categories e.g. 'https://www.crowdsupply.com/computers-and-networking' <br>
  
  <b>3. experiment.com</b> <br>
      a) <code>cd ExperimentDotComScraper</code><br>
      b) Change path to Chrome Webdriver on line 77 <br>
      c) <code>python experimentDotComScraper.py</code><br><br>
          3.1 Limitations:<br>
            - Collects info about 180 projects only<br>
          3.2 Solution (to collect info about ALL projects): <br>
            - Remove 'if-else' block checking whether k>=30 at line 35 of experimentDotComScraper.py
      
  
  



