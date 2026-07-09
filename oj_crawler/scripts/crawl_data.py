import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.alert import Alert

from selenium.webdriver.chrome.service import Service

##### 데이터 크롤링하는 코드 #####




# 과목 선택
def get_course(driver):
    #과목 리스트 찾기
    myclass_element = driver.find_element(By.CLASS_NAME, "list-group.list-group-bar")

    #각 과목들을 찾는 코드
    courses = myclass_element.find_elements(By.CLASS_NAME, "list-group-item")


    for idx, course in enumerate(courses):
        print(f"[{idx+1}] {course.text}")

    # 데이터를 가져올 과목 선택
    selected_course_idx = int(input("데이터를 가져올 과목 : "))
    selected_course = courses[selected_course_idx-1]
    course_name = selected_course.text
    # 과목 클릭
    selected_course.click()
    return course_name

#과제(실습 or 시험) 선택
def get_assignments(driver):
    assignments = driver.find_elements(
        By.XPATH, "/html/body/div[2]/div/div[1]/div/ul/li[position()>1]"
    )
    for idx, assignment in enumerate(assignments):
        print(f"[{idx+1}] {assignment.text}")
    selected_assignment_idx = int(input("데이터를 가져올 문제유형 : "))
    selected_assignment = assignments[selected_assignment_idx - 1]
    assignment_name = ''.join(selected_assignment.text)
    selected_assignment.click()
    print("선택한 문제유형 : ", assignment_name)
    return assignment_name




# 제출정보 모으기 => get_data에서 사용예정!
def get_submissions(driver, data):
    submissions = driver.find_elements(
        By.XPATH, '//*[@id="result-tab"]/tbody/tr[position()>0]'
    )

    for idx, submission in enumerate(submissions):
        sub_suid = submission.find_element(By.XPATH, ".//td[2]").text

        try:
            sub_result = submission.find_element(By.XPATH, ".//td[4]/btn").text
        except:
            sub_result = submission.find_element(By.XPATH, ".//td[4]").text
        sub_score = submission.find_element(By.XPATH, ".//td[5]").text


        #가져오고 있는 데이터를 출력
        #print(sub_suid, sub_result, sub_score)
        if (
            sub_result == "Empty Test-data"
            or sub_result == "Judging"
            or sub_result == "Compile Error"
        ):
            continue
        write_data(sub_suid, sub_result, float(sub_score.replace(" /100", "")), data)




#각 문제의 제출정보 열기
def get_status(problem, driver):
    problem_name = problem.find_element(By.XPATH, ".//td[2]/a")
    problem_status = problem.find_element(By.XPATH, ".//td[7]/a")
    problem_status.click()

    uid_box = driver.find_element(By.XPATH, '//*[@id="uid"]')
    search_btn = driver.find_element(
        By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/form/input"
    )

    # 학번 박스 내용 삭제
    uid_box.clear()
    search_btn.click()


#제출 정보 내의 모든 데이터를 모으기
def get_data(driver):
    #print("DEBUG : get_data 실행")
    data = []

    try : # 테스트 결과 페이지 수 확인 후 LINK 생성
        pagelist = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div/nav/ul"
        )
    except : # 테스트 횟수가 일정 수를 넘지 않아 페이지 구분이 생기지 않으면 해당 페이지만 실행
        get_submissions(driver, data)
        return data

    pager = pagelist.find_elements(By.XPATH, ".//li[position()>0]")

    # 제출 상태의 마지막 페이지 찾기
    lastpage = pager[-1]
    last_page_num = lastpage.find_element(By.XPATH, ".//a").get_attribute(
        "data-ci-pagination-page"
    )

    #현재 데이터를 수집하고있는 페이지 표시
    print("page ", end= '')


    # 페이지가 끝날 때까지 제출 상태를 출력
    for page in range(1, int(last_page_num) + 1):
        print(f"{page} ", end = '')
        get_submissions(driver, data)  # 데이터 불러오는 함수
        pagelist = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div/nav/ul"
        )
        pager = pagelist.find_elements(By.XPATH, ".//li[position()>0]")

        #페이지가 끝나면 break
        try:
            next = driver.find_element(
                By.XPATH, f".//a[@data-ci-pagination-page='{page+1}']"
            )

            nextpage = next.get_attribute("href")
            #print("페이지 이동!!!! ", nextpage)
            driver.get(nextpage)
        except:
            break
    print()
    return data

#Data 작성 및 수정 : 같은 학번이 있을 경우 대체. => get_submissions에서 사용
def write_data(suid, result, score, data):
    for student in data:
        if student["suid"] == suid:
            if student["score"] < score:
                student["result"] = result
                student["score"] = score
            return
    data.append({"suid": suid, "result": result, "score": score})




#datalist에 저장된 데이터 출력
def print_data(datalist):
    for code_index, data_list in enumerate(datalist):
        print(f"문제 {code_index + 1}에 대한 점수:")
        for i, data in enumerate(data_list):
            print(f"Data {i + 1}:")
            print(f"학번: {data['suid']}")
            print(f"상태: {data['result']}")
            print(f"점수: {data['score']}")
            print()

#학생당 문제별 시도 여부 출력
def print_trial(datalist):
    student_data = {}
    student_trial = {}
    for code_index, data_list in enumerate(datalist):
        for data in data_list:
            student_num = str(data["suid"])
            status = data["result"]
            score = data["score"]

            if student_num in student_data:
                # 기존 학생 번호에 대한 값 업데이트
                student_data[student_num]["count"] += 1
                student_data[student_num]["total_score"] += score

                # 상태가 "Accept"인 경우, 맞은 갯수 업데이트
                if status == "Accept":
                    student_data[student_num]["accept_count"] += 1
            else:
                # student data(딕셔너리 타입)에 학생 번호 추가
                student_data[student_num] = {
                    "count": 1,
                    "accept_count": 1 if status == "Accept" else 0,
                    "total_score": score,
                }

            #시도한 문제들
            if student_num in student_trial:
                student_trial[student_num].append(code_index)
            else:
                student_trial[student_num] = [code_index]

    student_data = dict(sorted(student_data.items(), key=lambda x: x[1]["total_score"], reverse=True))



    #print("AFTER", student_data)
    calc = 0
    for student_num, data in student_data.items():
        calc += 1
        print(calc)
        print(f"학번: {student_num}")
        print(f"맞은 갯수: {data['accept_count']}")
        print(f"총점: {data['total_score']}")

        # 학생이 시도한 문제 출력
        print("시도한 문제들:")
        for code_index in student_trial[student_num]:
            print(f"  문제 {code_index+1}")

        print()

#학생당 문제별 시도 여부 저장
def get_trial_data(student_data, student_trial, datalist):
    for code_index, data_list in enumerate(datalist):
        for data in data_list:
            student_num = str(data["suid"])
            status = data["result"]
            score = data["score"]

            if student_num in student_data:
                # 기존 학생 번호에 대한 값 업데이트
                student_data[student_num]["count"] += 1
                student_data[student_num]["total_score"] += score

                # 상태가 "Accept"인 경우, 개수 업데이트
                if status == "Accept":
                    student_data[student_num]["accept_count"] += 1
            else:
                # 딕셔너리에 학생 번호를 위한 새로운 항목 추가
                student_data[student_num] = {
                    "count": 1,
                    "accept_count": 1 if status == "Accept" else 0,
                    "total_score": score,
                }

            if student_num in student_trial:
                student_trial[student_num].append(code_index)
            else:
                student_trial[student_num] = [code_index]

    tdata = []
    for student_num, data in student_data.items():
        student = {}
        student["학번"] = student_num
        student["맞은 갯수"] = data["accept_count"]
        student["총점"] = data["total_score"]

        student["시도한 문제들"] = []
        for code_index in student_trial[student_num]:
            student["시도한 문제들"].append(f"문제 {code_index+1}")

        tdata.append(student)
    return tdata

#
def totalscores(trialdata):
    score_counts = {}
    for data in trialdata:
        score = data["총점"]
        if score in score_counts:
            score_counts[score] += 1
        else:
            score_counts[score] = 1
    return score_counts
