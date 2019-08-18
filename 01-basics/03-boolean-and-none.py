
python_course = True
java_course = False

# print(int(python_course))
# print(str(python_course))

aliens_found = None
print(aliens_found)
aliens_found = False

# ~ == not operator
if ~aliens_found:
    print("Found Aliens")
else:
    print("Aliens not found")

number = 5
if number == 5:
    print(f'number is {number}')
else:
    print(f'number is not {number}')

if not aliens_found:
    print('aliens not found')
else:
    print ('aliens found on earth now')

### AND & ORs
isHuman = True
isAlien = False

if isHuman and isAlien:
    print('This is human as well as alien')
else:
    print('this is not human or alien')

if isHuman or isAlien:
    print('This is human or alien')
else:
    print('this is not a human nor alien')


### Ternary Operator
a = 1
b = 2
print("bigger" if a > b else "smaller")
