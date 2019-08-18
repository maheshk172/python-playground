class Student:
    # name = ""
    # rollno = None

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        
    def toString(self):
        return f"name:{self.name}, rollno:{self.rollno}"

    def __str__(self):
        return "name:{0}, rollno:{1}".format(self.name, self.rollno)


class StudentManager:
    file_name = "./data/students-db.txt"
    students = []

    def add_student_to_db(self, name, rollno):
        tempStudent = Student(name, rollno)
        try:
            file = open(self.file_name, "a")
            #file.write(str("{" + tempStudent.toString()) + "}\n")
            file.write("{" + str(tempStudent) + "}\n")
            file.close()
        except Exception as exception:
            print(exception)

    def add_student(self, student):
        self.students.append(student)

    def populate_data_in_file(self, numberOfLines):
        for item in range(numberOfLines):
            self.add_student_to_db("student-{0}".format(item), item)

    def read_from_file(self):
        try:
            file = open(self.file_name, "r")
            for student in file.readlines():
                self.add_student(student)
            file.close()

        except Exception as exception:
            print("Error while reading the data from file")
            print(exception)


studentManager = StudentManager()
studentManager.populate_data_in_file(10)
studentManager.read_from_file()
print(studentManager.students)