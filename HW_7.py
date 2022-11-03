class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя лектора: {self.name}.\nФамилия летора: {self.surname}\nЧитаемые курсы: {self.courses_attached}"

    def add_courses(self, course_name):
        self.courses_attached.append(course_name)


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade_lec(self):
        sum_grades = 0
        number = 0
        for v in self.grades.values():
            sum_grades += sum(v)
            number += len(v)
        average_grade_lecture = round(sum_grades / number, 2)
        return average_grade_lecture

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade_lec() == other.average_grade_lec()
        else:
            return f"Ошибка. Сравниваются объекты разного класса."

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            if self.__eq__(other) is False:
                return True
        else:
            return f"Ошибка. Сравниваются объекты разного класса."

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade_lec() <= other.average_grade_lec()
        else:
            return f"Ошибка. Сравниваются объекты разного класса."

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade_lec() < other.average_grade_lec()
        else:
            return f"Ошибка. Сравниваются объекты разного класса."

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            if self.__lt__(other) is False:
                return True
        else:
            return f"Ошибка. Сравниваются объекты разного класса."

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            if self.__le__(other) is False:
                return True
        else:
            return f"Ошибка. Сравниваются объекты разного класса."

    def __str__(self):
        return f"{super().__str__()}\nСредняя оценка за лекции:{self.average_grade_lec()}"


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка. Или студент не изучает этот курс. Или аспирант не ведет занятия на этом курсе.')


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

    def rate_lecture(self, lecturer, course, mark):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and  \
                course in (self.courses_in_progress or self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [mark]
            else:
                lecturer.grades[course] = [mark]
        else:
            return \
                ('Ошибка. Проверьте название курса. 1) Лектор не читает этот курс.)'
                 '( 2) Студент не изучал/ не изучает этот курс.')

    def average_grade_hw(self):
        sum_grades = 0
        number =0
        for v in self.grades.values():
            sum_grades += sum(v)
            number += len(v)
        average_grade_hw_ = round(sum_grades/number, 2)
        return average_grade_hw_

    def __str__(self):
        return f"Имя студента: {self.name}.\nФамилия студента: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.average_grade_hw()}\n" \
               f"Курсы в процессе обучения: {self.courses_in_progress}\n" \
               f"Завершённые курсы:{self.finished_courses}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade_hw() == other.average_grade_hw()
        else:
            return f"Ошибка. Сравниваются объекты разного класса."

    def __ne__(self, other):
        if isinstance(other, Student):
            if self.__eq__(other) is False:
                return True
        else:
            return f"Ошибка. Сравниваются объекты разного класса."

    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_grade_hw() <= other.average_grade_hw()
        else:
            return f"Ошибка. Сравниваются объекты разного класса."

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade_hw() < other.average_grade_hw()
        else:
            return f"Ошибка. Сравниваются объекты разного класса."

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.average_grade_hw() >= other.average_grade_hw()
        else:
            return f"Ошибка. Сравниваются объекты разного класса."

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grade_hw() > other.average_grade_hw()
        else:
            return f"Ошибка. Сравниваются объекты разного класса."

up_mentor = Mentor('Ужас', "Великий")
up_mentor = Mentor('Великан', "Ужасный")
mentor_1 = Lecturer('Николай', 'Свиридов')
mentor_2 = Lecturer('Олег', 'Гежин')
student_1 = Student('Лариса', 'Сергеева', 'Ж')
student_2 = Student("Агата", "Платонова", "Ж")
graduate_student_1 = Reviewer('Анна', "Вартанян")
graduate_student_2 = Reviewer('Игорь', "Сверчков")
graduate_student_2.courses_attached = ["Python"]
student_1.finished_courses += ['Git']
student_1.courses_in_progress += ['Python', 'OOP']
# Оценки первого студента.
student_1.grades['Git'] = [10, 10, 10, 10, 10]
student_1.grades['Python'] = [10, 10]
graduate_student_2.rate_hw(student_1, 'Python', 5)
student_1.grades['OOP'] = [8, 7]
# Оценки второго студента.
student_2.grades['Python'] = [8, 10, 9, 6, 9]

student_2.finished_courses += ['Git']
student_2.courses_in_progress += ['Python', 'OOP']

up_mentor.add_courses('Геометрия')
student_1.add_courses('Геометрия')
mentor_1.courses_attached += ['Git', 'Python', 'OOP', 'Геометрия']
print('Первый студент средняя оценка:', student_1.average_grade_hw())
print('Второй студент средняя оценка:', student_2.average_grade_hw())

mentor_2.courses_attached += ['Python', 'Анализ данных']
graduate_student_1.add_courses(['Python', 'OOP'])

# Оценки лектора 1 за питон.
mentor_1.grades['Python'] = [10, 10, 7]
student_1.rate_lecture(mentor_1, 'Python', 8)
student_2.rate_lecture(mentor_1, 'Python', 7)
# Оценки лектора 2 за питон.
mentor_2.grades['Python'] = [8, 7, 3]
student_1.rate_lecture(mentor_2, 'Python', 6)
student_2.rate_lecture(mentor_2, 'Python', 7)
print(student_1)
print(student_2)
print(mentor_1)
print(mentor_2)
print(graduate_student_1)
print(student_1 != student_2)
print(student_2 <= student_1)
print(student_1 > student_2)
print(mentor_1 <= mentor_2)
print(mentor_1 > mentor_2)


def average_grade_hw(student_list, cours):
    average_list = list()
    for student in students_list:
        if isinstance(student, Student) and cours in student.grades:
            sum_grades = sum(student.grades[cours])
            average = round(sum_grades/len(student.grades[cours]), 2)
            average_list += [average]
        else:
            return f'Ошибка. Студента нет в списке или студент не изучал такой курс.'
    average_grade_hw_ = round(sum(average_list)/len(student_list), 2)
    return f'Средняя оценка всех студентов по курсу: {cours} {average_grade_hw_}'


def average_grade_lectures(mentor_list, cours):
    average_list = list()
    for mentor in mentor_list:
        if isinstance(mentor, Lecturer) and cours in mentor.grades:
            sum_grades = sum(mentor.grades[cours])
            average = round(sum_grades/len(mentor.grades[cours]), 2)
            average_list += [average]
        else:
            return f'Ошибка. Лектор не читает этот курс или его нет в списке лекторов.'
    average_grade_lecture_ = round(sum(average_list)/len(mentor_list), 2)
    return f'Средняя оценка всех лекторов по курсу: {cours} {average_grade_lecture_}'


students_list = [student_1, student_2]
print(average_grade_hw(students_list, 'Python'))

mentor_list = [mentor_1, mentor_2]
print(average_grade_lectures(mentor_list, 'Python'))