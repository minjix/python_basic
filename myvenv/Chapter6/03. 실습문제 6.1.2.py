# 실습문제 6.1.2
# docstring : 설명문  ex)"""함수 섦명"""

# 문자열 포맷팅
def printSumAvg(x, y, z):
    """두 수의 합계화 평균을 반환하는 함수"""
    sum = x + y + z
    avg = sum / 3
    print(f"합계 : {sum}  평균: {avg}")

printSumAvg(10, 20, 30)