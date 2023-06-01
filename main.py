#4 part 2

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} видає звук: {self.sound}")

animal1 = Animal("Котяра", "Мяу")
animal1.make_sound()

animal2 = Animal("Собака", "Гав")
animal2.make_sound()

animal3 = Animal("Глеб", "Дайте кристалик")
animal3.make_sound()
