class DigitalSchool:
    def __init__(self, name, city, state, courses):
        self.__name=name
        self.__city=city
        self.__state=state
        self.__courses=courses


    @property
    def name(self):
         return self.__name
    @name.setter
    def name(self, name):
        self.__name=name

    @property
    def name(self):
        return self.__city
    @city.setter
    def name(self, city):
        self.__city = city

    @property
    def name(self):
        return self.__state
    @state.setter
    def name(self,state):
        self.__state = state

    @property
    def name(self):
        return self.__courses

    @courses.setter
    def name(self, courses):
        self.__courses = courses

    #defining methods
    def show_school_info(self):
        return {
            "name":self.__name,
            "city":self.__city,
            "state":self.__state,
            "courses":self.__courses
        }
    def organize_hackathon(self):
        print("Organazing a generetic hackathon")

#define a subclass DS Prishtina where it has a private attribute called student and two methods organize_hackathon  and SCF
class DS_Prishtina(DigitalSchool):
    def __init__(self, name, city, state, courses, student_number):
        super().__init__(name, city, state, courses)
        self.__student_number=student_number
    def SCF(self):
        print("First edition")

    def organize_hackathon(self):
        print("We are doing data analysis hackathon")

prishtina_obj=DS_Prishtina("DS_Prishtina", "Prishtina", "Kosove", ["PHP","Python","JAVA"], 3000)
prishtina_obj.organize_hackathon()
print(prishtina_obj.show_school_info())

#detyra
# Base class
class DigitalSchool:
    def __init__(self, name):
        self.name = name

    def school_info(self):
        return f"Welcome to {self.name} Digital School!"

# Subclass
class DS_Ferizaj(DigitalSchool):
    def __init__(self, name, student_amba):
        super().__init__(name)
        self.__student_amba = student_amba  # private attribute

    def organize_hackathon(self):
        return f"{self.name} is organizing a coding hackathon for {self.__student_amba} student ambassadors!"

    def internship(self):
        return f"{self.name} offers internship programs to {self.__student_amba} student ambassadors."

    # Optional: Getter for student_amba if needed
    def get_student_amba(self):
        return self.__student_amba

school = DS_Ferizaj("DS Ferizaj", 5)
print(school.school_info())                # Inherited 
print(school.organize_hackathon())         # Subclass
print(school.internship())                 # Subclass
