# 1번
print("---------- 1번 --------------------")
# 예측
print("==예측")
print("[(0, 'apple'), (1, 'banana'), (2, 'grape')]")
print("정답 3번")
# 결과
print("==결과")
mylist = ['apple' ,'banana', 'grape']
result = list(enumerate(mylist))
print(result)

# 2번
print("---------- 2번 --------------------")
# 예측
print("==예측")
print("{'my': 5, 'cat': 6, 'has': 2, 'blue': 3, 'eyes,': 4, 'is': 7, 'cute': 8}")
print("정답 4번")
# 결과
print("==결과")
cat_song = "my cat has blue eyes, my cat is cute"
print({i:j for j,i in enumerate(cat_song.split())}) # i에 밸류, j에 인덱스를 부여하여 딕셔너리 생성.
# 딕셔너리는 중복을 허용하지 않음. 중복이 발생할 시, 최신값으로 이전 요소를 덮어씀. 따라서 my와 cat에 부여되었던 0과 1 인덱스는 지워지고,
# 새로 5와 6을 부여하여 딕셔너리 생성.

# 3번
print("---------- 3번 --------------------")
# 예측
print("==예측")
print("orange&pink&brown&black&white")
# 결과
print("==결과")
colors = ['orange', 'pink', 'brown', 'black', 'white']
result = '&'.join(colors) # 리스트 요소를 합쳐 문자열로 반환하되, 요소 사이에 &을 삽입.
print(result)

# 4번
print("---------- 4번 --------------------")
# 예측
print("==예측")
print("{'students': 0, 'superuser': 1, 'professor': 2, 'employee': 3}")
# 결과
print("==결과")
user_dict = {}
user_list = ["students", "superuser", "professor", "employee"]
for value_1, value_2 in enumerate(user_list):
    user_dict[value_2] = value_1
print(user_dict)

# 5번
print("---------- 5번 --------------------")
# 예측
print("==예측")
print("[0, 2, 4, 6, 8]")
print("[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")
print("['zero', 'one', 'two', 'three']")
print("cs50")
# 결과
print("==결과")
result = [i for i in range(10) if i%2 == 0]
print(result)
items = 'zero one two three'.split("two")
result =[i for i in range(10)]
print(result)
items = 'zero one two three'.split()
print(items)
example = 'cs50.gachon.edu'
subdomain, domain, tId = example.split('.')
print(subdomain)

# 6번
print("---------- 6번 --------------------")
# 예측
print("==예측")
print("['Cat', 'Panda', 'Owl']")
# 결과
print("==결과")
animal = ['Fox', 'Dog', 'Cat', 'Monkey', 'Horse', 'Panda', 'Owl'] # 대소문자 구분에 유의. Owl 에는 o가 포함되지 않음.
print([ani for ani in animal if 'o' not in ani])

# 7번
print("---------- 7번 --------------------")
# 예측
print("==예측")
print("DongUniversity")
# 결과
print("==결과")
name = "Hanbit University"
student = ["Hong", "Gil", "Dong"]
split_name = name.split()
join_student = ''.join(student)
print(join_student[-4:] + split_name[1])

# 8번
print("---------- 8번 --------------------")
# 예측
print("==예측")
print(20)
# 결과
print("==결과")
kor_score = [49, 79, 20, 100, 80]
math_score = [42, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]
print(midterm_score[0][2])

# 9번
print("---------- 9번 --------------------")
# 예측
print("==예측")
print("[[12, 3], [15, 3]]")
print("정답 2번")
# 결과
print("==결과")
a = [1, 2, 3]
b = [4, 5, ]
c = [7, 8, 9]
print([[sum(k), len(k)] for k in zip(a, b, c)])

# 10번
print("---------- 10번 --------------------")
# 예측
print("==예측")
print("yellow")
# 결과
print("==결과")
week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
list_data = [week, rainbow]
print(list_data[1][2])

# 11번
print("---------- 11번 --------------------")
# 예측
print("==예측")
print("score: 72")
# 결과
print("==결과")
kor_score = [30, 79, 20, 100, 80]
math_score = [43, 59, 0, 30, 90]
eng_score = [49, 72, 48, 67, 15]
midterm_score = [kor_score, math_score, eng_score]
print("score:", midterm_score[2][1])

# 12번
print("---------- 12번 --------------------")
# 예측
print("==예측")
print("['a', '2', 'error']")
# 결과
print("==결과")
alist = ["a", "b", "c"]
blist = ["1", "2", "3"]
abcd= []
for a, b in enumerate(zip(alist, blist)): # 0, ('a', 1) / 1, ('b', 2) / 2, ('c', 3)
    try: # try/except 구문: try에 해당하는 명령을 처리하되, 예외상황에서만 except를 처리함.
        abcd.append(b[a]) # 값의 자료형은 전부 문자형
    except IndexError: # 에러 발생시 처리 명령을 바꿈.
        abcd.append("error")
print(abcd)

# 13번
print("---------- 13번 --------------------")
# 예측
print("==예측")
print("빈칸에 들어갈 함수는 'zip'이다.")
# 결과
print("==결과")
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
    print(a, b)

# 14번
print("---------- 14번 --------------------")
# 예측
print("==예측")
print("80")
# 결과
print("==결과")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
nums = [i for i in range(20)]
answer = [alpha+str(num) for alpha in alphabet for num in nums if num%2==0] # 8회 / 10회
print(len(answer))