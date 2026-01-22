import json
import os

FILE_NAME = "students.json"

def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_students(students):
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=4)

def add_student(students):
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    students.append({"id": sid, "name": name, "course": course})
    save_students(students)
    print("✅ Student Added Successfully!")

def view_students(students):
    if not students:
        print("❌ No students found.")
        return
    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Course: {s['course']}")

def search_student(students):
    sid = input("Enter Student ID to Search: ")
    for s in students:
        if s["id"] == sid:
            print(f"✅ Found: {s}")
            return
    print("❌ Student Not Found")

def delete_student(students):
    sid = input("Enter Student ID to Delete: ")
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            save_students(students)
            print("✅ Student Deleted Successfully!")
            return
    print("❌ Student Not Found")

def menu():
    students = load_students()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("✅ Exiting... Bye!")
            break
        else:
            print("❌ Invalid choice, try again!")

menu()
