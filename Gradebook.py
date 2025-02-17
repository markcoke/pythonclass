# Else If Function to get letter grade
def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# Ask for user data
student_name = input("Enter the student name: ")

# Get five grades in a list
grades = list(map(int, input("Enter five grades separated by spaces: ").split()))

# Calculate average
average = sum(grades) / 5

# Get letter grade
letter_grade = get_letter_grade(average)

# Print results
print("\n" + student_name)
print("\nAverage:", round(average, 1))
print("\nLetter Grade:", letter_grade)
