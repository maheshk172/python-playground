## For loops with break and continue
student_names = ["Mark", "Katrina", "Jessica", "Makrum", "Stefan", "Jazz"]
found_candidate = None
for name in student_names:
    if name == 'Marka':
        print("found the candidate {0}".format("Mark"))
        found_candidate = True
        break

    if(name == 'Makrum'):
        print("we will not evaluate Markum");
        continue

    print("currently checking " + name)

if found_candidate == True:
    print("Found matching candidate")
else:
    print("Unable to find matching candidate")


## While Loop
x = 1
while True:
    print(x)
    x+=1
    if x == 100:
        break

