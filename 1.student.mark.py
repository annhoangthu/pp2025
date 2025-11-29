
students_list=[]
courses =[]
marks ={}

def nb_students():
    count = int(input("Enter number of students in the class: "))
    return count

def student_information():
    num = nb_students()
    for i in range(num):
        print(f"enter the details information of the student {i+1}")
        std_id = input("Student ID: ")
        std_name = input("Student name: ")
        DoB = input("Date of birth (date/month/year): ")
        student = {'id': std_id, 'name':std_name, 'DoB': DoB}
        students_list.append(student)

def nb_courses():
    count = int(input("\nEnter number of courses: "))
    return count

def course_information():
    num = nb_courses()
    for i in range(num):
        print(f"Enter the details information of the course {i+1}")
        course_id = input("The course ID: ")
        course_name = input("The course name: ")
        course = {'id': course_id, 'name': course_name}
        courses.append(course)


def list_courses():
    print("List of courses")
    if not courses:
        print("No courses available")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")

def list_students():
    print("Lists of students")
    if not students_list:
        print("No student available")
    for s in students_list:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['DoB']}")

def input_marks():
    list_courses()
    if not courses:
        return
    course_id = input("Enter course ID to input marks for:")
    print(f"input marks for course: {course_id} ")
    if course_id not in marks:
        marks[course_id]={}
    for s in students_list:
        try:
            mark = float(input(f"Enter mark for student {s['name']} (ID: {s['id']}): "))
            marks[course_id][s['id']] = mark
        except ValueError:
            print("Invalid input. Skipping this student")

def show_std_marks():
    list_courses()
    course_id = input("Enter course ID to view marks:")
    if course_id in marks:
        print(f"Marks for course {course_id}")
        for s in students_list:
            std_id = s['id']
            if std_id in marks[course_id]:
                print(f"Student: {s['name']}, Mark: {marks[course_id][std_id]}")
            else:
                print(f"Student: {s['name']}, Mark: N/A")
    else:
        print("No marks found for this course")

def menu():
    print("Student mark management system")
    print("1. Input students")
    print("2. Input course")
    print("3. List students")
    print("4. List courses")
    print("5. Input marks for a course")
    print("6. Show student marks")
    print("7. Exit")
    choice = input("Select an option: ")
    return choice

if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == '1':
            student_information()
        elif choice == '2':
            course_information()
        elif choice == '3':
            list_students()
        elif choice == '4':
            list_courses()
        elif choice == '5':
            input_marks()
        elif choice == '6':
            show_std_marks()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again")