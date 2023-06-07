class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

# оценки лекторам за лекции
    def rate_lector(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
# Средняя оценка домашнее задание по студенту   
    def av_grade(self):
        a = 0
        b = 0
        for course in self.grades.values():
            a += sum(course)
            b += len(course)
            # print(f'СУММА ОЦЕНОК ДЗ КУРСОВ =',a,'\n количество оценок =',b,'\n__________________________')
        return round(a / b, 2)
# Средняя оценка за лекции
    def av_grade_course(self, course):
        a = 0
        b = 0
        for lection in self.grades.keys():
            if lection == course:
                a += sum(self.grades[course])
                b += len(self.grades[course])
        return round(a / b, 3)
# Задание № 3. Полиморфизм и магические методы перегрузка магического метода для вывода по указанному формату
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
# Задание №3 2. Реализуйте возможность сравнивать между собой (студентов, лекторов) по средней оценке.
    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Внимание! Учеников не сравнивают с учителями")
            return
        return self.av_grade() < other.av_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def av_grade(self):
        a = 0
        b = 0
        for course in self.grades.values():
            a += sum(course)
            b += len(course)
        return round(a / b, 3)
# Средняя оценка за лекции
    def av_grade_course(self, course):
        a = 0
        b = 0
        for lesson in self.grades.keys():
            if lesson == course:
               a += sum(self.grades[course])
               b += len(self.grades[course])
        return round(a / b, 1)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_grade()}"
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Преподователей и студентов не сравнивают!")
            return
        return self.av_grade() < other.av_grade()      

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname}')

# Задание №4 Задание № 4. Полевые испытания
# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:
student1 = Student('Иван','Студент 1','мужской')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Git']

student2 = Student('Светлана','Студент 2', 'женский')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Git']

lecturer1 = Lecturer('Олег Петрович','Петров')
lecturer1.courses_attached += ['Python']
 
lecturer2 = Lecturer('Сергей Степанович','Сидоров')
lecturer2.courses_attached += ['Python']

reviewer1 = Reviewer('Владимир Владимирович','Проверочкин 1')
reviewer1.courses_attached += ['Git']
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Степан Петрович','Проверочкин 2')
reviewer2.courses_attached += ['Python']

# Оценки 
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student1, 'Git', 9)
reviewer1.rate_hw(student1, 'Git', 9)

reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Git', 10)
reviewer2.rate_hw(student2, 'Git', 10)

student1.rate_lector(lecturer1, 'Python', 10)
student1.rate_lector(lecturer1, 'Python', 10)
student1.rate_lector(lecturer1, 'Python', 10)
student1.rate_lector(lecturer1, 'Git', 10)

student2.rate_lector(lecturer2, 'Python', 10)
student2.rate_lector(lecturer2, 'Python', 10)
student2.rate_lector(lecturer2, 'Python', 9)
student2.rate_lector(lecturer2, 'Git', 10)

student_list = [student1, student2]
lecturer_list = [lecturer1, lecturer2]
reviewer_list = [reviewer1, reviewer2]

def average_rating_student(course, student_list):
    a = 0
    b = 0
    for stud in student_list:
        for course in stud.grades:
            a += stud.av_grade_course(course)
            b += 1
    return round(a / b, 2)
def average_rating_lector(course, lector_list):
    a = 0
    b = 0
    for lectr in lecturer_list:
        for course in lectr.grades:
            a += lectr.av_grade_course(course)
            b += 1
    return round(a / b, 2)

print('********************************************************************')
print('* Задание № 3. Полиморфизм и магические методы 1. вывод по формату *')
print('********************************************************************')
print(reviewer1,'\n',reviewer2)
print('_________________________________________')
print(lecturer1,'\n',lecturer2)
print('_________________________________________')
print(student1,'\n',student2)
print('_________________________________________')
print('Сравнение по средним оценкам:')
print('student1 < student2 ',student1 < student2)
print('lecturer1 < lecturer2 ',lecturer1 < lecturer2)
print('student1 < lecturer1 ', student1 < lecturer1)
print('student2 < lecturer2 ', student2 < lecturer2)
print('________________________________________')
print('Задание №4 подсчет средней оценки студентов и лекторов \nПодсчет средней оценки за домашние задания')
print(average_rating_student('Python', student_list))
print('подсчет средней оценки за лекции')
print(average_rating_lector('Python', lecturer_list))
print('________________________________________')
