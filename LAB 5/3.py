class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, new_name):
        self.name = new_name

class Student(Human):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

def get_student_info():
    name = input("Введіть ім'я студента: ")
    age = int(input("Введіть вік студента: "))
    university = input("Введіть назву університету: ")
    return Student(name, age, university)

if __name__ == "__main__":
    student = get_student_info()

    while True:
        print("\nМеню:")
        print("1. Додати оцінку")
        print("2. Порахувати середню оцінку")
        print("3. Змінити ім'я")
        print("4. Вийти")
        choice = input("Ваш вибір: ")

        if choice == "1":
            grade = float(input("Введіть оцінку: "))
            student.add_grade(grade)
            print("Оцінку додано!")
        elif choice == "2":
            print(f"Середня оцінка: {student.average_grade():.2f}")
        elif choice == "3":
            new_name = input("Введіть нове ім'я: ")
            student.change_name(new_name)
            print(f"Ім'я змінено на {student.name}")
        elif choice == "4":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")
