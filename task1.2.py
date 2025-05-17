# task1.py

class Student:
    def __init__(self, name, student_id):
        self.name = name          # сохраняем name в текущем объекте
        self.student_id = student_id  # сохраняем student_id в текущем объекте
        self.grades = []          # создаем пустой список grades для текущего объекта

    def add_grade(self, grade): # Добавляем оценку в список оценок студента
        if 0<=grade<=10: # Проверяем, что оценка находится в допустимом диапазоне (0-10)
            self.grades.append(grade) # Добавляем длпустимую оценку
        else:
            print('Ошибка. Оценка не в диапазоне 0-10') # Если оценка вне диапазона, выводит сообщение об ошибке
            
    def get_average(self): # Вычисляем средний балл студента
        if not self.grades:
            return 0.0 # Если нет оценок, возвращаем 0.0
        return sum(self.grades)/len(self.grades) # Иначе возвращаем среднее арифметическое всех оценок
    
    def display_info(self):
        print(f'Студент: {self.name}')
        print(f'ID: {self.student_id}')
        print(f"Оценки: {', '.join(map(str,self.grades))}") # Список оценок (преобразованный в строку)
        print(f'Средний балл: {self.get_average():.2f}\n') # Средний балл (с округлением до 2 знаков после запятой)
        
if __name__=="__main__":
    student1 = Student("Краснова Полина", "202")
    student1.add_grade(3)
    student1.add_grade(8)
    student1.display_info()
    
    
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
