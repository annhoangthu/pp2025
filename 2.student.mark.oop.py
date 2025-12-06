class Students:
    def __init__(self, std_id, std_name, dob):
        self.__id = std_id
        self.__name = std_name
        self.__dob = dob
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob
    def __str__(self):
        return f"ID: {self.__id}; Name: {self.__name}; DoB: {self.__dob}"

class Courses:
    def __init__(self, course_id, course_name):
        self.__id = course_id
        self.__name = course_name
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def __str__(self):
        return f"ID: {self.__id}; Name: {self.__name}"

class MarkManagementSystem:
    def __init__(self):
        self.__students =[]
        self.__courses = []
        self.__marks = {}

    def input_student(self):
        try:
            count = int(input("Enter number of students in the class: "))
        except ValueError:
            print("Invalid number")
            return
        for i in range(count):
            print(f"enter the details information of the student {i+1}")
            std_id = input("Student ID: ")
            std_name = input("Student name: ")
            DoB = input("Date of birth (date/month/year): ")
            student = Students(std_id, std_name, DoB)
            self.__students.append(student)

    def input_course(self):
        try:
            count = int(input("\nEnter number of courses: "))
        except ValueError:
            print("Invalid number")
            return
        for i in range(count):
            print(f"Enter the details information of the course {i+1}")
            course_id = input("The course ID: ")
            course_name = input("The course name: ")
            course = Courses(course_id, course_name)
            self.__courses.append(course)

    def list_courses(self):
        print("List of courses")
        if not self.__courses:
            print("No courses available")
        for c in self.__courses:
            print(c)
    
    def list_students(self):
        print("Lists of students")
        if not self.__students:
            print("No student available")
        for s in self.__students:
            print(s)

    def input_marks(self):
        self.list_courses()
        if not self.__courses:
            return
        course_id = input("Enter course ID to input marks for:")
        print(f"input marks for course: {course_id} ")
        if course_id not in self.__marks:
            self.__marks[course_id]={}
        for s in self.__students:
            try:
                mark = float(input(f"Enter mark for student {s.get_name()} (ID: {s.get_id()}): "))
                self.__marks[course_id][s.get_id()] = mark
            except ValueError:
                print("Invalid input. Skipping this student")

    def show_std_marks(self):
        self.list_courses()
        course_id = input("Enter course ID to view marks:")
        if course_id in self.__marks:
            print(f"Marks for course {course_id}")
        for s in self.__students:
            std_id = s.get_id()
            if std_id in self.__marks[course_id]:
                print(f"Student: {s.get_name()}, Mark: {self.__marks[course_id][std_id]}")
            else:
                print(f"Student: {s.get_name()}, Mark: N/A")
        else:
            print("No marks found for this course")

    def run(self):
        while True:
            print("Student mark management system")
            print("1. Input students")
            print("2. Input course")
            print("3. List students")
            print("4. List courses")
            print("5. Input marks for a course")
            print("6. Show student marks")
            print("7. Exit")
            choice = input("Select an option: ")
            
            if choice == '1':
                self.input_student()
            elif choice == '2':
                self.input_course()
            elif choice == '3':
                self.list_students()
            elif choice == '4':
                self.list_courses()
            elif choice == '5':
                self.input_marks()
            elif choice == '6':
                self.show_std_marks()
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = MarkManagementSystem()
    system.run()
