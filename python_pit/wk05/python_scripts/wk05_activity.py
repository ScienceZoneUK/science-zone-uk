# Week 5: Functions and Modular Programming - Class Activity
name = ""
marks = 0
grade = 0

def userinput(name, marks):
    

def calculate_grade(name, marks):
    if 0 <= marks <= 100:
        if marks >= 90:
            grade = 9
        elif marks >= 80:
            grade = 8
        elif marks >= 70:
            grade = 7
        elif marks >= 60:
            grade = 6
        elif marks >= 50:
            grade = 5
        elif marks >= 40:
            grade = 4
        else:
            grade = 'U'
        print(f"Student: {name}, Grade: {grade}")
    else:
        print("Invalid marks. Please enter a value between 0 and 100.")

