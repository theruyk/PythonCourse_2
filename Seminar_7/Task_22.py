students_scores = {
    "Anna": [89, 92, 85, 78, 90],
    "Bob": [60, 65, 70, 72, 68],
    "Charlie": [99, 99, 99, 99, 99],
    "David": [80, 78, 82, 84, 83]
}

def func(students_scores:dict):
    best_avg_score = 0
    best_student = ""
    for student, scores in students_scores.items():
        avg_score = sum(scores) / len(scores)
        if avg_score > best_avg_score:
            best_avg_score = avg_score
            best_student = student
    return best_student, best_avg_score

print(f'{func(students_scores)[0]} has the highest average score of {func(students_scores)[1]}')

     