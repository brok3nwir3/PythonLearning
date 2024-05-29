# Python Classes - Project 5
# Author: Phil van der Linden
# Date: 05/28/2024

### Creating the seven classes. ###

# 1. An affiliate class.
# d. The affiliate class demonstrates hierarchical inheritance with students, employees, and alumni classes.
class affiliate:
    def __init__(self, affiliate_id, affiliate_name, affiliate_type):
        self.affiliate_id = affiliate_id #int 7 digit
        self.affiliate_name = affiliate_name #string
        self.affiliate_type = affiliate_type #string

    def print_affiliate(self):
        print("Affiliate information...\n"\
              "Affiliate ID",self.affiliate_id,\
              ", Affiliate Name:",self.affiliate_name,\
              ", Affiliate Type:",self.affiliate_type,"\n")

# 2. A student class.
# a. The student class demonstrates single inheritance from the affiliate class.
class student(affiliate):
    def __init__(self, student_id, student_year, affiliate_id, affiliate_name, affiliate_type):
        affiliate.__init__(self, affiliate_id, affiliate_name, affiliate_type)
        self.student_id = student_id #int 7 digit
        self.student_year = student_year #int 1-5

    def print_student(self):
        print("Student information...\n"\
              "Student ID", self.student_id,\
              ", Student Year:",self.student_year,\
              ", Affiliate ID",self.affiliate_id,\
              ", Affiliate Name:",self.affiliate_name,\
              ", Affiliate Type:",self.affiliate_type,"\n")

# 3. An employee class.
class employee(affiliate):
    def __init__(self, employee_id, department, affiliate_id, affiliate_name, affiliate_type):
        affiliate.__init__(self, affiliate_id, affiliate_name, affiliate_type)
        self.employee_id = employee_id #int 7 digit
        self.department = department

    def print_employee(self):
        print("Employee information...\n"\
              "Employee ID", self.employee_id,\
              ", Department:",self.department,\
              ", Affiliate ID",self.affiliate_id,\
              ", Affiliate Name:",self.affiliate_name,\
              ", Affiliate Type:",self.affiliate_type,"\n")

# 4. A professor class.
class professor(employee):
    def __init__(self, subject, employee_id, department, affiliate_id, affiliate_name, affiliate_type):
        employee.__init__(self, employee_id, department, affiliate_id, affiliate_name, affiliate_type)
        self.subject = subject

    def print_professor(self):
        print("Professor information...\n"\
              "Subject Area:",self.subject,\
              ", Employee ID", self.employee_id,\
              ", Department:",self.department,\
              ", Affiliate ID",self.affiliate_id,\
              ", Affiliate Name:",self.affiliate_name,\
              ", Affiliate Type:",self.affiliate_type,"\n")

# 5. An adjunct class.
# c. The adjunct class demonstrates multilevel inheritance from the affiliate, employee, and projessor classes.
class adjunct(professor):
    def __init__(self, term_date, subject, employee_id, department, affiliate_id, affiliate_name, affiliate_type):
        professor.__init__(self, subject, employee_id, department, affiliate_id, affiliate_name, affiliate_type)
        self.term_date = term_date

    def print_adjunct(self):
        print("Adjunct information...\n"\
              "Termination Date:", self.term_date,\
              ", Subject Area:",self.subject,\
              ", Employee ID", self.employee_id,\
              ", Department:",self.department,\
              ", Affiliate ID",self.affiliate_id,\
              ", Affiliate Name:",self.affiliate_name,\
              ", Affiliate Type:",self.affiliate_type,"\n")

# 6. A student_worker class.
# b. The student_worker class demonstrates multiple inheritance from the employee class and student class.
class student_worker(employee, student):
    def __init__(self, internship, student_id, student_year, affiliate_id, affiliate_name, affiliate_type, employee_id, department):
        # Multiple inheritance from the employee and student classes.
        employee.__init__(self, employee_id, department, affiliate_id, affiliate_name, affiliate_type)
        student.__init__(self, student_id, student_year, affiliate_id, affiliate_name, affiliate_type)
        self.internship = internship # True/False

    # Function to calculate student worker pay.
    def student_pay(self):
        print("The pay for student worker", self.affiliate_name, "is $", 5 + (self.student_year * 5), "/hr.")

    def print_student_worker(self):
        print("Student worker information... \n"
              "Internship Worker:",self.internship,\
              ", Student ID:",self.student_id,\
              ", Student Year:",self.student_year,\
              ", Employee ID:",self.employee_id,\
              ", Employee Dept.",self.department,"\n")
        

# 7. An alumni class.
class alumni(affiliate):
    def __init__(self, alumni_year, affiliate_id, affiliate_name, affiliate_type):
        # Single inheritance from the affiliate class (parent).
        super().__init__(affiliate_id, affiliate_name, affiliate_type)
        self.alumni_year = alumni_year #int 4 digit.

    def print_alumni(self):
        print("Alumni information...\n"
              "Graduating Year:",self.alumni_year,\
              ", Affiliate Name:",self.affiliate_name,\
              ", Affiliate ID:", self.affiliate_id,\
              ", Affiliate Type:", self.affiliate_type,"\n")


### Creating objects for the seven classes, and calling echo print functions. ###

student1 = student(1111111, 3, 1111111, 'Kristen, Simmons', 'Student')
student1.print_student()

alumni1 = alumni(1991, 2222222, 'John, Doe', 'Graduate')
alumni1.print_alumni()

employee1 = employee(3333333, 'Technology', 3333333, 'Jack, Jillerson', 'Staff')
employee1.print_employee()

professor1 = professor('Economics', 4444444, 'Business', 4444444, 'Guy, Persons', 'Professor')
professor1.print_professor()

adjunct1 = adjunct('01012021', 'Chemistry', 5555555, 'Science', 5555555, 'Greggory, Hamburger', 'Adjunct')
adjunct1.print_adjunct()

student_worker1 = student_worker(True, 6666666, 2, 6666666, 'Sally, Seagull', 'Student', 6666666, 'Science')
student_worker1.print_student_worker()

affiliate1 = affiliate(7777777, 'Pencil Co.', 'Vendor')
affiliate1.print_affiliate()


### Calling other class functions. ###

student_worker1.student_pay()