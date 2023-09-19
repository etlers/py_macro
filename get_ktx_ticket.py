import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = 'https://www.letskorail.com/'

driver = webdriver.Firefox()
driver.get(URL)


# 발권을 위한 정보
def reserv_ticket():    
    # 로그인
    id_input = driver.find_element(By.NAME, "txtMember")
    id_input.clear()
    id_input.send_keys('9760227232')
    pw_input = driver.find_element(By.NAME, "txtPwd")
    pw_input.clear()
    pw_input.send_keys('wndyd@801')
    pw_input.send_keys(Keys.RETURN)
    # 결재하기 버튼
    driver.find_element(By.XPATH, '//*[@id="btn_next"]"]').click()
    # 신용카드 탭
    driver.find_element(By.XPATH, '//*[@id="tabStl1"]').click()    
    # 신용카드 번호 - ByName
    cd_input_01 = driver.find_element(By.NAME, "txtCardNo1")
    cd_input_01.clear()
    cd_input_01.send_keys('1234')
    cd_input_02 = driver.find_element(By.NAME, "txtCardNo2")
    cd_input_02.clear()
    cd_input_02.send_keys('5678')
    cd_input_03 = driver.find_element(By.NAME, "txtCardNo3")
    cd_input_03.clear()
    cd_input_03.send_keys('9012')
    cd_input_04 = driver.find_element(By.NAME, "txtCardNo4")
    cd_input_04.clear()
    cd_input_04.send_keys('3456')

    # 카드 비밀번호 - ByName
    cd_pw_input = driver.find_element(By.NAME, "txtCCardPwd_1")
    cd_pw_input.clear()
    cd_pw_input.send_keys('05')
    # 주민번호
    jumin_input = driver.find_element(By.NAME, "txtJuminNo2_1")
    jumin_input.clear()
    jumin_input.send_keys('721005')
    # 개인정보 수집 동의
    driver.find_element(By.XPATH, '//*[@id="chkAgree"]').click()
    # 발권하기
    driver.find_element(By.XPATH, '//*[@id="fnIssuing"]').click()

    return True


# 도착역
end_station_input = driver.find_element(By.NAME, "txtGoEnd")
end_station_input.clear()
end_station_input.send_keys('강릉')
end_station_input.send_keys(Keys.RETURN)
# 일자 클릭
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="res_cont_tab01"]/form/div/fieldset/ul[2]/li[1]/a/img').click()
# New Tab
driver.switch_to.window(driver.window_handles[-1])
# 날짜 선택
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[5]/td[3]/a'))).click()
# New Tab
driver.switch_to.window(driver.window_handles[-1])
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="time"]/option[19]'))).click()
# 예매하기
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="res_cont_tab01"]/form/div/fieldset/p/a/img'))).click()

time.sleep(3)

got_it = False

while not got_it:
    for i in range(20):  
        try:
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="tableResult"]/tbody/tr[{i}]/td[6]/a[1]/img'))).click()
            print('OK')
            got_it = reserv_ticket()

        except selenium.common.exceptions.TimeoutException:
            print('NG')
