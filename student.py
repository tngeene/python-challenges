class Student:

    def  __init__(self, name, course, gpa, is_on_probation):
        self.name = name
        self.course = course
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honour_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False