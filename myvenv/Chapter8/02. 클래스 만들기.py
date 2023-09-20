class Monster:
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed
    def decrease_health(self, num):
        self.health -= num
    def get_heath(self):
        return self.health
    def say(self):
        print("I'm, monster")

goblin = Monster()
goblin.say()

# 파이썬에서는 자료형도 클래스다
a = 10
b = "문자열"
c = True

print(type(a))
print(type(b))
print(type(c))

print(b.__dir__()) # 문자열 안에 있는 메서드들 호출