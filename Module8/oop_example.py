from symtable import Class

from Module8.procedural_programing import perimeter


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

my_rectangle = Rectangle(2, 5)

area = my_rectangle.calculate_area()
perimeter = my_rectangle.calculate_perimeter()

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

class Personi:
    def __init__(self, Emri, Mosha):
        self.Emri = Emri
        self.Mosha = Mosha
    def greet(self):
      print(f"Hello, i am {self.Emri}, and i am {self.Mosha} years old")

personi1 = Personi("Idriz", 18)
personi2 = Personi("Leon", 88)

personi1.greet()
personi2.greet()

class Student:
    school_name = "Digital School"
    student_name = "Student"

    def __init__(self,Emrii, Moshaa, Kursii):
        self.Emrii = Emrii
        self.Moshaa=Moshaa
        self.Kursii=Kursii

student_1 = Student("Bajram", 18, "Python")
print(student_1.Kursii)

#student_1 = Student()
#print(student_1.school_name)
#print(student_1.student_name)