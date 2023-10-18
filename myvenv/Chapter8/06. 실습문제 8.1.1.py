class Item:
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable

    def sale(self):
        print(f"[{self.name}] 판매가격은 [{self.price}]")

    def discard(self):
        if self.isdropable:
            print(f"[{self.name}] 버렸습니다.")
        else:
            print(f"[{self.name}] 버리지 않았습니다.")

class WearableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect

    def wear(self):
        print(f"[{self.name}]을 착용했습니다. {self.effect}")

class Usable(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect

    def use(self):
        print(f"[{self.name}]을 사용했습니다. {self.effect}")

# 인스턴스 생성
sword = WearableItem("검", 5000, 100, True, "체력 5000 증가 마력 5000 증가")
sword.wear()
sword.sale()
sword.discard()

potion = Usable("물약", 1000, 1, False, "투명효과 300초 지속")
potion.discard()
potion.use()
potion.sale()
