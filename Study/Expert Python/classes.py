import datetime


class Employee:
    tax_amount = 0.27
    raise_amount = 1.02
    num_of_employees = 0

    def __init__(self, firstname, lastname, age, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = firstname + "." + lastname + "@company.com"
        self.salary = salary

        Employee.num_of_employees += 1

    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    def apply_raise(self):
        salary_raise = float(self.salary) * self.raise_amount
        return salary_raise

    def tax(self):
        tax_am = float(self.apply_raise()) * self.tax_amount
        return round(tax_am, 2)

    def net_calc(self):
        net = float(self.apply_raise()) - self.tax()
        return net

    def info(self):
        return f"Name: {self.fullname()}\n" \
               f"Age: {self.age}\n" \
               f"Email: {self.email}\n" \
               f"Base Salary: ${self.salary}\n" \
               f"Raise amount: {self.raise_amount}\n" \
               f"Raised Salary: ${self.apply_raise()}\n" \
               f"Tax amount: ${self.tax()}\n" \
               f"Net wage: ${self.net_calc()}"

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        firstname, lastname, age, salary = emp_str.split(' ')  # Splitting the (Attila Szucs 20 120000) to 4 segment
        return cls(firstname, lastname, age, salary)  # This is creating a new employee

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return "Not workday!"
        return "Workday"


class Developer(Employee):
    raise_amount = 1.10  # Update raise amount just for Developers


class Employer:
    def __init__(self, ceo, company):
        self.ceo = ceo
        self.company = company


# Creating Employee's and Employer's (mode 1)
employer = Employer("Krypton", "Kryptonite Corp.")

# Creating Employee's (mode 1)
# emp_1 = Employee("Attila", "Szucs", 20, 120000)
# emp_2 = Employee("Henrietta", "Molnar", 18, 100000)

# Creating Employee's (mode 2)
Dev1 = "Attila Szucs 20 120000"
Emp1 = "Henrietta Molnar 18 95000"
Emp2 = "Péter Pálma 35 115000"

new_emp_1 = Developer.from_string(Dev1)
new_emp_2 = Employee.from_string(Emp1)
new_emp_3 = Employee.from_string(Emp2)

Employee.set_raise_amount(1.05)  # Update raise amount

# Define today's date
current_date = datetime.date.today()

print(f"\n{new_emp_1.info()}\n\n{new_emp_2.info()}\n\n{new_emp_3.info()}\n"
      f"\nNumber of employees: {Employee.num_of_employees}\n"
      f"Today is: {current_date} - {Employee.is_workday(current_date)}")