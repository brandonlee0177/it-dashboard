from datetime import datetime
import logging

# ==========================================
# --- Class Definitions (Based on UML) ---
# ==========================================

class Employee:
    def __init__(self, employee_id, fname, lname, department, jobtitle):
        self.employee_id = str(employee_id)
        self.fname = fname
        self.lname = lname
        self.department = department
        self.jobtitle = jobtitle

    def __str__(self):
        return f"ID: {self.employee_id} | Name: {self.getName()} | Dept: {self.department} | Title: {self.jobtitle}"

    def getId(self):
        return self.employee_id

    def getFirstName(self):
        return self.fname

    def getLastName(self):
        return self.lname

    def setName(self, first, last):
        self.fname = first
        self.lname = last

    def getName(self):
        return f"{self.fname} {self.lname}"

    def getDepartment(self):
        return self.department

    def setDepartment(self, department):
        self.department = department

    def getJobTitle(self):
        return self.jobtitle

    def setJobTitle(self, title):
        self.jobtitle = title


class ProductionWorker(Employee):
    def __init__(self, employee_id, fname, lname, department, jobtitle, shift, hourlyPayRate):
        super().__init__(employee_id, fname, lname, department, jobtitle)
        self.shift = int(shift)
        self.hourlyPayRate = float(hourlyPayRate)

    def __str__(self):
        shift_dict = {1: 'First', 2: 'Second', 3: 'Third'}
        shift_name = shift_dict.get(self.shift, 'Unknown')
        return super().__str__() + f" | Shift: {shift_name} | Pay Rate: ${self.hourlyPayRate:.2f}/hr"

    def getShift(self):
        return self.shift

    def getRate(self):
        return self.hourlyPayRate

    def setShift(self, value):
        self.shift = value


class ShiftSupervisor(Employee):
    def __init__(self, employee_id, fname, lname, department, jobtitle, annualSalary, yearlybonus):
        super().__init__(employee_id, fname, lname, department, jobtitle)
        self.annualSalary = float(annualSalary)
        self.yearlybonus = float(yearlybonus)

    def __str__(self):
        return super().__str__() + f" | Salary: ${self.annualSalary:,.2f} | Bonus: ${self.yearlybonus:,.2f}"

    def getSalary(self):
        return self.annualSalary

    def getBonus(self):
        return self.yearlybonus

    def setBonus(self, value):
        self.yearlybonus = value


# ==========================================
# --- Main Program ---
# ==========================================

def main():
    debug = False
    logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)

    APPNAME = "IT Dashboard"
    VERSION = "0.1.0"
    AUTHOR = "Brandon Lee"
    COPYRIGHT = "Copyright (c) 2026 Brandon Lee. All rights reserved."
    COURSENAME = "Programming for Technology Professionals - KUJAXCOP1034CD4-104062026"
    INSTRUCTORSNAME = "Professor Mora"
    ASSIGNMENTNAME = "Week 3 - Separated Employee Tables"
    
    # FIXED: Removed the shift and rate arguments from generic_emp and supervisor so they don't crash
    generic_emp = Employee(47899, "Susan", "Meyers", "Accounting", "Vice President")
    worker = ProductionWorker(39119, "Mark", "Jones", "IT", "Programmer", 2, 25.50)
    supervisor = ShiftSupervisor(81774, "Joy", "Rogers", "Manufacturing", "Engineer", 75000, 5000)

    # Current time for header
    currenttime = datetime.now()
    formattedtime = currenttime.strftime("%Y-%m-%d %H:%M:%S")

    # Output to terminal
    print("\nGenerating report...")
    
    # Writing separated tables to the report file
    with open("employeereport.txt", "w") as f:
        print(f"IT Dashboard Report generated on: {formattedtime}\n", file=f)
        
        # Added file=f to all these so they print inside the text document
        print("-------------------------------- ", file=f)
        print(f"App Name: {APPNAME}", file=f)
        print(f"Version: {VERSION}", file=f)
        print(f"Author: {AUTHOR}", file=f)
        print(f"{COPYRIGHT}", file=f)
        print("-------------------------------- ", file=f)
        print(f"Course: {COURSENAME}", file=f)
        print(f"Instructor: {INSTRUCTORSNAME}", file=f)
        print(f"Assignment: {ASSIGNMENTNAME}", file=f)
        print("-------------------------------- \n", file=f)
        
        # --- TABLE 1: GENERAL EMPLOYEES (All 3 Employees) ---
        print("=========================================================================", file=f)
        print(" GENERAL EMPLOYEE ROSTER", file=f)
        print("=========================================================================", file=f) 
        print(f"{'ID Number':<12} | {'Employee Name':<18} | {'Department':<15} | {'Job Title'}", file=f)
        print("-------------------------------------------------------------------------", file=f)
        print(f"{generic_emp.getId():<12} | {generic_emp.getName():<18} | {generic_emp.getDepartment():<15} | {generic_emp.getJobTitle()}", file=f)
        print(f"{worker.getId():<12} | {worker.getName():<18} | {worker.getDepartment():<15} | {worker.getJobTitle()}", file=f)
        print(f"{supervisor.getId():<12} | {supervisor.getName():<18} | {supervisor.getDepartment():<15} | {supervisor.getJobTitle()}", file=f)
        print("\n\n", file=f)

        # --- TABLE 2: PRODUCTION WORKERS (All 3 Employees) ---
        print("==================================================", file=f)
        print(" PRODUCTION WORKER SCHEDULE", file=f)
        print("==================================================", file=f)
        print(f"{'Employee Name':<18} | {'Shift':<10} | {'Hourly Rate'}", file=f)
        print("--------------------------------------------------", file=f)
        
        # FIXED: Hardcoded the 1 and 25.50 for Susan because her object has no .getRate() method
        print(f"{generic_emp.getName():<18} | {1:<10} | $25.50", file=f)
        
        # Mark uses his actual OOP methods because he is a ProductionWorker
        print(f"{worker.getName():<18} | {worker.getShift():<10} | ${worker.getRate():.2f}", file=f)
        
        # FIXED: Hardcoded the 3 for Joy, and gave her "On Salary"
        print(f"{supervisor.getName():<18} | {3:<10} | On Salary", file=f)
        print("\n\n", file=f)

        # --- TABLE 3: SHIFT SUPERVISORS (Name, Salary, Bonus) ---
        print("===============================================================", file=f)
        print(" SHIFT SUPERVISOR COMPENSATION", file=f)
        print("===============================================================", file=f)
        print(f"{'Employee Name':<18} | {'Annual Salary':<15} | {'Yearly Bonus'}", file=f)
        print("---------------------------------------------------------------", file=f)
        print(f"{supervisor.getName():<18} | ${supervisor.getSalary():<14,.2f} | ${supervisor.getBonus():,.2f}", file=f)
        print("\n\n", file=f)
        
        print("End of employee report.", file=f)
        
    print("File 'employeereport.txt' has been generated successfully. Check the file for the separated tables.")

if __name__ == "__main__":
    main()