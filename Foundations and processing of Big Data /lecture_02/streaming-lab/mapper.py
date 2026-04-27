#!/usr/bin/env python3
# Reads CSV rows from stdin, emits: student_id \t score
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split(",")
    if parts[0] == "student_id":   # skip header
        continue
    try:
        student_id = parts[0]
        score = float(parts[3])
        print(f"{student_id}\t{score}")
    except (IndexError, ValueError):
        continue
