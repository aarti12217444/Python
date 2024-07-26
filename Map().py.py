marks = [90, 67, 47, 78, 100]

def grade(marks):
    if marks >= 90:
        return "O"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

a = list(map(grade, marks))
print("Score:", marks)
print("Grades:", a)
