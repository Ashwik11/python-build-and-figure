def result_for(marks):
    """Return total, percentage, grade, and pass status for marks."""
    if not marks or any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100")
    total = 0
    for mark in marks:
        total += mark
    percentage = total / len(marks)
    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"
    passed = all(mark >= 40 for mark in marks)
    return total, percentage, grade, "Pass" if passed else "Fail"


print(result_for([85, 92, 78]))
