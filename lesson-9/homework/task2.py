import csv


grades = {}

with open("grades.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        subject = row["Subject"]
        grade = int(row["Grade"]) 
        
        if subject not in grades:
            grades[subject] = []  
        grades[subject].append(grade)  


average_grades = {subject: sum(grades_list) / len(grades_list) for subject, grades_list in grades.items()}


with open("average_grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])  
    
    for subject, avg_grade in average_grades.items():
        writer.writerow([subject, avg_grade])

print("Average grades have been successfully written to 'average_grades.csv'.")
