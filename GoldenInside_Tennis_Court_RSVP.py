from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
import csv


#기본 세팅
def chromeWebdriver(): 
    chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=chrome_service, options=options)
    return driver

driver = chromeWebdriver()

#웹사이트 열기
driver.get('https://sports.gangseo.seoul.kr/fmcs/28?facilities_type=C&base_date=&rent_type=1001&center=GANGSEO05&part=02&place=1')
driver.implicitly_wait(2) #로딩이 끝날 때까지 2초를 기다려준다.

#로그인
driver.find_element(By.ID,"process_login").click();
driver.find_element(By.ID,"user_id").send_keys("sun0yoon26");
driver.find_element(By.ID,"user_password").send_keys("cotton123!");
driver.implicitly_wait(2) #로딩이 끝날 때까지 2초를 기다려준다.
driver.find_element(By.CLASS_NAME,"submit").click()

#열리는 시간까지 새로고침
while True:
    now = datetime.now()
    print(now)
    start_time = now.replace(hour=22, minute=35)
    end_time = now.replace(hour=23, minute=4)

    if start_time < now < end_time:
        driver.refresh()
        continue
    else: end_time == now
    break

#날짜 선택
driver.find_element(By.ID,"next_month").click();#다음달로 달력을 넘길 때 필수!
driver.implicitly_wait(0.5)

driver.find_element(By.XPATH,'//*[@id="date-20221015"]').click();

    






#대관 신청 클릭
# time.sleep(2)


# #무한 스크롤 내리기======================

# #현재 스크롤 위치
# scroll = browser.execute_script('return window.scrollY')

# while True:
#     #맨 아래로 스크롤을 내린다
#     browser.find_element_by_css_selector("body").send_keys(Keys.END)

#     #스크롤 사이 페이지 로딩 시간
#     time.sleep(1)

#     #마지막 스크롤 위치
#     after_h = browser.execute_script('return window.scrollY')
#     if after_h == scroll:
#         break
#     scroll = after_h

# #파일 생성
# #f = open(r"C:\Python\data.csv", 'w', encoding='UTF-8-sig', newline='')
# #csvWriter = csv.writer(f)


# #상품 정보 DIV
# items = browser.find_elements_by_css_selector('basicList_info_area__17Xyo')

# for item in items:
#     name = item.find_element_by_css_selector('basicList_title__3P9Q7').text
#     try:
#         price = item.find_element_by_css_selector('price_num__2WUXn').text
#     except:
#         price = "판매중단"
#     link = item.find_element_by_css_selector('basicList_title__3P9Q7 > a').get_attribute('href')
#     print(name,price,link)

# #    csvWriter.writerow([name,price,link]) #한 행을 추가하겠다. 

# #파일 닫기
# #f.close()