class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привіт, мене звати {self.name}, мені {self.age} років.")


class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def work(self):
        print(f"{self.name} працює як {self.position}.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} (ID: {self.student_id}) зараз навчається.")


class University:
    def __init__(self):
        self.employees = []
        self.students = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_student(self, student):
        self.students.append(student)

    def remove_employee(self, name):
        self.employees = [emp for emp in self.employees if emp.name != name]

    def remove_student(self, student_id):
        self.students = [stu for stu in self.students if stu.student_id != student_id]

    def find_person(self, identifier):
        for emp in self.employees:
            if emp.name == identifier:
                return f"Знайдено працівника: {emp.name}, посада: {emp.position}"
        for stu in self.students:
            if stu.student_id == identifier:
                return f"Знайдено студента: {stu.name}, ID: {stu.student_id}"
        return "Особа не знайдена."

    def show_info(self):
        print("\nПрацівники університету:")
        for emp in self.employees:
            print(f"{emp.name}, {emp.age} років, посада: {emp.position}")

        print("\nСтуденти університету:")
        for stu in self.students:
            print(f"{stu.name}, {stu.age} років, ID: {stu.student_id}")


def create_employee():
    name = input("Введіть ім'я працівника: ")
    age = int(input("Введіть вік працівника: "))
    position = input("Введіть посаду працівника: ")
    return Employee(name, age, position)


def create_student():
    name = input("Введіть ім'я студента: ")
    age = int(input("Введіть вік студента: "))
    student_id = input("Введіть ID студента: ")
    return Student(name, age, student_id)


university = University()

num_employees = int(input("Скільки працівників додати? "))
for _ in range(num_employees):
    university.add_employee(create_employee())

num_students = int(input("Скільки студентів додати? "))
for _ in range(num_students):
    university.add_student(create_student())

university.show_info()

search_query = input("\nВведіть ім'я працівника або ID студента для пошуку: ")
print(university.find_person(search_query))

delete_choice = input("Бажаєте видалити працівника чи студента? (employee/student/skip): ").strip().lower()
if delete_choice == "employee":
    del_name = input("Введіть ім'я працівника для видалення: ")
    university.remove_employee(del_name)
elif delete_choice == "student":
    del_id = input("Введіть ID студента для видалення: ")
    university.remove_student(del_id)

print("\nОновлена інформація:")
university.show_info()
