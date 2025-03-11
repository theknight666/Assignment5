marks = {
    "Alice": 85,
    "Benney": 58,
    "Mukul": 98,
    "Sudip": 66,
    }

name = input("Enter the student's name: ")

# Retrieve and display the corresponding marks
if name in marks:
    print(f"{name}'s marks: {marks[name]}")
else:
    print("Student not found")
