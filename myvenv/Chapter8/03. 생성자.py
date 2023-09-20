# 생성자
# : 인스턴스를 만들 때 호출되는 메서드
# 인스턴스 : 프로젝트 동작 시 객체가 만들어지는 시점의 객체

class Monster:
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed
    def decrease_health(self, num):
        self.health -= num
    def get_heath(self):
        return self.health

# 고블린 인스턴스 생성
goblin = Monster(800, 120, 300)

goblin.decrease_health(100)
print(goblin.get_heath())

# 늑대 인스턴스 생성
wolf = Monster(1500, 200, 350)
wolf.decrease_health(200)
print(wolf.get_heath())