

# *args
def print_welcome_message(name, *args):
    print(name)
    print(args)

def print_message(name, **kwargs):
    print(name)
    print(kwargs)


print_welcome_message("mahesh", "1", 2, 3, 4, None, "Loves python")
print_message("mahesh", field1="1", field2=2, field3=3, field4=4, field5=None, field6="Loves python")