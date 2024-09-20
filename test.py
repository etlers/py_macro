from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = 'https://ticket.interpark.com/Gate/TPLogin.asp'

driver = webdriver.Chrome()
driver.get(URL)

# iframe으로 구성되어 프레임을 변경해줘야 함
elem_iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(elem_iframe)

# 사용자 아이디
id_input = driver.find_element(By.NAME, "userId")
id_input.clear()
id_input.send_keys('byme72')
# 비밀번호
pw_input = driver.find_element(By.NAME, "userPwd")
pw_input.clear()
pw_input.send_keys('wndyd@801')
# pw_input.send_keys(Keys.RETURN)

while True:
    1 == 1

# 메뉴 - 연극 이미지 클릭
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn_play'))).send_keys(Keys.ENTER)
# driver.find_element(By.CLASS_NAME, 'btn_play').send_keys(Keys.ENTER)
# 검색
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'Nav_SearchWord'))).click()
search_input = driver.find_element(By.ID, "Nav_SearchWord")
search_input.clear()
search_input.send_keys('3일간의 비')
search_input.send_keys(Keys.RETURN)
# # 메뉴 - 3일간의비 이미지 클릭
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="allContent"]/div[1]/div[2]/ul/li[1]/div[1]/a'))).click()
# driver.find_element(By.XPATH, '//*[@id="allContent"]/div[1]/div[2]/ul/li[1]/div[1]/a').click()
# New Tab
driver.switch_to.window(driver.window_handles[-1])
# Popup Close
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popup-prdGuide"]/div/div[3]/button'))).click()
# driver.find_element(By.XPATH, '//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[33]').click()
# 날짜 선택
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[33]'))).click()
# 예매하기
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="productSide"]/div/div[2]/a[1]'))).click()

# 좌석 선택 팝업으로 이동
main_window = driver.current_window_handle
for handle in driver.window_handles: 
    if handle != main_window: 
        popup = handle
        driver.switch_to.window(popup)

elem_iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(elem_iframe)

# 첫번째 비어있는 좌석 선택
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SID0"]'))).send_keys(Keys.ENTER)
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn_play'))).send_keys(Keys.ENTER)
# 우측 하단 좌석 선택 클릭
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="NextStepImage"]'))).click()


for _ in range(10):
    time.sleep(1)
    print(1)

# # 웹 페이지에서 ID로 식별된 요소 가져오기
# elements = driver.find_elements(By.CSS_SELECTOR, "[name]")
# # 요소 출력
# list_ids = []
# for element in elements:
#     list_ids.append(element.get_attribute("name"))
# print(list_ids)

# for _ in range(10):
#     time.sleep(1)

driver.close()