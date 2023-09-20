# 실습문제 5.3.3
# Learnig Korean

#한국어 리스트
word_list = ["사랑해", "고마워", "행복해", "귀엽다"]

print("Let's start korean")
for word in word_list:
    print(word)
    data = input()

    if word != data:
        break

# 전체 문제 개수: x 개
# 맞힌 문제 개수 : y 개
# 틀린 문제 개수 : z 개