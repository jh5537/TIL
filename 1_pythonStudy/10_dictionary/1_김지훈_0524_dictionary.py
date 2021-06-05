students = [
   {"name" : "홍길동", "korean" : 87, "math" : 98, "english" : 88, "science" : 95},
   {"name" : "이몽룡", "korean" : 92, "math" : 98, "english" : 96, "science" : 98},
   {"name" : "성춘향", "korean" : 76, "math" : 96, "english" : 94, "science" : 90},
   {"name" : "변학도", "korean" : 98, "math" : 92, "english" : 96, "science" : 92},
   {"name" : "박지성", "korean" : 95, "math" : 98, "english" : 98, "science" : 98},
   {"name" : "류현진", "korean" : 64, "math" : 88, "english" : 92, "science" : 92}]
print("1번")
print("이름   총점    평균")
for k in students:
   sum = avg = 0
   sum = int(k["korean"]) + int(k["english"]) + int(k["science"])
   avg = sum/3
   print("%s %4d %7.2f" % (k['name'], sum, avg))

print("==============================")
print("2번")
dic = {}
while True:
   voc = input("영어 단어 등록 (종료는 quit) : ")
   if voc != "quit":
      if voc in dic:
          print("%s는 이미 등록된 단어입니다." % voc)
          print()
          continue
      else:
          mean = input("%s의 뜻 입력 (종료는 quit) : " % voc)
          print()
          if mean != "quit":
            dic[voc] = mean
          else:
             break
   else:
      print()
      break
while True:
   sear = input("검색할 단어 입력 (종료는 quit) : ")
   if sear != "quit":
      if sear in dic:
         print("%s의 뜻은 %s입니다." % (sear,dic[sear]))
         print()
         continue
      else:
         print("%s는 사전에 없는 단어입니다." % sear)
         print()
         continue
   else:
      print()
      print("종료합니다.")
      break