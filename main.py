#1 part 2

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print("Ім'я студента:", self.name)
        print("Вік студента:", self.age)

student1 = Student("Дімончик", 14)
student1.get_info()

student2 = Student("Вовчик", 14)
student2.get_info()
student3 = Student("Максим", 16)
student3.get_info()