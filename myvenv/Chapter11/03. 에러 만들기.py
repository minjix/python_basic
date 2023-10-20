class PositiveNumberError(Exception):
    def __init__(self):
        super().__init__("양수 입력 불가능")
try:
    num = int(input("음수 입력>>>"))
    if num >= 0:
        raise PositiveNumberError
except PositiveNumberError as e:
    print("에러발생", e)
