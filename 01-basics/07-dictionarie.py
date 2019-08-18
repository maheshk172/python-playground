student_database = [{
    "name": "Mark",
    "rollNo": 20,
    "feedback": None
}, {
    "name": "Mark1",
    "rollNo": 21,
    "feedback": None
}, {
    "name": "Mark2",
    "rollNo": 22,
    "feedback": None
}, {
    "name": "Mark1",
    "rollNo": 21,
    "feedback": None
}]

for student in student_database:
    print(student["name"])
    print(student["rollNo"])
    print(student["feedback"])
    print(student.get("feedback1","No feedback"))
