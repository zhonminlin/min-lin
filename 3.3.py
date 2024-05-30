total_students = 0
pass_count = 0
fail_count = 0
total_score = 0

while True:
    score = int(input("請輸入學生成績（輸入 -1 表示結束）："))
    
    if score == -1:
        break
    
    if score < 0 or score > 100:
        print("請輸入有效成績（0-100之間）")
        continue
    
    total_students += 1
    total_score += score
    if score >= 60:
        pass_count += 1
    else:
        fail_count += 1

print("全班人數：", total_students)
print("及格人數：", pass_count)
print("不及格人數：", fail_count)
if total_students > 0:
    average_score = total_score / total_students
    print("全班平均值：", average_score)
else:
    print("無學生成績")
