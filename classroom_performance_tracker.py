def calculate_average_and_top_performer(students):
    averages = {name: sum(marks)/len(marks) for name, marks in students.items()}
    top_performer = max(averages, key=averages.get)
    return averages, top_performer

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
averages, top_performer = calculate_average_and_top_performer(students)
print(f"Average Marks: {averages}")
print(f"Top Performer: {top_performer}")
