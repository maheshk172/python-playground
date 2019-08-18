student = {
    "name": "Mark",
    "rollNo": 20,
    "feedback": None
}

try:
    print(student["name"])
    print(student["rollNo"])
    print(student["feedback"])
    print(student.get("feedback4"))
    integer = 100
    integer = integer + "100"
except KeyError as keyError:
    print("Key error thrown")
    print(keyError)
except Exception as error:
    print("Generic error handler")
    print(error)
finally:
    print("Finally always calls")




