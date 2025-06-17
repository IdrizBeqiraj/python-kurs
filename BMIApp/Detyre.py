#Klas abstrakte person  name, age,weight, height || calculate_bmi || get_bmi_catgory || print info
#klasa Adult BMI= weight-height || underweight BMI < 18,5 || Normal:18,5-24.9 || Overweight: 24.9-29.9 || obese: >= 29.9 kjo hine te get_bim_category
#Klasa child BMI = weight-height * 1,3

from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height




    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name



    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age



    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight):
        self.__weight = weight



    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        self.__height = height



    @abstractmethod
    def calculate_bmi(self):
        pass
    @abstractmethod
    def get_bmi_category(self):
        pass


    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} m")
        bmi = self.calculate_bmi()
        print(f"BMI: {bmi:.2f}")
        print(f"BMI Category: {self.get_bmi_category()}")




class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal"
        elif 24.9 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"




class Child(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "Underweight"
        elif 14 <= bmi < 18:
            return "Normal"
        elif 18 <= bmi < 24:
            return "Overweight"
        else:
            return "Obese"


#BMI App,  add_person, collect_user_details, Print_results, run
class BMIApp:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)
        print(f"{person.name} added successfully.")

    def collect_user_details(self):
        try:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (m): "))

            if age >= 18:
                person = Adult(name, age, weight, height)
            else:
                person = Child(name, age, weight, height)

            self.add_person(person)
        except ValueError as e:
            print(f"Invalid input: {e}")

    def print_results(self):
        if not self.people:
            print("No people added yet.")
            return
        print("\nBMI Results:")
        for person in self.people:
            print("-" * 20)
            person.print_info()

    def run(self):
        while True:
            print("\nBMI App Menu:")
            print("1. Add person")
            print("2. Show results")
            print("3. Exit")

            choice = input("Choose an option: ")
            if choice == '1':
                self.collect_user_details()
            elif choice == '2':
                self.print_results()
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")


adult = Adult("Idriz Beqiraj", 30, 70, 1.75)
adult.print_info()

print()

child = Child("Idriz Beqiraj", 10, 35, 1.3)
child.print_info()
