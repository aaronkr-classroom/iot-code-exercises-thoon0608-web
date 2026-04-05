# 테스트를 위해 임의의 month와 day를 지정합니다.
month = 8
day = 15

if month == 8 and day == 15:
    print("광복절")
elif (month % 2 != 0 and day == 15) or (month % 2 == 0 and day == 16):
    print("그날")
else:
    print("평일")