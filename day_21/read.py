# import json 

# FILENAME = "day_21/student.json"

# def read_student():
#     student_id = input("Enter student id")
#     with open(FILENAME, "r") as fp:
#         students = json.loads(fp.read())
#         for student in students:
#             if student["id"] == student_id:
#                 print(student)
#                 break
#         else:
#             print("invalid student_id")
        
#         want_to_continue = input("Do you want to continue?(y/n)")
#         return True if want_to_continue.lower() == 'y' else False
    









import json 

FILENAME = "day_21/students.json"

def read_student():
    student_id = input("Enter student id")
    with open(FILENAME, "r") as fp:
        students = json.loads(fp.read())
        filtered_student = list(filter(lambda student: student["id"] == student_id, students))
        if filtered_student:
            print(filtered_student[0])
        else:
            print("invalid student_id")
        
        want_to_continue = input("Do you want to continue?(y/n)")
        return True if want_to_continue.lower() == 'y' else False