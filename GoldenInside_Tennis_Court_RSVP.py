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
driver.find_element(By.ID,"user_id").send_keys("sun0yoon26"); #gkim10 #sun0yoon26
driver.find_element(By.ID,"user_password").send_keys("cotton123!");
time.sleep(1)
driver.find_element(By.CLASS_NAME,"submit").click()


# ###############
# # 강서 굴다리 밑 조폭에게 끌려감
# ###############
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR,'#center > option:nth-child(3)').click(); #강서 구립 선택   
time.sleep(0.5)
#코트 선택
# driver.find_element(By.CSS_SELECTOR,'#place > option:nth-child(1)').click(); #3번 코트
# driver.find_element(By.CSS_SELECTOR,'#place > option:nth-child(2)').click(); #4번 코트
# driver.find_element(By.CSS_SELECTOR,'#place > option:nth-child(3)').click(); #5번 코트
driver.find_element(By.CSS_SELECTOR,'#place > option:nth-child(4)').click(); #6번 코트
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR,'#search > fieldset > div > div > div > button').click(); #조회 버튼 클릭
time.sleep(0.5)

#날짜 선택
driver.find_element(By.ID,"next_month").click();#다음달로 달력을 넘길 때 필수!
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR,'#date-20221210').click();#특정 날짜 선택
time.sleep(0.5)

while True:
    now = datetime.now()
    print(now)
    if driver.find_element(By.XPATH,"//*[@id='checkbox_time_0']").is_displayed() == False:
        time.sleep(5) #로딩시간까지 0.5초 기다림
        driver.refresh() #계속 REFRESH
        break
    else:
        ### 아래에서 시간 택 1 ###
        # driver.find_element(By.XPATH,"//*[@id='checkbox_time_0']").click(); # 9시~11시
        driver.find_element(By.XPATH,"//*[@id='checkbox_time_1']").click(); # 11시~13시
        # driver.find_element(By.XPATH,"//*[@id='checkbox_time_2']").click(); # 13시~15시
        # driver.find_element(By.XPATH,"//*[@id='checkbox_time_3']").click(); # 15시~17시
        # driver.find_element(By.XPATH,"//*[@id='checkbox_time_4']").click(); # 17시~19시
        # driver.find_element(By.XPATH,"//*[@id='checkbox_time_5']").click(); # 19시~21시
        driver.find_element(By.CSS_SELECTOR,'#contents > article > div > div > div.order_r > button').click();
    break

# 상세 예약 페이지로 진입 후 대관 완료
driver.find_element(By.ID,"users").send_keys("4");
driver.find_element(By.ID,"purpose").send_keys("운동");
driver.find_element(By.ID,"agree_use1").click();
driver.find_element(By.CSS_SELECTOR,"#writeForm > fieldset > p:nth-child(25) > button > span").click();
time.sleep(0.1)


###추가 예약 시###
driver.get('https://sports.gangseo.seoul.kr/fmcs/28?facilities_type=C&base_date=&rent_type=1001&center=GANGSEO05&part=02&place=1')
driver.implicitly_wait(2) #로딩이 끝날 때까지 2초를 기다려준다.
driver.find_element(By.CSS_SELECTOR,'#center > option:nth-child(3)').click(); #강서 구립 선택   
time.sleep(0.1)
#코트 선택
# driver.find_element(By.CSS_SELECTOR,'#place > option:nth-child(1)').click(); #3번 코트
# driver.find_element(By.CSS_SELECTOR,'#place > option:nth-child(2)').click(); #4번 코트
# driver.find_element(By.CSS_SELECTOR,'#place > option:nth-child(3)').click(); #5번 코트
driver.find_element(By.CSS_SELECTOR,'#place > option:nth-child(4)').click(); #6번 코트
time.sleep(0.1)
driver.find_element(By.CSS_SELECTOR,'#search > fieldset > div > div > div > button').click(); #조회 버튼 클릭
time.sleep(0.2)

#날짜 선택
driver.find_element(By.ID,"next_month").click();#다음달로 달력을 넘길 때 필수!
time.sleep(0.25)
driver.find_element(By.CSS_SELECTOR,'#date-20221211').click();#특정 날짜 선택
time.sleep(0.25)
# driver.find_element(By.XPATH,"//*[@id='checkbox_time_0']").click(); # 9시~11시
driver.find_element(By.XPATH,"//*[@id='checkbox_time_1']").click(); # 11시~13시
# driver.find_element(By.XPATH,"//*[@id='checkbox_time_2']").click(); # 13시~15시
# driver.find_element(By.XPATH,"//*[@id='checkbox_time_3']").click(); # 15시~17시
# driver.find_element(By.XPATH,"//*[@id='checkbox_time_4']").click(); # 17시~19시
# driver.find_element(By.XPATH,"//*[@id='checkbox_time_5']").click(); # 19시~21시
driver.find_element(By.CSS_SELECTOR,'#contents > article > div > div > div.order_r > button').click();

#상세 예약 페이지로 진입 후 대관 완료
driver.find_element(By.ID,"users").send_keys("4");
driver.find_element(By.ID,"purpose").send_keys("운동");
driver.find_element(By.ID,"agree_use1").click();
driver.find_element(By.CSS_SELECTOR,"#writeForm > fieldset > p:nth-child(25) > button > span").click();



# ##################
# # 황금내 날짜 선택
# ##################
# time.sleep(0.5)
# driver.find_element(By.CSS_SELECTOR,'#search > fieldset > div > div > div > button').click(); #조회 버튼 클릭
# # driver.find_element(By.ID,"next_month").click();#다음달로 달력을 넘길 때 필수!
# time.sleep(0.5)
# driver.find_element(By.XPATH,'//*[@id="date-20221112"]').click();#날짜 선택
# time.sleep(0.5)

# #열리는 시간까지 새로고침
# while True:
#     now = datetime.now()
#     print(now)
#     if driver.find_element(By.XPATH,"//*[@id='checkbox_time_0']").is_displayed() == False:
#         time.sleep(0.5) #로딩시간까지 0.5초 기다림
#         driver.refresh() #계속 REFRESH
#         continue
#     else:
#         ### 아래에서 시간 택 1 ###
#         # driver.find_element(By.XPATH,"//*[@id='checkbox_time_0']").click(); # 시간 오전 09-10 ###"226;1;0900;1000;1"
#         # driver.find_element(By.XPATH,"//*[@id='checkbox_time_1']").click(); # 시간 오전 10-11 ###"227;2;1000;1100;1"
#         # driver.find_element(By.XPATH,"//*[@id='checkbox_time_2']").click(); # 시간 오전 11-12 ###"228;3;1100;1200;1"
#         driver.find_element(By.XPATH,"//*[@id='checkbox_time_3']").click(); # 시간 오후 12-13 ###"229;4;1200;1300;1"
#         # driver.find_element(By.XPATH,"//*[@id='checkbox_time_4']").click();   # 시간 오후 13-14 ###"230;5;1300;1400;1"
#         # driver.find_element(By.XPATH,"//*[@id='checkbox_time_5']").click(); # 시간 오후 14-15 ###"231;6;1400;1500;1"
#         driver.find_element(By.CSS_SELECTOR,'#contents > article > div > div > div.order_r > button').click();
#     break

# #상세 예약 페이지로 진입 후
# driver.find_element(By.ID,"users").send_keys("2");
# driver.find_element(By.ID,"purpose").send_keys("운동");
# driver.find_element(By.ID,"agree_use1").click();
# driver.find_element(By.CSS_SELECTOR,"#writeForm > fieldset > p:nth-child(25) > button > span").click();



################
# 우장산 테니스장
################

# time.sleep(0.5)
# driver.find_element(By.CSS_SELECTOR,'#center > option:nth-child(2)').click(); #우장산 선택   
# time.sleep(0.5)
# driver.find_element(By.CSS_SELECTOR,'#part > option:nth-child(2)').click(); #우장산 테니스장 선택
# time.sleep(0.5)

# #코트 선택
# # driver.find_element(By.CSS_SELECTOR, '#place > option:nth-child(1)').click(); #1번 코트
# # driver.find_element(By.CSS_SELECTOR, '#place > option:nth-child(2)').click(); #2번 코트
# # driver.find_element(By.CSS_SELECTOR, '#place > option:nth-child(3)').click(); #3번 코트
# driver.find_element(By.CSS_SELECTOR, '#place > option:nth-child(4)').click(); #4번 코트 
# time.sleep(0.5)
# driver.find_element(By.CSS_SELECTOR,'#search > fieldset > div > div > div > button').click(); #조회 버튼 클릭
# time.sleep(0.5)

# driver.find_element(By.ID,"next_month").click();#다음달로 달력을 넘길 때 필수!
# time.sleep(0.5)
# driver.find_element(By.XPATH,'//*[@id="date-20221112"]').click();#날짜 선택
# time.sleep(0.5)

# #열리는 시간까지 새로고침
# while True:
#     now = datetime.now()
#     print(now)
#     if driver.find_element(By.XPATH,"//*[@id='checkbox_time_0']").is_displayed() == False:
#     # if (driver.find_element(By.XPATH,"//*[@id='checkbox_time_0']").get_attribute("value") != "266;1;0900;1000;1"):
#         time.sleep(0.5) #로딩시간까지 0.5초 기다림
#         driver.refresh() #계속 REFRESH
#         continue
#     else:
#         ### 아래에서 시간 택 1 ###
#         # driver.find_element(By.XPATH,"//*[@id='checkbox_time_0']").click(); # 시간 오전 08-11
#         driver.find_element(By.XPATH,"//*[@id='checkbox_time_1']").click(); # 시간 오전후 11-14
#         # driver.find_element(By.XPATH,"//*[@id='checkbox_time_2']").click(); # 시간 오후 14-17

#         driver.find_element(By.CSS_SELECTOR,'#contents > article > div > div > div.order_r > button').click();
#     break


# #상세 예약 페이지로 진입 후
# driver.find_element(By.ID,"users").send_keys("4");
# driver.find_element(By.ID,"purpose").send_keys("운동");
# driver.find_element(By.ID,"agree_use1").click();
# driver.find_element(By.CSS_SELECTOR,"#writeForm > fieldset > p:nth-child(25) > button > span").click();