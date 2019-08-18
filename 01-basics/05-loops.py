# For loops--
student_names = ["Mark", "Katrina", "Jessica"]

## for in combination
for name in student_names:
    print('Student name is {0}'.format(name))

## using 'range' -> just returns list [0, 1, ...., 9]
# counter = 1
# for index in range(10):
#     counter = counter + 10
#     print(counter)

print('resetting the counter............')
## using 'range' -> just returns list [10, 11, ...., 19]
# counter = 1
# for index in range(10, 20):
#     counter = counter + 10
#     print(counter)


print('resetting the counter............')
## using 'range' -> just returns list [10, 11, ...., 19]
counter = 1
for index in range(10, 20, 3):
    counter = counter + 10
    print(counter)