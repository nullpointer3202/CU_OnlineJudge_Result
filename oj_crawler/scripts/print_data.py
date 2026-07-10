





#datalist에 저장된 데이터를 보기 편한 방식으로 출력
def print_data(datalist):
    for code_index, data_list in enumerate(datalist):
        print(f"문제 {code_index + 1}에 대한 점수:")
        for i, data in enumerate(data_list):
            print(f"Data {i + 1}:")
            print(f"아이디: {data['suid']}")
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
                # 딕셔너리에 학생 번호 추가
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
        print(f"아이디: {student_num}")
        print(f"맞은 갯수: {data['accept_count']}")
        print(f"총점: {data['total_score']}")

        # 학생이 시도한 문제 출력
        print("시도한 문제들:")
        for code_index in student_trial[student_num]:
            print(f"  문제 {code_index+1}")

        print()
