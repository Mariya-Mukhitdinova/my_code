# class Animal:
#     def __init__(self, skin):
#         self.skin = skin
#     def make_sound(self,sound):
#         print(sound)
# class Fish(Animal):
#     def make_sound(self, sound):
#         pass
# class Hourse(Animal):
#     def __init__(self, skin, fur):
#         super().__init__(skin)
#         self.fur = fur
#     def skachka(self):
#         print("лошадь скачет")
#
# class Cat(Animal):
#     def murchat(self):
#         print("кошка мурчит")
#
# busefal = Hourse()
# tom = Cat()
#
# sushestvo = Animal(skin="прозрачная")
# nemo = Fish(skin="прозрачная")
# busefal.make_sound("hhhjn")
# busefal.skachka()
# tom.murchat()
# tom.make_sound("мяу")
# sushestvo.make_sound("jjbjbjv")


class Animal:
    def __init__(self, skin, lapi):
        self.skin = skin
        self.lapi = lapi
    def make_sound(self,sound):
        print(sound)

class Aqua_animal:
    def __init__(self, cheshuya):
        self.cheshuya = cheshuya



