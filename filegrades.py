"""
Goal 1: Make two functions. One function gets a user's grades and saves them into a file.
The other function reads a file of grades.
"""

"""
Purpose: Get grades from the user and save them in a file.
Parameters: filename - name of the file that the grades are saved in - string
Returns: None
"""
def saveGrades(filename):
    SENTINEL = "999"
    grades = []
    grade = "0"

    while grade != SENTINEL:
        grade = input("Enter a grade: ")
        while not grade.isdigit() or int(grade) < 0:
            print("Please enter an integer.")
            grade = input("Enter a grade: ")

        if grade != SENTINEL: grades.append(grade)

    fd = open(filename, "w")
    for grade in grades:
        fd.write(grade+"\n")
    fd.close()


"""
Purpose: Read grades out of file.
Parameters: filename - file to read grades from
Returns: List containing the grades in the file
"""
def readGrades(filename):
    grades = []

    fd = open(filename)
    for line in fd:
        grades.append(line.strip())
    fd.close()

    print(grades)


