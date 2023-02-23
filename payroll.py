import os
import shutil

employee_list = []
PAY_LOGFILE = "payroll.txt"


class Employee:
    def __init__(self, emp_id, first_name, last_name, address, city, state, zipcode, classification):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.classification = classification

    def make_salaried(self, salary):
        self.classification.classification = 1
        self.classification.salary = salary

    def make_hourly(self, hourly):
        self.classification.classification = 3
        self.classification.hourly = hourly

    def make_commission(self):
        self.classification.classification = 2


class Classification:
    def __init__(self, classification, salary, commission, hourly):
        self.classification = classification
        self.hours_worked = []
        self.salary = salary
        self.commission = commission
        self.hourly = hourly
        self.receipts = []

    def issue_payment(self, employee_lists):
        current_employee = None
        for i in employee_lists:
            if i.classification.classification == self.classification and i.classification.hourly == self.hourly \
                    and i.classification.commission == self.commission and i.classification.salary == self.salary:
                current_employee = i
        total_pay = 0
        if self.classification == 1:
            total_pay = self.salary
        elif self.classification == 2:
            total_pay = self.salary
            sales = 0
            for i in self.receipts:
                sales += float(i)
            total_pay += (sales * self.commission * .01)
        elif self.classification == 3:
            hours = 0
            for i in self.hours_worked:
                hours += float(i)
            total_pay = (hours * self.hourly)
        self.classification.hours_worked = []
        self.classification.receipts = []
        file = open("payroll.txt", 'a')
        file.write(
            f"Mailing {total_pay:0.2f} to {current_employee.first_name} {current_employee.last_name} at "
            f"{current_employee.address} {current_employee.city} {current_employee.state} {current_employee.zipcode}")
        return total_pay


def find_employee_by_id(employee, employee_lists):
    for j in employee_lists:
        if j.emp_id == employee:
            return j


def load_employees(employee_lists):
    file = open("employees.csv")
    employee_data = file.read()
    lines = employee_data.split("-")
    for i in range(len(lines) - 1):
        if i == 0:
            first_num = lines[0]
            lines.pop(0)
            lines[0] = first_num + "-" + lines[0]
        else:
            previous_string = lines[i - 1]
            previous_num = previous_string[-2] + previous_string[-1]
            lines[i] = previous_num + "-" + lines[i]
    for i in range(len(lines) - 1):
        lines[i] = lines[i][:-2].strip()
    for i in range(len(lines) - 1):
        more_lines = lines[i].split(',')
        real_classification = Classification(more_lines[7], more_lines[8], more_lines[9], more_lines[10])
        real_employee = Employee(more_lines[0], more_lines[1], more_lines[2], more_lines[3], more_lines[4],
                                 more_lines[5], more_lines[6], real_classification)
        employee_lists.append(real_employee)
    return employee_lists


def process_timecards(employee_lists):
    file = open("timecards.csv")
    hourly_data = file.read()
    lines = hourly_data.split()
    for i in lines:
        more_lines = i.split(",")
        current_employee = more_lines[0]
        a = find_employee_by_id(current_employee, employee_lists)
        a.classification.hours_worked.append(more_lines[1:])
    return employee_lists


def process_receipts(employee_lists):
    file = open("receipts.csv")
    receipt_data = file.read()
    lines = receipt_data.split()
    for i in lines:
        more_lines = i.split(",")
        current_employee = more_lines[0]
        a = find_employee_by_id(current_employee, employee_lists)
        a.classification.receipts.append(more_lines[1:])
    return employee_lists


def run_payroll(employee_lists):
    if os.path.exists(PAY_LOGFILE):  # pay_log_file is a global variable holding ‘payroll.txt’
        shutil.move("C:\Users\Donov\Documents\GitHub\DessertShop\payroll.txt",
                    "C:\Users\Donov\Documents\GitHub\DessertShop\old_payroll.txt")
    for emp in employee_lists:  # employees is the global list of Employee objects
        emp.issue_payment(employee_lists)  # issue_payment calls a method in the classification


def main():
    data = load_employees(employee_list)
    more_data = process_timecards(data)
    even_more_data = process_receipts(more_data)
    run_payroll(even_more_data)


if __name__ == "__main__":
    main()
