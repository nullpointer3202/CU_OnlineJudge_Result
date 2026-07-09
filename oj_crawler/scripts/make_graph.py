import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

import numpy as np

from scripts.crawl_data import totalscores
mpl.rcParams['axes.unicode_minus'] = False

fontname = fm.FontProperties(fname="./font/malgun.ttf").get_name()
plt.rc('font', family=fontname)


#학생당 문제별 시도와 결과 여부 저장
def students_each_prob_graph(datalist, cname, aname):
    problem_attempt_count = {}
    problem_correct_count = {}

    # 각 HTML 코드의 데이터 리스트를 반복
    for code_index, data_list in enumerate(datalist):
        # 코드 블록별로 딕셔너리 초기화
        problem_attempt_count[code_index] = {}
        problem_correct_count[code_index] = {}

        # 데이터 리스트 내의 각 데이터를 반복
        for data in data_list:
            student_num = data["suid"]

            # 문제를 시도한 학생 수 업데이트
            if student_num in problem_attempt_count[code_index]:
                problem_attempt_count[code_index][student_num] += 1
                if data['result'] == "Accept":
                    problem_correct_count[code_index][student_num] = 1
            else:
                problem_attempt_count[code_index][student_num] = 1
                if data['result'] == "Accept":
                    problem_correct_count[code_index][student_num] = 1

    # 문제 시도 횟수를 오름차순으로 정렬한 딕셔너리 생성
    sorted_problem_counts = sorted(problem_attempt_count.items(), key=lambda x: x[0])
    sorted_correct_counts = sorted(problem_correct_count.items(), key=lambda x: x[0])

    # 문제 인덱스와 학생 수를 따로 리스트로 추출
    problem_indices = [problem_index for problem_index, _ in sorted_problem_counts]
    student_counts = [sum(counts.values()) for _, counts in sorted_problem_counts]

    c_problem_indices = [problem_index for problem_index, _ in sorted_correct_counts]
    correct_counts = [sum(counts.values()) for _, counts in sorted_correct_counts]

    # 각 문제에 대한 학생 수를 나타내는 막대 그래프 생성
    bar = plt.bar(problem_indices, student_counts)
    correct_bar = plt.bar(c_problem_indices, correct_counts, label="Correct Attempts", alpha=0.7)

    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % height, ha='center', va='bottom', size=12)

    for rect in correct_bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % height, ha='center', va='bottom', size=12)

    plt.legend()
    plt.xlabel("문제 번호")
    plt.ylabel("학생 수")
    plt.title(f"{cname} {aname}의 각 문제를 시도한 학생 수")
    plt.show()





def score_distribution_graph(trialdata, cname, aname):
    score_counts = totalscores(trialdata)

    plt.figure(figsize=(10, 6))
    bar = plt.bar(score_counts.keys(), score_counts.values())

    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % height, ha='center', va='bottom', size = 12)

    plt.xlabel("점수")
    plt.ylabel("학생 수")
    plt.title(f"{cname} {aname}의 점수 분포표")

    plt.show()


def total_score_graph(trialdata, cname, aname):

    graphthick = 30  # 그래프의 두께와 세부도. 10~50, 30이 적절
    toppercent = 25  # 그래프의 상위 퍼센트 하이라이트. 25%가 적절
    titleText = f"{cname} {aname} 응시자의 총 점수 분포 (상위 {toppercent}%)"  # 그래프 제목, 한글불가

    total_scores = []
    for data in trialdata:
        total_scores.append(data["총점"])

    # 총 학생 수
    total_students = len(total_scores)

    # 총점 분포도 그래프 그리기
    plt.hist(total_scores, bins=graphthick, edgecolor="black")
    plt.yticks(np.arange(0, 10))
    plt.xlabel("총점")
    plt.ylabel("학생 수")
    plt.title(f"{titleText}")
    plt.text(
        0.05,
        0.95,
        f"학생 수: {total_students}",
        transform=plt.gca().transAxes,
    )

    total_scores_np = np.array(total_scores)
    threshold = np.percentile(total_scores_np, 100 - toppercent)
    plt.axvspan(threshold, np.max(total_scores), color="orange", alpha=0.3)

    plt.show()

#한글폰트 지정


