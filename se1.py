import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

length=1000

def get_html(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error"
    
def get_html2(url):
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.maximize_window()
    driver.get(url)
    time.sleep(2)
    target = driver.find_element_by_xpath("//td[@data-reactid = '1553']")
    for i in range(0,4):
        driver.execute_script("arguments[0].scrollIntoView();",target)
        time.sleep(2)

    data = driver.page_source
    return data

def get_content(stockUrl):
    comments = []
    html = get_html2(stockUrl)
    soup = BeautifulSoup(html,'lxml')

    trTags = soup.find_all('tr',attrs={'class': 'BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)'})

    for tr in trTags:
       
        comment = {}

        try:

            td1 = tr.find('td',attrs={'class':'Py(10px) Ta(start) Pend(10px)'})
            comment['Time']  = td1.find('span').text.strip()
            comment['Open'] = tr.find_all('td',attrs={'class':'Py(10px) Pstart(10px)'})[0].find('span').text.strip()
            comment['High'] = tr.find_all('td',attrs={'class':'Py(10px) Pstart(10px)'})[1].find('span').text.strip()
            comment['Low'] = tr.find_all('td',attrs={'class':'Py(10px) Pstart(10px)'})[2].find('span').text.strip()

            comment['Close'] = tr.find_all('td',attrs={'class':'Py(10px) Pstart(10px)'})[3].find('span').text.strip()

            comment['Volume'] =  tr.find_all('td',attrs={'class':'Py(10px) Pstart(10px)'})[5].find('span').text.strip()

            comments.append(comment)

        except:
            print('Something Wrong')
    return comments

def write_in_file(dict):
    with open('History_AMAZ2.txt','a+')as f:
        for comment in dict:
            f.write('Time: {} \t Open: {} \t High: {} \t Low: {} \t Close: {} \t Volume: {} \n'.format(
                comment['Time'],comment['Open'],comment['High'],comment['Low'],comment['Close'],comment['Volume']))

        print('Wirte Success!')

def main(base_url):
    content = get_content(base_url)
    write_in_file(content)
    print('Success all')

base_url = 'https://finance.yahoo.com/quote/AMZN/history?p=AMZN'

if __name__ == '__main__':
    main(base_url)

