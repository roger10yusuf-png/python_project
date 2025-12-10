total_marks = {
    "Math": 100,
    "English": 100,
    "Science": 150,
    "History": 100
}

marks_scored = {
    "Math": 92,
    "English": 85,
    "Science": 120,
    "History": 90}

percentages = {}

for key,value in total_marks.items():
    total = total_marks[key]
    scored = marks_scored[key]
    percentages[key,value] = (scored / total) * 100

print(percentages)
