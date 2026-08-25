#           Task1
#-------------------------------
class Course:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class Student:

    def __init__(self, name):
        self.name = name
        self.courses = []  # Composition: Student has a list of Course objects

    def add_course(self, name, grade):
        # Reject grades outside 0-100
        if 0 <= grade <= 100:
            course_obj = Course(name, grade)
            self.courses.append(course_obj)

    def gpa(self):
        if len(self.courses) == 0:
            return 0.0

        total = 0
        for i in self.courses:
            total += i.grade

        avg = total / len(self.courses)
        return round(avg, 1)

    def best_course(self):
        if len(self.courses) == 0:
            return None

        # Finding max using loop as instructed
        best = self.courses[0]
        for c in self.courses:
            if c.grade > best.grade:
                best = c

        return best.name


if __name__ == '__main__':
    s = Student("Hager")
    s.add_course("C languge", 90)
    s.add_course("C++ languge", 95)
    s.add_course("Python languge", 80)
    s.add_course("Verilog languge",90)

    print("GPA =", s.gpa())
    print("Best course =", s.best_course())
    print("Courses =", len(s.courses))