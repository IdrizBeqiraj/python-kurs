class DigitalSchool:
    def __init__(self, name, city, state, courses):
        # Private attributes
        self.__name = name
        self.__city = city
        self.__state = state
        self.__courses = courses

    # Getters
    @property
    def name(self):
        return self.__name

    @property
    def city(self):
        return self.__city

    @property
    def state(self):
        return self.__state

    @property
    def courses(self):
        return self.__courses

    # Setters
    @name.setter
    def name(self, name):
        self.__name = name

    @city.setter
    def city(self, city):
        self.__city = city

    @state.setter
    def state(self, state):
        self.__state = state

    @courses.setter
    def courses(self, courses):
        self.__courses = courses

    #  Metoda return shkolla digjitale
    def show_school_info(self):
        return {
            "Name": self.__name,
            "City": self.__city,
            "State": self.__state,
            "Courses": self.__courses
        }


# Example usage
if __name__ == "__main__":
    school = DigitalSchool("Shkolla Digjitale", "Prishtina", "Kosov", ["Python", "AI", "Web Development"])

  # metoda e printimit
    info = school.show_school_info()
    for key, value in info.items():
        print(f"{key}: {value}")
