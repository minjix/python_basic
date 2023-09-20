# 딕셔너리
# : 사전 형태의 자료형

# 딕셔너리 만들기
stock_a = {"삼성전자":82000, "LG전자": 150000}

stock_b = {
    "삼성전자": [81000, 81500, 83000, 78000, 82000],
    "LG전자": (151000, 151500, 152000, 152500, 151500)
}

stock_c = {
    "삼성전자" : {
        "현재가": 82000,
        "보유수량": 5,
        "매수단가": 81000
    }
}# 중첩 딕셔너리

#print(stock_a)
#print(stock_b)
#print(stock_c)

# 딕셔너리 접근하기
print(stock_a["삼성전자"])
print(stock_c["삼성전자"]["보유수량"])

# 딕셔너리 할당하기
stock_a["삼성전자"] = 85000
print(stock_a)

# 딕셔너리 삭제하기
del stock_a["LG전자"]
print(stock_a)

# 딕셔너리 함수
stock_d = {
    "삼성전자": 82000, 
    "SK하이닉스":123000, 
    "네이버": 370000, 
    "카카오": 150000
}

# items() : 키와 데이터 쌍
for item in stock_d.items():
     #print(item)
     print(item[0]) # 키 값만 출력
     print(item[1]) # 데이터 값만 출력

# keys() : 키
for key in stock_d.keys():
    print(key)

# values() : 데이터
for value in stock_d.values():
    print(value)
