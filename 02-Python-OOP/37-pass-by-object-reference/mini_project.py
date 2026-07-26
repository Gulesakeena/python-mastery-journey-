"""
Mini Project

Student Score Management
"""

def add_score(scores, score):
    scores.append(score)


def replace_scores(scores):
    scores = [100, 100, 100]
    print("Inside function:", scores)


student_scores = [78, 85, 90]

print("Before:", student_scores)

add_score(student_scores, 95)

print("After add_score:", student_scores)

replace_scores(student_scores)

print("After replace_scores:", student_scores)

print("Memory ID:", id(student_scores))