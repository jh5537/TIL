marks = [90, 25, 67, 45, 80]

for number in range(1,(len(marks)+1)):
    if marks[number-1] < 60:
        continue
    print("%d번 학생은 합격입니다. 축하합니다." % number)


