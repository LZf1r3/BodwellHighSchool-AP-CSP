#Importing libraries
import os
from time import sleep as s

# Data Setup => Dictionary of students with names and IDs
students = [{"name": "Alice", "id": 10234},
    {"name": "Bob", "id": 20345},
    {"name": "Charlie", "id": 30456},
    {"name": "David", "id": 40567},
    {"name": "Eva", "id": 50678},
    {"name": "Frank", "id": 60789},
    {"name": "Grace", "id": 70890},
    {"name": "Hannah", "id": 80901},
    {"name": "Ian", "id": 91012},
    {"name": "Jack", "id": 10123},
    {"name": "Kathy", "id": 11234},
    {"name": "Liam", "id": 12345},
    {"name": "Mia", "id": 13456},
    {"name": "Noah", "id": 14567},
    {"name": "Olivia", "id": 15678},
    {"name": "Paul", "id": 16789},
    {"name": "Quinn", "id": 17890},
    {"name": "Rachel", "id": 18901},
    {"name": "Sam", "id": 19012},
    {"name": "Tina", "id": 20123},
    {"name": "Uma", "id": 21234},
    {"name": "Vince", "id": 22345},
    {"name": "Wendy", "id": 23456},
    {"name": "Alice", "id": 24567},
    {"name": "Bob", "id": 25678},
    {"name": "Charlie", "id": 26789},
    {"name": "David", "id": 27890},
    {"name": "Eva", "id": 28901},
]

# Preparing sorted list for binary search (IDs only)
def ids_data():
    ids_sorted = sorted([student["id"] for student in students])
    return ids_sorted

# Preparing name list for linear search
def names_data():
    students_names = [student["name"] for student in students]
    return students_names

# Functions for searching students cmon we all know how this works by now...
"""
Well, if you don't, this is how a binary works:
    
1. Start with two pointers, low and high, at the beginning and end of the list.
2. While low is less than or equal to high:
    a. Calculate the mid index.
    b. If the middle element is the target, return its index.
    c. If the target is greater than the middle element, move the low pointer to mid + 1.
    d. If the target is less than the middle element, move the high pointer to mid - 1.
3. If the target is not found, return -1.
"""
def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    steps = 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid, steps
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps


# Linear Search Function
def linear_search(list, target):
    _steps = []
    indexes  = []
    steps = 0
    for index, value in enumerate(list):
        steps += 1
        if value == target:
            indexes.append(index)
            _steps.append(steps)
    
    return indexes, steps

#Function to add a student to the list. It add the student to the list.
def add_student(name, id):
    students.append({"name": name, "id": id})
    print(f"Student {name} with ID {id} added successfully.")

#Function to remove a student from the list by ID
def remove_student(id):
    global students
    students = [student for student in students if student["id"] != id]
    print(f"Student with ID {id} removed successfully.")

# Main Program Loop
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the Student Lookup System!")
    s(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("---------------------")
        print("Student Lookup Menu")
        print("---------------------")
        print(" 1. Search by student ID")
        print(" 2. Search by student name")
        print(" 3. Show all students")
        print(" 4. Add a new student")
        print(" 5. Remove a student")
        print(" 6. Clear Screen")
        print(" 7. Exit")
        print("---------------------")

        # Get user choice
        choice = input("Please enter your choice (1-7): ")

        #Definition of choices
        if choice == '1':
            try:
                target_id = int(input("Enter Student ID to search: "))
                ids_sorted = ids_data()
                index, steps = binary_search(ids_sorted, target_id)
                student_found = next((student for student in students if student["id"] == target_id), None)
                if student_found:
                    print(f"Student Found: Name: {student_found['name']}, ID: {student_found['id']}, Steps: {steps}")
                else:
                    print(f"Student ID {target_id} not found. Steps taken: {steps}")
            except ValueError:
                print("Invalid input. Please enter a numeric ID.")

        elif choice == '2':
            target_name = input("Enter Student Name to search: ")
            names_list = names_data()
            indexes, steps = linear_search(names_list, target_name)
            if indexes:
                print(f"Student(s) Found at indexes {indexes} with total steps: {steps}")
                for idx in indexes:
                    student = students[idx]
                    print(f"Name: {student['name']}, ID: {student['id']}")
            else:
                print(f"Student Name '{target_name}' not found. Steps taken: {steps}")
        
        elif choice == '3':
            print("All Students:")
            for student in students:
                print(f"Name: {student['name']}, ID: {student['id']}")
        
        elif choice == '4':
            name = input("Enter Student Name to add: ")
            try:
                id = int(input("Enter Student ID to add: "))
                add_student(name, id)
                ids_sorted = ids_data()  # Update sorted IDs list with new student
            except ValueError:
                print("Invalid input. Please enter a numeric ID.")
        
        elif choice == '5':
            try:
                id = int(input("Enter Student ID to remove: "))
                remove_student(id)
                ids_sorted = ids_data()  # Update sorted IDs list after student removal
            except ValueError:
                print("Invalid input. Please enter a numeric ID.")
            
        elif choice == '6':
            os.system('cls' if os.name == 'nt' else 'clear')

        elif choice == '7':
            print("Exiting the Student Lookup System. Goodbye!")
            exit()
        
        input("Press Enter to continue")