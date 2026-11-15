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


# ==================================================
# 여기부터 실제 프로그램 코드
# ==================================================

import json   # 파이썬 기본 제공 모듈: dict/list <-> JSON 파일 변환
import os     # 파이썬 기본 제공 모듈: 파일 경로 다루기

# state.json을 main.py와 같은 폴더(프로젝트 루트)에 만들기 위한 경로
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(BASE_DIR, "state.json")


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


# 글자 입력 검사 함수 (빈 입력을 막음)
def read_text(prompt):
    while True:
        text = input(prompt).strip()

        if text == "":
            print("빈칸은 입력할 수 없습니다. 다시 입력하세요.")
            continue

        return text


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

    # JSON 파일에 저장할 수 있도록 dict로 바꿔서 돌려줌
    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }


# 게임 전체를 관리하는 클래스
class QuizGame:

    def __init__(self):
        self.quizzes = []
        self.best_score = None
        self.load_data()

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

    # 기본 데이터로 되돌림 (첫 실행 / 파일 손상 시 사용)
    def reset_to_default(self):
        self.quizzes = self.create_default_quizzes()
        self.best_score = None

    # state.json에서 퀴즈와 최고 점수를 불러옴
    def load_data(self):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            quizzes = []
            for item in data["quizzes"]:
                if len(item["choices"]) != 4 or item["answer"] not in [1, 2, 3, 4]:
                    raise ValueError("퀴즈 형식이 올바르지 않습니다.")
                quizzes.append(Quiz(item["question"], item["choices"], item["answer"]))

            self.quizzes = quizzes
            self.best_score = data["best_score"]

            if self.best_score is None:
                score_text = "기록 없음"
            else:
                score_text = f"{self.best_score}점"
            print(f"저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고 점수 {score_text})")

        except FileNotFoundError:
            print("저장된 파일이 없어 기본 퀴즈로 시작합니다.")
            self.reset_to_default()
            self.save_data()

        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            self.reset_to_default()
            self.save_data()

        except OSError:
            print("파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            self.reset_to_default()

    # 퀴즈와 최고 점수를 state.json에 저장
    def save_data(self):
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
        }

        try:
            with open(STATE_FILE, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except OSError:
            print("파일 저장 중 오류가 발생했습니다.")

    # 퀴즈 풀기
    def play_quiz(self):
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.")
            return

        total = len(self.quizzes)
        correct_count = 0

        print(f"\n퀴즈를 시작합니다! (총 {total}문제)")

        for number, quiz in enumerate(self.quizzes, start=1):
            quiz.display(number)
            user_answer = read_number("정답 입력: ", 1, 4)

            if quiz.is_correct(user_answer):
                print("정답입니다!")
                correct_count += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        score = int(correct_count / total * 100)
        print("=" * 40)
        print(f"결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")
        self.update_best_score(score)
        print("=" * 40)

    # 최고 점수와 비교해서 더 높으면 갱신하고 저장
    def update_best_score(self, score):
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")
            self.save_data()

    # 최고 점수 확인
    def show_score(self):
        if self.best_score is None:
            print("아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"최고 점수: {self.best_score}점")

    # 퀴즈 목록 보기
    def show_quiz_list(self):
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"\n등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")

        print("-" * 40)

    # 퀴즈 추가
    def add_quiz(self):
        print("\n새로운 퀴즈를 추가합니다.")

        question = read_text("문제를 입력하세요: ")

        choices = []
        for i in range(1, 5):
            choice = read_text(f"선택지 {i}: ")
            choices.append(choice)

        answer = read_number("정답 번호 (1-4): ", 1, 4)

        self.quizzes.append(Quiz(question, choices, answer))
        self.save_data()
        print("퀴즈가 추가되었습니다!")

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
                    self.play_quiz()

                elif choice == 2:
                    self.add_quiz()

                elif choice == 3:
                    self.show_quiz_list()

                elif choice == 4:
                    self.show_score()

                else:
                    self.save_data()
                    print("데이터를 저장하고 게임을 종료합니다.")
                    break

        except (KeyboardInterrupt, EOFError):
            self.save_data()
            print("\n입력이 중단되어 데이터를 저장하고 안전하게 종료합니다.")


# 프로그램 시작
if __name__ == "__main__":
    game = QuizGame()
    game.run()
