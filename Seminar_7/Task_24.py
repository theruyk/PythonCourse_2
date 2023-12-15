students_data = [
    {"name": "Anna", "scores": {"math": 89, "history": 90, "physics": 95}},
    {"name": "Bob", "scores": {"math": 78, "history": 88, "physics": 82}},
    {"name": "Charlie", "scores": {"math": 95, "history": 92, "physics": 90}},
    {"name": "David", "scores": {"math": 80, "history": 85, "physics": 88}}
]

def func(data):
    highest_score = 0
    best_subject = ''
    best_student_name = ''
    
    for student in data:
        name = student["name"]
        scores = student["scores"]
        
        for subject, mark in scores.items():
            if mark > highest_score:
                highest_score = mark
                best_subject = subject
                best_student_name = name
            avg_mark = sum(mark) / len(mark)
                
    return best_subject, best_student_name, avg_mark

print(func(students_data))



