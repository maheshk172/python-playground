
mca_students = []
bcs_students = []

def add_student(name, class_name, role_no, feedback=None):
    tempStudent = {
        "name":name,
        "class_name":class_name,
        "role_no": role_no
    }

    if feedback:
        tempStudent["feedback"] = feedback

    if class_name == "MCA":
        mca_students.append(tempStudent)
    elif class_name == "BCS":
        bcs_students.append(tempStudent)
    else:
        print(tempStudent)
        print("cant add this student, class should MCA/BCS only")

def printStudents(students):
    if not students:
        print("request params students are empty or not truthy")
        return

    for student in students:
        print(student)


add_student("mark1","MCA",21,"Differantly abled student")
add_student("mark2","BCS",22)
add_student("mark3","BCS",21,"Differantly abled student")
add_student("mark4","BCD",22)
add_student("mark5","MCA",21,"Lefty")
add_student("mark6","MCS",22)
add_student("mark7","MCS",22,"painter")

print("Printing MCA Students List")
print(mca_students)

print("Printing BCS Students List")
print(bcs_students)

