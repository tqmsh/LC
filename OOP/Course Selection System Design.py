from typing import List, Optional
from collections import defaultdict
from datetime import date
 
class Person:
    def __init__(self, id, name): 
        self.id = id; self.name = name  
 
class Student(Person):
    def __init__(self, id, name): 
        super().__init__(id, name)
    def __str__(self): 
        return f"Student(id={self.id}, name={self.name})"
 
class Teacher(Person):
    def __init__(self, id, name): 
        super().__init__(id, name)
    def __str__(self): 
        return f"Teacher(id={self.id}, name={self.name})"
 
class Course:
    def __init__(self, id, name, t, teacher_id, students=[]): 
        self.id = id; self.name = name; self.t = t; self.teacher_id = teacher_id; self.students: List[Student] = students
class Course:
    def __init__(self, id, name, t, teacher_id, students=[]): 
        self.id = id; self.name = name; self.t = t; self.teacher_id = teacher_id; self.students: List[Student] = students
    
    def __str__(self):  
        students_str = ', '.join(str(student) for student in self.students)
        return f"Course(id={self.id}, name={self.name}, time={self.t}, teacher id={self.teacher_id}, students=[{students_str}])"

class System:
    def __init__(self): 
        self.teacher_name_to_courses: defaultdict[str, List[Course]] = defaultdict(list)
  
class StudentService:
    def __init__(self, system): 
        self.system: System = system; self.student_sz = 0

    def pick(self, student, teacher_name, course_id=None, course_name=None):
        courses = self.system.teacher_name_to_courses[teacher_name]
        ans = None
        
        if course_id: 
            ans = next((course for course in courses if course.id == course_id), None)
        if course_name: 
            ans = next((course for course in courses if course.name == course_name), None)
        
        if ans: 
            ans.students.append(student); print(f"==========\nStudent {student} picked {ans}")
        else: 
            print("==========\nDNE course")

    def init_student(self, name):
        self.student_sz += 1
        return Student(self.student_sz, name)
 
class TeacherService:
    def __init__(self, system): 
        self.system: System = system; self.teacher_sz = 0; self.course_sz = 0

    def init_course(self, course_name, course_t, teacher: Teacher):
        self.course_sz += 1
        self.system.teacher_name_to_courses[teacher.name].append(Course(self.course_sz, course_name, course_t, teacher.id))
        print(f"=========\nteacher {teacher} made {self.system.teacher_name_to_courses[teacher.name][-1]}")        

    def init_teacher(self, name):
        self.teacher_sz += 1
        return Teacher(self.teacher_sz, name)  # Fixed from Student to Teacher

    def show_course_list(self, teacher: Teacher):
        print(f"==========\nteacher {teacher}'s list:")
        for course in self.system.teacher_name_to_courses[teacher.name]: 
            print(course)

# Testing the functionality of the system

# Initialization
system = System()
teacher_service = TeacherService(system)
student_service = StudentService(system)

# Test #1: Initialize teachers and courses
teacher_1 = teacher_service.init_teacher("Mr. Smith")
course_1 = teacher_service.init_course("Math", date(2024, 10, 1), teacher_1)

# Test #2: Initialize students and enroll them
student_1 = student_service.init_student("Alice")
student_2 = student_service.init_student("Bob")
student_service.pick(student_1, "Mr. Smith", course_name="Math")
student_service.pick(student_2, "Mr. Smith", course_name="Math")

# Test #3: Show courses for the teacher
teacher_service.show_course_list(teacher_1)

# 🟥 Edge Case: Picking a course that does not exist
student_service.pick(student_1, "Mr. Smith", course_name="History")

# 🟥 Edge Case: Picking a course for a non-existent teacher
student_service.pick(student_1, "Mr. Doe", course_name="Math")
