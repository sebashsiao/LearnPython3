class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []
        self.attendance = {}

    def __repr__(self):
        return self.name + ', year: {}'.format(self.year)

    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade.score)

    def get_average(self):
        avg_grade = sum(self.grades) / len(self.grades)
        return 'Average score: {}'.format(round(avg_grade, 1))

    def add_attendance(self, attend):
        if type(attend) is Attendance:
            self.attendance[attend.date] = attend.attd


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

    def is_passing(self):
        if self.score > 90:
            return 'Congrats, you have passed with excellent score!'
        elif self.score >= 65:
            return 'Congrats, you have passed the grade.'
        else:
            return 'Sorry, you did not pass the grade :('


class Attendance:
    def __init__(self, date, attd=True):
        self.date = date
        self.attd = attd


# Instance objects
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

# Add grades
pieter.add_grade(Grade(100))
pieter.add_grade(Grade(82))
pieter.add_grade(Grade(75))

# Add attendances
pieter.add_attendance(Attendance('2023/08/10'))
pieter.add_attendance(Attendance('2023/08/11'))
pieter.add_attendance(Attendance('2023/08/12', False))
pieter.add_attendance(Attendance('2023/08/14', True))



print("----- ----- TESTING LINES ----- -----")

print('Student Info:', pieter)
print('Grades:', pieter.grades)
print('Attendance:', pieter.attendance)
# print('Attendance:', [f'{k} attd= {v}' for k,v in pieter.attendance.items()])

# print(Grade(88).score)
# print(Grade(55).is_passing())
# print(Grade(65).is_passing())
# print(Grade(96).is_passing())
# print(pieter.get_average())
# print(Attendance('2023/01/01').date)
# print(Attendance('2023/01/01').attd)

