
class Student:
    def __init__(self, name, age, grade):
        # private attribute
        self.__name = name
        self.age = age
        self.grade = grade
    
    # protected method
    def _get_grade(self):
        return self.grade
    
    # private method
    def __get_name(self):
        return self.__name
    
    # public method
    def display_student_info(self):
        print("Name:", self.__get_name())
        print("Age:", self.age)
        print("Grade:", self._get_grade())

# creating an object of the class
student = Student("John Doe", 22, "A")

# accessing the public method
student.display_student_info()
