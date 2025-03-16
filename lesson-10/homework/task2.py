import csv
from collections import defaultdict

class GradeManager:
    def __init__(self, filename):
        """Initialize with the filename and load data."""
        self.filename = filename
        self.grades = []  
    def read_grades(self):
        """Read grades from the CSV file and store them in a list of dictionaries."""
        with open(self.filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['Grade'] = int(row['Grade'])  
                self.grades.append(row)

    def calculate_average_grades(self):
        """Calculate the average grade for each subject."""
        subject_totals = defaultdict(list)

        for record in self.grades:
            subject_totals[record['Subject']].append(record['Grade'])

        averages = {subject: sum(grades) / len(grades) for subject, grades in subject_totals.items()}
        return averages

    def write_average_grades(self, output_filename):
        """Write the average grades to a new CSV file."""
        averages = self.calculate_average_grades()
        with open(output_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Subject", "Average Grade"])
            for subject, avg in averages.items():
                writer.writerow([subject, round(avg, 2)])  


if __name__ == "__main__":
    manager = GradeManager("grades.csv")
    manager.read_grades()
    manager.write_average_grades("average_grades.csv")
    print("Average grades have been written to average_grades.csv")

