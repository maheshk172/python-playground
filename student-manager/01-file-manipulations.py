file_name = "./data/students-db.txt"
students = []

def add_student_to_db(name, rollno):
    tempStudent = {
        "name": name,
        "rollno": rollno
    }
    try:
        file = open(file_name, "a")
        file.write(str(tempStudent) + "\n")
        file.close()
    except Exception as exception:
        print(exception)


def add_student(student):
    students.append(student)


def populate_data_in_file(numberOfLines):
    for item in range(numberOfLines):
        add_student_to_db("student-{0}".format(item), item)


def read_from_file():
    try:
        file = open(file_name, "r")
        for student in file.readlines():
            add_student(student)
        file.close()

    except Exception as exception:
        print("Error while reading the data from file")
        print(exception)


def __main__():
    populate_data_in_file(10)
    read_from_file()
    print(students)

__main__()