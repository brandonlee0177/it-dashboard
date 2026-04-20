from datetime import datetime
import logging

def main():
    debug = False
    logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)

    APPNAME = "IT Dashboard"
    VERSION = "0.1.0"
    AUTHOR = "Brandon Lee"
    COPYRIGHT = "Copyright (c) 2026 Brandon Lee. All rights reserved."
    COURSENAME = "Programming for Technology Professionals - KUJAXCOP1034CD4-104062026"
    INSTRUCTORSNAME = "Professor Mora"
    ASSIGNMENTNAME = "Week 3 - IT Dashboard Starter Script"
    print("-------------------------------- ")
    print(f"Author: {AUTHOR}")
    print(f"{COPYRIGHT}")
    print("-------------------------------- ")
    print(f"Course: {COURSENAME}")
    print(f"Instructor: {INSTRUCTORSNAME}")
    print(f"Assignment: {ASSIGNMENTNAME}")
    print("-------------------------------- ")
    

    # Current time for header
    currenttime = datetime.now()

    # Employee data (strings; you can pull from a source as needed)
    emp1 = "Susan Meyers"
    emp1ID = 47899
    emp1Dept = "Accounting"
    emp1Pos = "Vice President"

    emp2 = "Mark Jones"
    emp2ID = 39119
    emp2Dept = "IT"
    emp2Pos = "Programmer"

    emp3 = "Joy Rogers"
    emp3ID = 81774
    emp3Dept = "Manufacturing"
    emp3Pos = "Engineer"

    def row(name, sid, dept, pos, widths):
        return f"{name:<{widths[0]}} | {sid:<{widths[1]}} | {dept:<{widths[2]}} | {pos:<{widths[3]}}"

    # Compute dynamic widths based on header names and data
    widths = (
        max(len("Employee Name"), len(emp1), len(emp2), len(emp3)),
        max(len("ID Number"), len(str(emp1ID)), len(str(emp2ID)), len(str(emp3ID) if 'emp3ID' in locals() else "")),
        max(len("Department"), len(emp1Dept), len(emp2Dept), len(emp3Dept)),
        max(len("Position"), len(emp1Pos), len(emp2Pos), len(emp3Pos)),
    )

    formattedtime = currenttime.strftime("%Y-%m-%d %H:%M:%S")

    with open("employeereport.txt", "w") as f:
        print(f"Report generated on: {formattedtime}", file=f)
        print("_____________________________________________________________", file=f)
        print("Employee Name | ID Number | Department    | Position", file=f)
        print("=============================================================", file=f)
        print(row(emp1, emp1ID, emp1Dept, emp1Pos, widths), file=f)
        print(row(emp2, emp2ID, emp2Dept, emp2Pos, widths), file=f)
        print(row(emp3, emp3ID, emp3Dept, emp3Pos, widths), file=f)
        print("=============================================================", file=f)
        print("End of employee report.", file=f)

if __name__ == "__main__":
    main()