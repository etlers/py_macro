from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
from selenium.common.exceptions import TimeoutException
import yaml
from selenium.webdriver.common.action_chains import ActionChains


def current_milli_time():
    return round(time.time() * 1000)


# 환경 파일에서 신청버튼을 누를 시각 가져오기
with open('weverse.yaml', encoding='utf-8-sig') as f:
    dict_cfg = yaml.safe_load(f)

run_tm = dict_cfg['run_tm']
print('신청버튼 클릭 시각:', run_tm)


URL = 'https://weverse.io/'

class_login = 'HeaderView_link_sign__jZmkX'
class_email_continue = 'sc-763a3587-1.gOzeoU' #'sc-763a3587-2.cTaekF'

email_id = 'iyreen@naver.com'
pswd = 'txt0304!'

driver = webdriver.Chrome()
driver.get(URL)


delay = 10 # seconds
# 참여신청만 자동으로 눌러주게 함
# driver.find_element_by_xpath("//div[@class='btn_Login']/input").click()

# 로그인 버튼
try:
    myElem = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.CLASS_NAME, class_login))).send_keys(Keys.ENTER)
    print("Login Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

# 이메일 아이디
try:
    myElem = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.NAME, 'userEmail'))).send_keys(email_id)
    print("email input is ready!")
except TimeoutException:
    print("Loading took too much time!")
# 이메일 진행
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/button").click()

# 비밀번호
try:
    myElem = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys(pswd)
    print("PSWD input is ready!")
except TimeoutException:
    print("Loading took too much time!")

# 여기까진 미리 진행해 둠

# try:
#     driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div[3]/button").click()
# except Exception as e:
#     print(e)

# while True:
#     last_tab = driver.window_handles[-1]
#     driver.switch_to.window(window_name=last_tab)
#     time.sleep(1)
#     last_tab = driver.window_handles[0]
#     driver.switch_to.window(window_name=last_tab)


#############################################################################################
# 신청버튼의 클릭
def wait_and_click():
    # 테스트로 로그인 버튼
    # driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/button").click()
    # 신청버튼은 미리 생성되어 있기에 누르기만 하면 됨
    # sc-eltbHq bMKJJd /html/body/div[1]/div/div/div/form/div/button
    # driver.switch_to( driver.window_handles[0] )
    # 새로운(마지막) 탭으로 이동
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)

    # driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/form/div/button").click()

    join_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/form/div/button")
                    
    # 해당 요소가 화면에 존재하지 않으면 클릭할 수 없으므로 요소가 보일때까지 스크롤하는 액션
    actions = ActionChains(driver).move_to_element(join_btn)
    actions.perform()
    join_btn.click()

#############################################################################################
# 로직의 시작
#############################################################################################
try:
    while True:
        # 100분의 1초 단위로 시각 체크를 위한 대기
        time.sleep(0.01)
        now_dtm = datetime.now().strftime('%Y%m%d %H%M%S')
        tm = now_dtm.split(' ')[1]
        # 지정한 시각과 맞는지 확인
        if tm >= run_tm:
            # 핸드폰 시각보다 살짝 빨라 조정
            time.sleep(0.1)
            start_ms = current_milli_time()
            print(tm)
            wait_and_click()
            end_ms = current_milli_time()
            print(datetime.now().strftime('%Y%m%d %H%M%S'))
            print((end_ms - start_ms) / 1000.0)
            # 신청 버튼 누르고 와서 종료
            break
except Exception as e:
    print(e)


while True:
    1 == 1
