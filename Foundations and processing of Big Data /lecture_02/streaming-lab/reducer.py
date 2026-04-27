#!/usr/bin/env python3
# Reads sorted "student_id \t score" lines from stdin,
# emits: student_id \t average_score
import sys

current_student = None
total = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    student_id, score = line.split("\t")
    score = float(score)

    if student_id != current_student:
        if current_student is not None:
            print(f"{current_student}\t{total / count:.2f}")
        current_student = student_id
        total = 0.0
        count = 0

    total += score
    count += 1

if current_student is not None:
    print(f"{current_student}\t{total / count:.2f}")
