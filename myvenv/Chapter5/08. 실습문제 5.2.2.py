# 실습문제 5.2.2

result = []

day1 = int(input("1일차 턱걸이 횟수 >>>"))
result.append(day1)
day2 = int(input("2일차 턱걸이 횟수 >>>"))
result.append(day2)
day3 = int(input("3일차 턱걸이 횟수 >>>"))
result.append(day3)
day4 = int(input("4일차 턱걸이 횟수 >>>"))
result.append(day4)
day5 = int(input("5일차 턱걸이 횟수 >>>"))
result.append(day5)
day6 = int(input("6일차 턱걸이 횟수 >>>"))
result.append(day6)
day7 = int(input("7일차 턱걸이 횟수 >>>"))
result.append(day7)

avg = (result[0] + result[1] + result[2] + result[3] + result[4] + result[5] + result[6]) / 7

print(int(avg))