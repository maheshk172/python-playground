student_names = []
student_names = ["Mark", "Katrina", "Jessica"]

# print(student_names[0])
# print(student_names[1])
# print(student_names[2])
#
# print(student_names[-1])
# print(student_names[-2])
# print(student_names[-3])

student_names.append('joseph')
new_students = ["akram", "chintu", "pinu"]
student_names.append(new_students)

print(student_names)
# print length of list
print(len(student_names))

## check if item is 'in' the list
if "Mark" in student_names:
    print("Mark is enrolled")
    index_of_student = student_names.index("Mark")
    del student_names[index_of_student]
    print('removed Mark')
else:
    print('Mark is not in the list')

print(student_names)

