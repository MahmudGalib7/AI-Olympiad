
students_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eve": 88
}

"""
Write a function find_top_student(students_scores) that returns the name of the student with the highest score
"""

def find_top_student(students_score):
    top_student = None
    top_score = 0

    for student, score in students_scores.items():
        if score > top_score:
            top_score = score
            top_student = student

    return top_student


def find_top_student_(students_score):
    return max(students_score, key=students_score.get)


print(find_top_student(students_scores))
print(find_top_student_(students_scores))