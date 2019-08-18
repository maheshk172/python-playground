file_name = "./data/students-db.txt"
students=[]


def add_student(student):
    students.append(student)

def read_from_file():
    try:
        file = open(file_name, "r")
        for student in read_Students(file):
            add_student(student)
        file.close()

    except Exception as exception:
        print("Error while reading the data from file")
        print(exception)


def read_Students(f):
    for line in f:
        yield line

read_from_file()
print(students)