subjects = ["M1","M2","M3","M4","M5","M6"]
grades = [input(f"{i}: ") for i in subjects]

for i in range(len(subjects)):
    print(f"A {subjects[i]} a tret {grades[i]}")