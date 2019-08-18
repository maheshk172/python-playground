
# String operations
#string = 'Big black fox jumps on the fence and now he is over the fence'
# string = "HelloWorld"
#
# print(string.capitalize())
# print(string.count(string))
# string = string.replace('o','#')
# print(string)
# print(string.isalpha())
# string = string + '200'
# print(string.isalnum())
#
# numString = "200s"
# print("Is Digit: ")
# print(numString.isdigit())
# # Split and create array/list
# print(string.split("#"))

### String Formatting
name = 'Mahesh Kulkarni'
machine = 'Hal'

message = 'Nice to meet {0}, I am {1}'
print(message)
print(message.format(name, machine))

### String Interpolcation - using 'f' === format
print(f'Nice to meet {name}, I am {machine}')

