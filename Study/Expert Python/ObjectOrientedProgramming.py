class Szamol:
    def __init__(self, x, y):
        self.elsotag = x
        self.masodiktag = y

    def osszeg(self):
        return self.elsotag + self.masodiktag

    def kulonbseg(self):
        return self.elsotag - self.masodiktag

    def szorzat(self):
        return self.elsotag * self.masodiktag

    def osztas(self):
        return self.elsotag / self.masodiktag

    def info(self):
        print(f"Osszeg: {self.osszeg()}\n"
              f"Kulonbseg: {self.kulonbseg()}\n"
              f"Szorzat: {self.szorzat()}\n"
              f"Osztas: {self.osztas()}")


# -------------------------------------------------------------------------------------------------------------------


class AdvAdd:
    def __init__(self, *nums):
        self.nums = nums

    def add(self):
        total = 0
        for i in self.nums:
            total += i
        return total

    def info(self):
        print(f"Add: {self.add()}")


# -------------------------------------------------------------------------------------------------------------------


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, course_name, max_students):
        self.course_name = course_name
        self.max_students = max_students
        self.students = []

    def get_course_name(self):
        return self.course_name + " Course"

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
        else:
            print(f"[ERROR] The {self.get_course_name()} is full!")

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return f"[{self.get_course_name()}] Average grade: {value / len(self.students)}"


# -------------------------------------------------------------------------------------------------------------------


def courses():
    s1 = Student("Tim", 19, 95)
    s2 = Student("Bill", 18, 75)
    s3 = Student("Jill", 19, 65)

    science_curse = Course("Science", 2)

    science_curse.add_student(s1)
    science_curse.add_student(s2)

    print(science_curse.get_average_grade())


def calcs():
    g = int(input("Kerem az elso szamot: "))
    h = int(input("Kerem a masodik szamot: "))

    sz = Szamol(g, h)

    print(sz.info())


def adv_calcs():
    sz = AdvAdd(5, 8, 11, 20, 3, 7, 41)

    print(sz.info())

