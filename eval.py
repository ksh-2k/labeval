dict1 = {
    
    "student1":{"name":"Kshitij" , "class" : "12","height" : "169" , "weight" : "61"},
    "student2":{"name":"Akshat" , "class" : "12","height" : "139" , "weight" : "44"},
    "student3":{"name":"aditiya" , "class" : "12","height" : "175" , "weight" : "79"}
    
}

def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def dietchart(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 22 :
        return "need more intake"
    else:
        return "sufficient intake"
    
        def main():
    students = []

    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        student = {}
        student["name"] = input("Enter student name: ")
        student["class"] = input("Enter student class: ")
        student["height_m"] = float(input("Enter student height (in meters): "))
        student["weight_kg"] = float(input("Enter student weight (in kg): "))
        student["sport"] = input("Enter student's sport: ")

        bmi = calculate_bmi(student["weight_kg"], student["height_m"])

        if bmi < 18.5:
            diet_status = "Red (Underweight)"
        elif 18.5 <= bmi < 24.9:
            diet_status = "Orange (Needs more intake)"
        else:
            diet_status = "Green (Sufficient consumption)"

        student["diet_status"] = diet_status
        students.append(student)

    for student in students:
        print(f"\nStudent: {student['name']}")
        print(f"Class: {student['class']}")
        print(f"Sport: {student['sport']}")
        print(f"Diet Status: {student['diet_status']}")

    main()



