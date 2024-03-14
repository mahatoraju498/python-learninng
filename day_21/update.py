import json
FILENAME = 'day_21/students.json'


def update_student():
    student_id = input("enter the student id to update")
    which_info = input("enter the info you want to change")
    new_info = input(f"Enter the  new {which_info}")

    with open(FILENAME, "r+") as fp:
        students = json.loads(fp.read())
        for student in students:
            if student["id"] == student_id:
                student[which_info] = new_info
                break
        else:
            print("invalid student id")
            want_to_continue = input("Do you want to continue?(y/n)")
            return  True if want_to_continue.lower() == 'y' else False
            
        fp.seek(0)
        fp.write(json.dumps(students,indent=2))

print("student Update Successfully")

