import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

import csv

def getHtml(url):
    # Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}
    try:
        response = requests.get(url,timeout=40,headers=headers)
        response.raise_for_status()

        response.encoding = response.apparent_encoding

        return response.text
    except:
        import traceback
        traceback.print_exc()


def downloadPaper(url):
    try:
        

        soup = BeautifulSoup(getHtml(url), 'html.parser')
        result = soup.body.find_all('iframe')
        

        downloadUrl = result[-1].attrs['src'].split('?')[0]
        
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}
        response = requests.get(downloadUrl, timeout=80, headers=headers)
        
        time.sleep(10)
        
        fname = downloadUrl[-12:]
# =============================================================================
#         print(fname)
# =============================================================================
        path = "downloadedPDF\\" + fname
        print(path)
        with open(path,'ab+') as f:
            print('start download file',fname,'...')
            f.write(response.content)
        print('successed !')
        return True
    except:
        print('Failed !')
        return False

# =============================================================================
# def catchPaperNumber(thesis_want):
# =============================================================================
    

if __name__ == '__main__':
    driver = webdriver.PhantomJS(executable_path=r'[your phantomjs.exe path')  # PhantomJs
    #driver.get('https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=Intelligence')  # 輸入範例網址，交給瀏覽器
    driver.get('https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=Intelligence&ranges=2016_2020_Year&rowsPerPage=100&sortType=desc_p_Citation_Countieeexplore.ieee.org%2Fsearch%2Fsearchresult.jsp')

        
    time.sleep(10)


    js = 'var button = document.getElementsByClassName("loadMore-btn"); '
    driver.execute_script(js)
    time.sleep(5)
    print('getElementsByClassName')
    loadmore_time=40
    for i in range(0,loadmore_time):
        js = 'var button = document.getElementsByClassName("loadMore-btn");button[0].click();'
        driver.execute_script(js)        
        print('pressed loadMore button',i)
        time.sleep(10)

    ele_num = []

    link_list = driver.find_elements_by_xpath('//a[@class="icon-pdf"]') #使用selenium的xpath定位到每個具有data-artnum元素
    print('Catching thesis number......')
    link_count=1
    start_from=1099
    test_num_limit=3
    for link in link_list:
        if test_num_limit<=0: 
            break
        if(link_count>=start_from):
            thesis_num = link.get_attribute('data-artnum')
            ele_num.append(thesis_num)
            print(thesis_num)
        link_count+=1
        
        #test_num_limit-=1
    with open('thesis_num.csv', 'w', newline='') as csvfile:
        writer  = csv.writer(csvfile)
        for row in ele_num:
            writer.writerow([row])    
    
    print('length of thesis_num =',len(ele_num))
    driver.close()        
        
# =============================================================================
#     print(ele_num)
# =============================================================================
    

    baseUrl = 'http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber='
    thesis_want=1000
    download_try=0
    download_success=0
    download_fail=0
    
    jump=0
    wantToJump=1601
    for eleNum in ele_num:
        
        if(jump<wantToJump):
            jump+=1
            print('skip')
            continue
        if(download_success>=thesis_want): 
            break
        newUrl = baseUrl + str(eleNum)
        result = downloadPaper(newUrl)
        if(result):
            download_success+=1
        else:
            download_fail+=1     
        download_try+=1
        print('finished:',download_try,'/',len(ele_num))
        print('successed:',download_success,'/',download_try)

    
    print('')
    print('Total tried: ',download_try)
    print('Success: ',download_success)
    print('Fail:',download_fail)

