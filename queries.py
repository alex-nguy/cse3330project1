import sqlite3

departmentfile = open("./entryfiles/DEPARTMENT.txt", "r")
deptloc = open("./entryfiles/DEPT_LOCATIONS.txt", "r")
employeefile = open("./entryfiles/EMPLOYEE.txt", "r")
projectfile = open("./entryfiles/PROJECT.txt", "r")
worksonfile = open("./entryfiles/WORKS_ON.txt", "r")

conn = sqlite3.connect('project.db')
c = conn.cursor()

# Requirement 2
for x in departmentfile:
    depart = x.replace("'", "").rstrip().split(", ")
    c.execute("INSERT INTO DEPARTMENT VALUES(:Dname, :Dnumber, :Mgr_ssn, :Mgr_start_date)", {'Dname':depart[0], 'Dnumber':depart[1], 'Mgr_ssn':depart[2], 'Mgr_start_date':depart[3]})

for x in deptloc:
    dept = x.replace("'", "").rstrip().split(", ")
    c.execute("INSERT INTO DEPT_LOCATIONS VALUES(:Dnumber, :Dlocation)", {'Dnumber': dept[0], 'Dlocation': dept[1]})

for x in employeefile:
    employ = x.replace("'", "").rstrip().split(", ")
    c.execute("INSERT INTO EMPLOYEE VALUES(:Fname, :Minit, :Lname, :Ssn, :Bdate, :Address, :Sex, :Salary, :Super_ssn, :Dno)", {'Fname': employ[0], 'Minit': employ[1], 'Lname':employ[2], 'Ssn':employ[3], 'Bdate': employ[4], 'Address': employ[5], 'Sex': employ[6], 'Salary': employ[7], 'Super_ssn': employ[8], 'Dno': employ[9]})

for x in projectfile:
    project = x.replace("'", "").strip().split(",")
    c.execute("INSERT INTO PROJECT VALUES(:Pname, :Pnumber, :Plocation, :Dnum)", {'Pname': project[0], 'Pnumber': project[1], 'Plocation': project[2], 'Dnum': project[3]})

for x in worksonfile:
    works = x.replace("'", "").rstrip().split(", ")
    c.execute("INSERT INTO WORKS_ON VALUES(:Essn, :Pno, :Hours)", {'Essn': works[0], 'Pno': works[1], 'Hours': works[2]})


# Requirement 4
myDname = input("Enter department to find all employees and salaries: ")
c.execute("SELECT EMPLOYEE.Fname, EMPLOYEE.Minit, EMPLOYEE.Lname, EMPLOYEE.Salary FROM DEPARTMENT, EMPLOYEE WHERE EMPLOYEE.Dno = DEPARTMENT.Dnumber AND DEPARTMENT.Dname =:Dname", {'Dname': myDname})
print(c.fetchall())

# Requirement 5
print("Find an employee's project name and their salary.")
myFname = input("Enter first name: ")
myLname = input("Enter last name: ")
c.execute("SELECT PROJECT.Pname, WORKS_ON.Hours FROM PROJECT, WORKS_ON, EMPLOYEE WHERE EMPLOYEE.Ssn = WORKS_ON.Essn AND (EMPLOYEE.Fname = :Fname and EMPLOYEE.Lname = :Lname) AND WORKS_ON.Pno = PROJECT.Pnumber", {'Fname': myFname, 'Lname': myLname})
print(c.fetchall())

# Requirement 6
myDep = input("Enter a department to find their total salary: ")
c.execute("SELECT sum(salary) FROM EMPLOYEE, DEPARTMENT WHERE Dno = Dnumber and Dname = :Dname", {'Dname': myDep})
print(c.fetchall())

# Requirement 7
print("Department Population: ")
c.execute("SELECT DEPARTMENT.Dname, COUNT(*) FROM EMPLOYEE, DEPARTMENT WHERE EMPLOYEE.Dno = DEPARTMENT.Dnumber GROUP BY EMPLOYEE.Dno ORDER BY COUNT(*) DESC")
print(c.fetchall())

# Requirement 8
print("Employee Supervisors: ")
c.execute("SELECT S.Fname, S.Lname, COUNT(*) FROM EMPLOYEE AS S, EMPLOYEE AS E WHERE S.Ssn = E.Super_ssn GROUP BY E.Super_ssn ORDER BY COUNT(*) DESC, S.Fname ASC")
print(c.fetchall())

c.execute("DELETE FROM DEPARTMENT")
c.execute("DELETE FROM DEPT_LOCATIONS")
c.execute("DELETE FROM EMPLOYEE")
c.execute("DELETE FROM PROJECT")
c.execute("DELETE FROM WORKS_ON")

conn.commit()
conn.close()