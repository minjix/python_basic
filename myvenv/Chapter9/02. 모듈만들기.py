import py_module

# 변수 사용
print(py_module.version)

# 함수 사용
py_module.printAuthor()

# 클래스 사용
pay_info = py_module.Pay("AA", 10000, "2023-10-18")
print(pay_info.get_pay_info())

print(py_module.__name__)