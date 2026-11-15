# print("출력성공")


# # name = input("이름을 입력하세요 : ")
# # print(f"{name}님, 퀴즈 게임 만들기를  시작합니다.")

# choices = ["금융위원회", "금융감독원", "금융통화위원회", "국회"]
# print(choices[0])
# print(len(choices))

# quiz = {"question" : "기준 금리를 정하는 곳은?","answer": 3}
# print(quiz["answer"])

# choice = 2
# if choice == 1:
#     print("퀴즈 풀기")
# elif choice == 2:
#     print("퀴즈 추가")

# # else:
# #     print("그 외")

# # for i in range(4):
# #     print(i +1, choices[i])

# # count = 0 
# # while count < 3:
# #     print("반복 중", count)
# #     count = count +1



# def check_an(us_an, co_an):
#     return us_an == co_an

# result = check_an(3,quiz["answer"])
# print(result)

# result = check_an(2,quiz["answer"])
# print(result)

# while True:
#     try:
#         answer = int(input("정답 번호를 입력하세요 (1~4): "))

#         if answer < 1 or answer > 4:
#             print("1~4 사이의 숫자를 입력하세요.")
#             continue

#         if check_an(answer, quiz["answer"]):
#             print("정답입니다!")
#         else:
#             print("오답입니다!")

#         break

#     except ValueError:
#         print("숫자만 입력해야 합니다. 다시 입력하세요.")

# # 숫자 입력을 검사하는 함수
# def read_number(prompt, min_value, max_value):
#     while True:
#         text = input(prompt).strip()

#         # 아무것도 입력하지 않은 경우
#         if text == "":
#             print("입력값이 비어 있습니다.")
#             continue

#         # 숫자가 아닌 경우
#         try:
#             number = int(text)
#         except ValueError:
#             print("숫자만 입력해야 합니다.")
#             continue

#         # 허용 범위를 벗어난 경우
#         if number < min_value or number > max_value:
#             print(f"{min_value}~{max_value} 사이의 숫자를 입력하세요.")
#             continue

#         # 정상적인 숫자라면 반환
#         return number


# # 함수 사용하기
# answer = read_number("정답 번호를 입력하세요: ", 1, 4)

# if check_an(answer, quiz["answer"]):
#     print("정답입니다!")
# else:
#     print("오답입니다!")

# 숫자 입력 검사 함수
def read_number(prompt, min_value, max_value):
    while True:
        text = input(prompt).strip()

        if text == "":
            print("아무것도 입력하지 않았습니다.")
            continue

        try:
            number = int(text)
        except ValueError:
            print("숫자만 입력해야 합니다.")
            continue

        if number < min_value or number > max_value:
            print(f"{min_value}~{max_value} 사이의 숫자를 입력하세요.")
            continue

        return number

# 퀴즈 한 문제를 관리하는 클래스
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 문제와 선택지를 화면에 출력
    def display(self, number):
        print("-" * 40)
        print(f"[문제 {number}]")
        print(self.question)

        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    # 사용자의 답이 정답인지 검사
    def is_correct(self, user_answer):
        return user_answer == self.answer
# 게임 전체를 관리하는 클래스

class QuizGame:
    

    def __init__(self):
        self.quizzes = self.create_default_quizzes()
        self.best_score = None

    # 기본 퀴즈 5개를 만들어서 돌려줌
    def create_default_quizzes(self):
        return [
            Quiz(
                "기준금리를 결정하는 곳은?",
                ["금융위원회", "금융감독원", "금융통화위원회", "국회"],
                3
            ),
            Quiz(
                "PER(주가수익비율)을 구하는 식은?",
                ["주가 ÷ 주당순이익(EPS)", "주가 ÷ 주당순자산(BPS)", "순이익 ÷ 매출액", "부채 ÷ 자기자본"],
                1
            ),
            Quiz(
                "한국 주식시장(코스피·코스닥) 정규장 마감 시간은?",
                ["오후 3시", "오후 3시 30분", "오후 4시", "오후 2시 30분"],
                2
            ),
            Quiz(
                "한국 주식의 하루 가격제한폭(상한가·하한가)은?",
                ["±10%", "±15%", "±30%", "±50%"],
                3
            ),
            Quiz(
                "자기자본 대비 순이익의 비율을 나타내는 지표는?",
                ["PER", "PBR", "EPS", "ROE"],
                4
            ),
        ]

    # 메뉴를 화면에 출력
    def show_menu(self):
        print("=" * 40)
        print("       주식·경제 상식 퀴즈")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    # 게임 실행
    def run(self):
        try:
            while True:
                self.show_menu()

                choice = read_number("선택: ", 1, 5)

                if choice == 1:
                    print("퀴즈 풀기 선택!")

                elif choice == 2:
                    print("퀴즈 추가 선택!")

                elif choice == 3:
                    print("퀴즈 목록 선택!")

                elif choice == 4:
                    print("점수 확인 선택!")

                else:
                    print("게임을 종료합니다.")
                    break

        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되어 안전하게 종료합니다.")


# 프로그램 시작
# 프로그램 시작
if __name__ == "__main__":
    game = QuizGame()
    print(f"기본 퀴즈 {len(game.quizzes)}개를 불러왔습니다.")
    game.run()