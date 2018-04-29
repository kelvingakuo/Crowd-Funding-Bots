# Crowd-Funding-Bots
Set-up: <br>
  1. <code>pip install scrapy</code> <br>
  2. <code>pip install selenium</code> <br>
  3. Download Selenium webdriver for Chrome <br>
  
Usage: <br>
  <b>1. kickstarter.com <br><b>
      <code>cd KickstarterDotComScraper</code><br>
      <code>scrapy list</code><br>
      <code>scrapy crawl kickstarterleads -o nameOfFile.json</code><br>
          Limitations:<br>
            - Collects info for the first 240 projects under the filter 'Nearly Funded' only<br><br>
  
  <b>2. crowdsupply.com <b><br>
      <code>cd CrowdSupplyDotComScraper</code><br>
      <code>scrapy list</code><br>
      <code>scrapy crawl crowdsupplyyields -o nameOfFile.json</code><br>
          Limitations:<br>
            - Collects info for the projects under the filters 'Archived', 'Crowdfunding, 'Available' only <br><br>
  
  <b>3. experiment.com <br></b>
      <code>cd ExperimentDotComScraper</code><br>
      <code>python experimentDotComScraper.py</code><br>
          Limitations:<br>
            - Collects info about ALL projects slowly<br><br>
      
  
  



