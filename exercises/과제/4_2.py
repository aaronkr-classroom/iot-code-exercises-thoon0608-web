total = 0

for i in range(1, 51):
    # 짝수(2로 나눈 나머지가 0)이면서 3의 배수가 아닌(3으로 나눈 나머지가 0이 아닌) 경우
    if i % 2 == 0 and i % 3 != 0:
        total += i

print(f"합계: {total}")