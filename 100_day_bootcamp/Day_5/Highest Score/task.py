student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]


total_exam_score = sum(student_scores)
print(total_exam_score)

total = 0
for score in student_scores:
    total += score

print(total)

maxScore = 0
for score in student_scores:
    if score > maxScore:
        maxScore = score
print(maxScore)
print(max(student_scores))