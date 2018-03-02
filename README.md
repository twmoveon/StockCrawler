# StockPriceRetrieve

A python web crawler used by Software Engineering Web Application Course.
The crawler retrieves dynamicly the historical price and realtime price of 10 companies from Yahoo Finance("https://finance.yahoo.com) and store the data in MySQL database.

Notes:
1. Use Beautiful Soup(bs4) and Requests to analyze html file.

2. Use Selenium to reslove the web dynamic pull-down issuse. The key is to use webdriver to imitate a real web browser.(The Path of webdriver need to be fixed carefully!)

3. When doing web scoll-down, use Xpath to locate the target element: target = driver.find_element_by_xpath("//td[@data-reactid = '1553']")

4. DROP TABLE before Create
