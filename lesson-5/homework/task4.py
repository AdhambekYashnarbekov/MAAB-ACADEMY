import statistics
student_mean=0
tuition_mean=0
student_median=0
tuition_median=0

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats():
    total_students=0
    total_tuition=0
    for i in range(len(universities)):
        total_students+=universities[i][1]
        total_tuition+=universities[i][2]
    return(f"Total students: {total_students}\nTotal tuition: ${total_tuition}")



def mean():
    students=[]
    tuitions=[]
    for i in range(len(universities)):
        students.append(universities[i][1])
        tuitions.append(universities[i][2])
    student_mean=statistics.mean(students)
    tuition_mean=statistics.mean(tuitions)
    return student_mean, tuition_mean


def median():
    students=[]
    tuitions=[]
    for i in range(len(universities)):
        students.append(universities[i][1])
        tuitions.append(universities[i][2])
    student_median=statistics.median(students)
    tuition_median=statistics.median(tuitions)
    return student_median, tuition_median

student_mean, tuition_mean=mean()
student_median, tuition_median=median()




print("******************************")
print(f"{enrollment_stats()}\n")
print(f"Student mean: {student_mean:.2f}\nStudent median: {student_median:,}\n")
print(f"Tuition mean: {tuition_mean:.2f}\nTuition median: {tuition_median:,}")
print("******************************")

