# with 구문을 사용하면 자동으로 file close
with open("./myvenv/Chapter10/data.txt", "r") as file:
    data = file.read()
    print(data)