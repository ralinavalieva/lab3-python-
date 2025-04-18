# task1.py

class Student:
    def __init__(self, name, student_id):
        """
        инициализация студента.
        
        :param name: Имя студента
        :param student_id: ID студента
        """
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        """
        добавляет оценку с валидацией (0-10).
        
        :param grade: оценка для добавления
        """
        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            raise ValueError("оценка должна быть в диапазоне от 0 до 10.")

    def get_average(self):
        """
        возвращает средний балл.
        
        :return: средний балл
        """
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def display_info(self):
        """
        выводит информацию о студенте.
        """
        print(f"имя: {self.name}, ID: {self.student_id}, оценки: {self.grades}, средний балл: {self.get_average():.2f}")

    def __str__(self):
        return f"студент {self.name} (ID: {self.student_id})"

    def __eq__(self, other):
        return self.student_id == other.student_id

    def __len__(self):
        return len(self.grades)


if __name__ == "__main__":
    student = Student("Иван Иванов", "12345")
    student.add_grade(8)
    student.add_grade(9)
    student.display_info()
    
    
# task2.py

class Person:
    def __init__(self, name, age):
        """
        инициализация человека.
        
        :param name: имя человека
        :param age: возраст человека
        """
        self.name = name
        self.age = age


class Teacher(Person):
    def __init__(self, name, age, subject):
        """
        инициализация преподавателя.
        
        :param name: имя преподавателя
        :param age: возраст преподавателя
        :param subject: преподаваемый предмет
        """
        super().__init__(name, age)
        self.subject = subject
        self.students = []

    def add_student(self, student):
        """добавляет студента в список."""
        self.students.append(student)

    def remove_student(self, student):
        """удаляет студента из списка."""
        self.students.remove(student)

    def list_students(self):
        """выводит список студентов."""
        for student in self.students:
            print(student)


if __name__ == "__main__":
    teacher = Teacher("Анна Петрова", 35, "математика")
    student1 = Student("Иван Иванов", "12345")
    student2 = Student("Мария Смирнова", "67890")

    teacher.add_student(student1)
    teacher.add_student(student2)
    
    print(f"преподаватель {teacher.name} ведет предмет {teacher.subject}. студенты:")
    teacher.list_students()