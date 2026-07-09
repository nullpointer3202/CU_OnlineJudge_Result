from scripts import crawl_data, login, make_graph, print_data
import selenium
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

import numpy as np

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.alert import Alert

from selenium.webdriver.chrome.service import Service

from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

URL = "https://oj.chosun.ac.kr/index.php/auth/login/"

#크롬 드라이버 초기화 및 실행
driver = webdriver.Chrome(options=chrome_options)

#URL 열기
driver.get(url = URL)

#사이트가 다운될 경우 오류
login.oj_login(driver)

course_name = crawl_data.get_course(driver)

assignment_name = crawl_data.get_assignments(driver)



#과제 내 문제들을 찾는 코드
problems_page = driver.current_url

problems = driver.find_elements(By.XPATH,'/html/body/div[2]/div/div[4]/div/table/tbody/tr[position()>0]')

datalist = []

for idx, problem in enumerate(problems) :

    prob = driver.find_elements(By.XPATH,'/html/body/div[2]/div/div[4]/div/table/tbody/tr[position()>0]')


    #문제 이름들을 찾아내 출력하는 코드
    problem_name = prob[idx].find_element(By.XPATH, './/td[2]/a')###########
    problem_status = prob[idx].find_element(By.XPATH, './/td[7]/a')
    print(f"\n[{idx+1}] {problem_name.text}")

    print("데이터 받아오는 중....")
    crawl_data.get_status(prob[idx], driver)
    datalist.append(crawl_data.get_data(driver))
    #print(datalist[idx])

    driver.get(problems_page)

print(datalist)


#디버그용. 또는 OJ 사용 불가 시 사용
#course_name = "디버그 과목명"
#assignment_name = "디버그 시험명"

#datalist = [[{'suid': '20233095', 'result': 'Accept', 'score': 100.0}, {'suid': '20233146', 'result': 'Accept', 'score': 100.0}, {'suid': '20233088', 'result': 'Accept', 'score': 100.0}, {'suid': '20233097', 'result': 'Accept', 'score': 100.0}, {'suid': '20233132', 'result': 'Accept', 'score': 100.0}, {'suid': '20233065', 'result': 'Accept', 'score': 100.0}, {'suid': '20233092', 'result': 'Accept', 'score': 100.0}, {'suid': '20233086', 'result': 'Accept', 'score': 100.0}, {'suid': '20233121', 'result': 'Accept', 'score': 100.0}, {'suid': '20233117', 'result': 'Accept', 'score': 100.0}, {'suid': '20233057', 'result': 'Accept', 'score': 100.0}, {'suid': '20233101', 'result': 'Accept', 'score': 100.0}, {'suid': '20233185', 'result': 'Accept', 'score': 100.0}, {'suid': '20203146', 'result': 'Accept', 'score': 100.0}, {'suid': '20233058', 'result': 'Accept', 'score': 100.0}, {'suid': '20233161', 'result': 'Accept', 'score': 100.0}, {'suid': '20233107', 'result': 'Accept', 'score': 100.0}, {'suid': '20233163', 'result': 'Accept', 'score': 100.0}, {'suid': '20233172', 'result': 'Accept', 'score': 100.0}, {'suid': '20212790', 'result': 'Accept', 'score': 100.0}, {'suid': '20233106', 'result': 'Accept', 'score': 100.0}, {'suid': '20233167', 'result': 'Accept', 'score': 100.0}, {'suid': '20223161', 'result': 'Accept', 'score': 100.0}, {'suid': '20233090', 'result': 'Accept', 'score': 100.0}, {'suid': '20205087', 'result': 'Accept', 'score': 100.0}, {'suid': '20233127', 'result': 'Accept', 'score': 100.0}, {'suid': '20210470', 'result': 'Accept', 'score': 100.0}, {'suid': '20233160', 'result': 'Accept', 'score': 100.0}, {'suid': '20233109', 'result': 'Accept', 'score': 100.0}, {'suid': '20233071', 'result': 'Accept', 'score': 100.0}, {'suid': '20233115', 'result': 'Accept', 'score': 100.0}, {'suid': '20233133', 'result': 'Accept', 'score': 100.0}, {'suid': '20233145', 'result': 'Accept', 'score': 100.0}, {'suid': '20190445', 'result': 'Accept', 'score': 100.0}, {'suid': '20233122', 'result': 'Accept', 'score': 100.0}, {'suid': '20181771', 'result': 'Wrong Answer', 'score': 75.0}, {'suid': '20220484', 'result': 'Wrong Answer', 'score': 0.0}], [{'suid': '20233185', 'result': 'Accept', 'score': 100.0}, {'suid': '20233117', 'result': 'Accept', 'score': 100.0}, {'suid': '20233092', 'result': 'Accept', 'score': 100.0}, {'suid': '20233172', 'result': 'Accept', 'score': 100.0}, {'suid': '20233109', 'result': 'Accept', 'score': 100.0}, {'suid': '20210470', 'result': 'Accept', 'score': 100.0}, {'suid': '20233132', 'result': 'Accept', 'score': 100.0}, {'suid': '20233101', 'result': 'Accept', 'score': 100.0}, {'suid': '20233163', 'result': 'Accept', 'score': 100.0}, {'suid': '20203146', 'result': 'Accept', 'score': 100.0}, {'suid': '20233160', 'result': 'Accept', 'score': 100.0}, {'suid': '20233086', 'result': 'Accept', 'score': 100.0}, {'suid': '20233095', 'result': 'Accept', 'score': 100.0}, {'suid': '20212790', 'result': 'Accept', 'score': 100.0}, {'suid': '20233106', 'result': 'Accept', 'score': 100.0}, {'suid': '20233161', 'result': 'Accept', 'score': 100.0}, {'suid': '20233065', 'result': 'Accept', 'score': 100.0}, {'suid': '20233058', 'result': 'Accept', 'score': 100.0}, {'suid': '20233090', 'result': 'Accept', 'score': 100.0}, {'suid': '20233121', 'result': 'Accept', 'score': 100.0}, {'suid': '20233057', 'result': 'Accept', 'score': 100.0}, {'suid': '20233145', 'result': 'Accept', 'score': 100.0}, {'suid': '20190445', 'result': 'Accept', 'score': 100.0}, {'suid': '20233115', 'result': 'Accept', 'score': 100.0}, {'suid': '20233088', 'result': 'Accept', 'score': 100.0}, {'suid': '20233122', 'result': 'Accept', 'score': 100.0}, {'suid': '20233097', 'result': 'Wrong Answer', 'score': 75.0}, {'suid': '20233146', 'result': 'Wrong Answer', 'score': 75.0}, {'suid': '20233167', 'result': 'Wrong Answer', 'score': 0.0}, {'suid': '20233133', 'result': 'Wrong Answer', 'score': 0.0}, {'suid': '20233071', 'result': 'Wrong Answer', 'score': 0.0}, {'suid': '20205087', 'result': 'Wrong Answer', 'score': 0.0}, {'suid': '20220484', 'result': 'Run-Time Error', 'score': 0.0}], [{'suid': '20190445', 'result': 'Accept', 'score': 100.0}, {'suid': '20233090', 'result': 'Accept', 'score': 100.0}, {'suid': '20233058', 'result': 'Accept', 'score': 100.0}, {'suid': '20233071', 'result': 'Accept', 'score': 100.0}, {'suid': '20233121', 'result': 'Accept', 'score': 100.0}, {'suid': '20233106', 'result': 'Accept', 'score': 100.0}, {'suid': '20233101', 'result': 'Accept', 'score': 100.0}, {'suid': '20233097', 'result': 'Accept', 'score': 100.0}, {'suid': '20233109', 'result': 'Accept', 'score': 100.0}, {'suid': '20233065', 'result': 'Accept', 'score': 100.0}, {'suid': '20233117', 'result': 'Accept', 'score': 100.0}, {'suid': '20233092', 'result': 'Accept', 'score': 100.0}, {'suid': '20233160', 'result': 'Accept', 'score': 100.0}, {'suid': '20233057', 'result': 'Accept', 'score': 100.0}, {'suid': '20233115', 'result': 'Accept', 'score': 100.0}, {'suid': '20233122', 'result': 'Accept', 'score': 100.0}, {'suid': '20203146', 'result': 'Wrong Answer', 'score': 33.3}, {'suid': '20233088', 'result': 'Wrong Answer', 'score': 33.3}, {'suid': '20233163', 'result': 'Wrong Answer', 'score': 33.3}, {'suid': '20233185', 'result': 'Wrong Answer', 'score': 33.3}, {'suid': '20233145', 'result': 'Output Limit', 'score': 0.0}, {'suid': '20233161', 'result': 'Wrong Answer', 'score': 0.0}, {'suid': '20233172', 'result': 'Output Limit', 'score': 0.0}, {'suid': '20223161', 'result': 'Wrong Answer', 'score': 0.0}, {'suid': '20233086', 'result': 'Wrong Answer', 'score': 0.0}], [{'suid': '20233160', 'result': 'Accept', 'score': 100.0}, {'suid': '20233185', 'result': 'Accept', 'score': 100.0}, {'suid': '20233117', 'result': 'Accept', 'score': 100.0}, {'suid': '20233058', 'result': 'Accept', 'score': 100.0}, {'suid': '20233145', 'result': 'Accept', 'score': 100.0}, {'suid': '20233172', 'result': 'Accept', 'score': 100.0}, {'suid': '20233163', 'result': 'Accept', 'score': 100.0}, {'suid': '20233101', 'result': 'Accept', 'score': 100.0}, {'suid': '20233065', 'result': 'Accept', 'score': 100.0}, {'suid': '20233095', 'result': 'Accept', 'score': 100.0}, {'suid': '20190445', 'result': 'Accept', 'score': 100.0}, {'suid': '20233092', 'result': 'Accept', 'score': 100.0}, {'suid': '20205087', 'result': 'Accept', 'score': 100.0}, {'suid': '20233121', 'result': 'Accept', 'score': 100.0}, {'suid': '20233133', 'result': 'Accept', 'score': 100.0}, {'suid': '20233057', 'result': 'Accept', 'score': 100.0}, {'suid': '20233167', 'result': 'Accept', 'score': 100.0}, {'suid': '20233090', 'result': 'Accept', 'score': 100.0}, {'suid': '20233071', 'result': 'Accept', 'score': 100.0}, {'suid': '20233115', 'result': 'Accept', 'score': 100.0}, {'suid': '20233086', 'result': 'Accept', 'score': 100.0}, {'suid': '20233122', 'result': 'Accept', 'score': 100.0}, {'suid': '20233109', 'result': 'Accept', 'score': 100.0}, {'suid': '20212790', 'result': 'Wrong Answer', 'score': 0.0}, {'suid': '20223161', 'result': 'Wrong Answer', 'score': 0.0}, {'suid': '20233097', 'result': 'Wrong Answer', 'score': 0.0}, {'suid': '20181771', 'result': 'Wrong Answer', 'score': 0.0}], [{'suid': '20233092', 'result': 'Accept', 'score': 100.0}, {'suid': '20233097', 'result': 'Accept', 'score': 100.0}, {'suid': '20233145', 'result': 'Accept', 'score': 100.0}, {'suid': '20223161', 'result': 'Accept', 'score': 100.0}, {'suid': '20233058', 'result': 'Accept', 'score': 100.0}, {'suid': '20233133', 'result': 'Accept', 'score': 100.0}, {'suid': '20233185', 'result': 'Accept', 'score': 100.0}, {'suid': '20233065', 'result': 'Accept', 'score': 100.0}, {'suid': '20233095', 'result': 'Accept', 'score': 100.0}, {'suid': '20205087', 'result': 'Accept', 'score': 100.0}, {'suid': '20181771', 'result': 'Accept', 'score': 100.0}, {'suid': '20190445', 'result': 'Accept', 'score': 100.0}, {'suid': '20233101', 'result': 'Accept', 'score': 100.0}, {'suid': '20233086', 'result': 'Accept', 'score': 100.0}, {'suid': '20233057', 'result': 'Accept', 'score': 100.0}, {'suid': '20233117', 'result': 'Accept', 'score': 100.0}, {'suid': '20233115', 'result': 'Accept', 'score': 100.0}, {'suid': '20233090', 'result': 'Accept', 'score': 100.0}, {'suid': '20233071', 'result': 'Accept', 'score': 100.0}, {'suid': '20233122', 'result': 'Accept', 'score': 100.0}, {'suid': '20233121', 'result': 'Accept', 'score': 100.0}, {'suid': '20233109', 'result': 'Accept', 'score': 100.0}, {'suid': '20233160', 'result': 'Wrong Answer', 'score': 0.0}, {'suid': '20233132', 'result': 'Wrong Answer', 'score': 0.0}, {'suid': '20233172', 'result': 'Run-Time Error', 'score': 0.0}], [{'suid': '20233065', 'result': 'Accept', 'score': 100.0}, {'suid': '20233109', 'result': 'Accept', 'score': 100.0}, {'suid': '20233117', 'result': 'Accept', 'score': 100.0}, {'suid': '20233071', 'result': 'Accept', 'score': 100.0}, {'suid': '20233092', 'result': 'Accept', 'score': 100.0}, {'suid': '20233101', 'result': 'Accept', 'score': 100.0}, {'suid': '20233122', 'result': 'Accept', 'score': 100.0}, {'suid': '20233121', 'result': 'Accept', 'score': 100.0}, {'suid': '20233057', 'result': 'Wrong Answer', 'score': 75.0}, {'suid': '20190445', 'result': 'Wrong Answer', 'score': 0.0}, {'suid': '20181771', 'result': 'Wrong Answer', 'score': 0.0}, {'suid': '20233167', 'result': 'Wrong Answer', 'score': 0.0}, {'suid': '20233095', 'result': 'Wrong Answer', 'score': 0.0}]]


#데이터 출력
#print_data.print_data(datalist)



student_data = {}
student_trial = {}

print_data.print_trial(datalist)
trialdata = crawl_data.get_trial_data(student_data, student_trial, datalist)




make_graph.students_each_prob_graph(datalist, course_name, assignment_name)

make_graph.score_distribution_graph(trialdata, course_name, assignment_name)

make_graph.total_score_graph(trialdata, course_name, assignment_name)




