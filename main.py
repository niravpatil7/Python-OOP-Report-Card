# Base class to demonstrate basic inheritance
class Person:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

# Student class inheriting from Person
class Student(Person):
    def __init__(self, name, student_id):
        # Call the constructor of the parent class
        super().__init__(name, student_id)
        # Dictionary to store subjects and their corresponding grades
        self.grades = {} 

    # Method to add or update a grade
    def add_or_update_grade(self, subject, grade):
        self.grades[subject] = grade
        print(f"Success: Recorded {grade} for {self.name} in {subject}.")

    # Method to display the formatted report card
    def display_report_card(self):
        print("\n" + "="*40)
        print("          STUDENT REPORT CARD          ")
        print("="*40)
        print(f"Student Name : {self.name}")
        print(f"Student ID   : {self.student_id}")
        print("-" * 40)
        
        if not self.grades:
            print("No grades recorded yet.")
        else:
            print("SUBJECT GRADES:")
            for subject, grade in self.grades.items():
                print(f"  * {subject.ljust(20)}: {grade}")
        print("="*40 + "\n")


# --- Demonstration of the System ---
if __name__ == "__main__":
    # 1. Add student details
    student1 = Student("Ransh", "CE2024-042")

    # 2. Add grades
    student1.add_or_update_grade("Engineering Mathematics-I", "A")
    student1.add_or_update_grade("Engineering Physics", "B+")
    student1.add_or_update_grade("Basic Electronics", "A+")

    # Update an existing grade
    student1.add_or_update_grade("Engineering Physics", "A")

    # 3. Display the report card
    student1.display_report_card()