# 실습문제 5.3.4
# Learnig Korean

#한국어 리스트
word_list = ["사랑해", "고마워", "행복해", "귀엽다"]
#success = []
#fail = []

# 점수
score = 0

print("Let's start korean")
for word in word_list:
    print(word)
    data = input()

    #if word != data:
    #    fail.append(data)
    #elif word == data:
    #    success.append(data)

    if data == word: # 문제를 맞힌 경우
        score += 1 # 점수를 1씩 증가
        
print("전체 문제 개수: ", len(word_list), "개")
#print("맞힌 문제 개수: ", len(success), "개")
#print("틀린 문제 개수: ", len(fail), "개")
print("맞힌 문제 개수: ", score, "개")
print("틀린 문제 개수: ", len(word_list) - score, "개")