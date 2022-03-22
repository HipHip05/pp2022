from typing import List, Any


def inputStudentcount():
    return int(input("Please enter number of student:"))


class Students:
    pass


def inputStudentInfo(studentCount):
    students = []
    for i in range(studentCount):
        print(f"Please enter student {i + 1} info:")
        id = input("- ID:")
        name = input("-Name:")
        birthday = input("-DoB:")
        Students.append({
            "name": name,
            "id": id,
            "dob": birthday
        })
    print(f"Finished entering{studentCount} student")
    return students
def inputCourseCount():
    return int(input("Please enter number of courses: "))

def selectCourse():
    for i in range(len(student_list)):
        mark = input(f"input mark for student id {i + 1} for course {course} :")
        student_list[i]["mark"][course] = mark

def inputStudentMarkForCourse():
    pass

def listCourse(courseList):
    def print_course_list_for():
        for i in range(len(course_list)):
            print("course id:", course_list[i]["course_id"])
            print("course name:", course_list[i]["name"])
            print("\n")

def listStudent(students):
    print(f"Listing {len(students)} students")
    for student in students:
         print(f"- ID {student['id']}, name {student['name']}, DoB {student['dob']}")

def showMarks():
    for i in range(len(student_list)):
        print("student id:", student_list[i]["id"])
        print("student name:", student_list[i]["name"])
        print("course_name:", course)
        print("student mark:", student_list[i]["mark"][course])
        print("\n")

studentCount = inputCourseCount()
student: list[Any] = inputStudentInfo(studentCount)
listStudents(students)

courseCount = inputCourseCount()
inputCourseCount()
listCourse()
selectCourse()
inputStudentMarkForCourse()
showMarks()
