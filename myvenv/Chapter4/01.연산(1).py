# 1. 대입 연산
# 변수이름 = 데이터

# 2. 산술 연산
# - 숫자 연산
x = 5
y = 2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y) # 몫
print(x % y) # 나머지
print(x ** y) # 제곱

# - 문자열 연산
tag1 = "#내꺼"
tag2 = "#오늘부터"
tag3 = "1일"

tag = tag1 + tag2 + tag3
print(tag)

message = "우리 모두 파이썬 사랑합니다.\n" * 5
print(message)

# 복합 할당 연산자
level = 10 #(레벨 1 증가)
level += 1 #level = level + 1

health = 2000
health -= 300 # health = health - 300

attack = 300
attack *= 1.5 # attack = attack * 1.5

speed = 420
speed /= 2 # speed = speed / 2

print(level, health, attack, speed)