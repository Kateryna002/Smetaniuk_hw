class Student:
    def __init__(self, first_name, last_name, age, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gpa = gpa

    def display_info(self):
        print(f"Студент: {self.first_name} {self.last_name}, Вік: {self.age}, Середній бал: {self.gpa}")

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa
        print(f"Середній бал {self.first_name} {self.last_name} оновлено до: {self.gpa}")


student1 = Student("Катерина", "Сметанюк", 23, 4.2)

student1.display_info()

student1.update_gpa(4.8)
student1.display_info()
