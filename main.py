print("출력성공")


# name = input("이름을 입력하세요 : ")
# print(f"{name}님, 퀴즈 게임 만들기를  시작합니다.")

choices = ["금융위원회", "금융감독원", "금융통화위원회", "국회"]
print(choices[0])
print(len(choices))

quiz = {"question" : "기준 금리를 정하는 곳은?","answer": 3}
print(quiz["answer"])

choice = 2
if choice == 1:
    print("퀴즈 풀기")
elif choice == 2:
    print("퀴즈 추가")

else:
    print("그 외")

for i in range(4):
    print(i +1, choices[i])

count = 0 
while count < 3:
    print("반복 중", count)
    count = count +1