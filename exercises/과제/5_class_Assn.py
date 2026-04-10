class SayDays:
    def __init__(self, year, month, day):
        self.y = year
        self.m = month
        self.d = day

    # 윤년 판별
    def is_leap(self):
        return (self.y % 4 == 0 and self.y % 100 != 0) or (self.y % 400 == 0)

    # 각 달의 일수
    def month_days(self):
        mdays = [31, 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]
        if self.is_leap():
            mdays[1] = 29
        return mdays

    # 올해 1월 1일부터 며칠째인지
    def days(self):
        mdays = self.month_days()
        total = 0
        for i in range(self.m - 1):
            total += mdays[i]
        total += self.d
        return total

    # 올해 12월 31일까지 남은 일수
    def days_left(self):
        total_days = 366 if self.is_leap() else 365
        return total_days - self.days()

    # 요일 계산 (Zeller 공식 변형)
    def week(self):
        y = self.y
        m = self.m
        d = self.d

        if m < 3:
            m += 12
            y -= 1

        K = y % 100
        J = y // 100

        h = (d + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7

        # 0=토요일 → 문제 조건 맞춤
        return h

    # 요일 한글 출력
    def week_name(self):
        names = ["토", "일", "월", "화", "수", "목", "금"]
        return names[self.weekday()]


# -------------------------------
# 실행 코드
# -------------------------------

while True:
    try:
        data = input("날짜 입력 (YYYY MM DD): ")
        y, m, d = map(int, data.split())

        s = SayDays(y, m, d)

        print("올해 몇 번째 날:", s.days())
        print("남은 일수:", s.days_left())
        print("요일(숫자):", s.week())
        print("요일(한글):", s.week_name())
        print()

    except:
        print("입력 오류! 다시 입력하세요.\n")