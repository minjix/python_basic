# 원화를 입력, 환율 입력 -> 달러값 출력

won = input("원화금액을 입력하세요>>>")
dollar = input("환율을 입력하세요>>>")

try: #예외가 발생할 수 있는 코드
    print(int(won)/int(dollar))
except ValueError as e: #예외가 발생했을 떄 실행 코드
    print("문자열 예외발생", e)
except ZeroDivisionError as e:
    print("나누기 0은 불가능", e)
else: #예외가 발생하지 않았을 때 실행
    print("예외가 발생하지 않았을 떄 실행")
finally: # 파일 닫기
    print("예외 발생여부와 관계없이 항상 실행")

print("exit")