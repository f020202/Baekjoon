lines = []
point = 0
grade = 0
total_grade = 0
total_point = 0
grade_to_point = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

try:
    while True:
        line = input()
        if not line:  # 입력이 빈 문자열인 경우 종료
            break
        lines.append(line)
except EOFError:
    pass

for line in lines:
    line = line.split()
    if line[2] != "P":
        point = float(line[1])
        grade = float(grade_to_point[line[2]])
        total_grade += point * grade
        total_point += point
    else:
        continue

print(total_grade / total_point)