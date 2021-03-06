# CSE3330 Project 1
Group Members: Alexander Nguyen, Myles Guiam, Andy Vu, An Nguyen<br/>
Myles Guiam: Created each of the Tables<br/>
Andy Vu and An Nguyen: Populated the tables with INSERT statements<br/>
Alexander Nguyen: Queried the database with the SELECT statements<br/>

## Motivation
In this project, the group started on how to use a relational DBMS. We used SQLite for creating tables, populating them with data, and querying
the tables.

#### Requirements
1. Create the following tables specified in the textbook(Figure 3.2): EMPLOYEE,
DEPARTMENT, PROJECT, WORKS_ON, DEPT_LOCATIONS. <br/><img src="https://github.com/amusealex/cse3330project1/blob/main/images/Figure3-2.PNG"/>
2. Load the records that will be provided to you into each of the tables that you created.
3. Write SQL queries OR use a simple Web interfaces to get the results of the following
queries:
4. Enter a department name, and retrieve all the names and salaries of all employees who work
in that department.
5. Enter an employee last name and first name and retrieve a list of projects names/hours per
week that the employee works on.
6. Enter a department name and retrieve the total of all employee salaries who work in the
department.
7. For each department, retrieve the department name and the number (count) of employees
who work in that department. Order the result by number of employees in descending order.
8. For each employee who is a supervisor, retrieve the employee first and last name and the
number (count) of employees that are supervised. Order the result in descending order.

## Technologies & Installation
This project is created using:
* [Python3](https://www.python.org/)
* [SQLite3](https://www.sqlite.org/index.html)
* [DB Browswer for SQLite](https://sqlitebrowser.org/)

## Usage
When ran the program will prompt the user the following:
```
  Enter department to find all employees and salaries: 
  Find an employee's project name and their salary.
  Enter first name:
  Enter last name:
  Enter a department to find their total salary:
  Department Population: 
  Employee Supervisors: 
```

## Example
When ran with test cases:
* Research
* Alex Freed
* Administration

Should output the following:
```
  Enter department to find all employees and salaries: Research
  Employee Name             | Employee Salary
  Franklin T. Wong          |     $40000
  John B. Smith             |     $30000
  Ramesh K. Narayan         |     $38000
  Joyce A. English          |     $25000
  Michael A. Morgan         |     $73500
  Andrea M. Sondrini        |     $65000
  James U. Miller           |     $75000

  Find an employee's project name and their salary.
  Enter first name: Alex
  Enter last name: Freed
  Alex Freed's Projects     | Hours Spent
  InkjetPrinters            | 40 Hours

  Enter a department to find their total salary: Administration
  Department                | Total Salary
  Administration            |  $330500

  Department Population:
  Department                | Total Employees
  Sales                     |     $18
  Software                  |     $16
  Hardware                  |     $14
  HR                        |     $7
  Research                  |     $7
  Administration            |     $6
  Headquarters              |     $2
  Networking                |     $1

  Employee Supervisors:
  Supervisors               | Employees Supervised
  Alex Freed                | 7 Employees
  Bob Bender                | 4 Employees
  Jared James               | 4 Employees
  Roy Lewallen              | 4 Employees
  Evan Wallis               | 3 Employees
  Franklin Wong             | 3 Employees
  James Borg                | 3 Employees
  John James                | 3 Employees
  Kate King                 | 3 Employees
  Jennifer Wallace          | 2 Employees
  Josh Zell                 | 2 Employees
  Juan Linda                | 2 Employees
  Lyle Leslie               | 2 Employees
  Nandita Ball              | 2 Employees
  Red Bacher                | 2 Employees
  Sammy Hall                | 2 Employees
  Ahmad Jabbar              | 1 Employees
  Alec Best                 | 1 Employees
  Billie King               | 1 Employees
  Bonnie Bays               | 1 Employees
  Carl Reedy                | 1 Employees
  Gerald Small              | 1 Employees
  Jill Jarvis               | 1 Employees
  John Smith                | 1 Employees
  John Ed                   | 1 Employees
  Kim Grace                 | 1 Employees
  Naveen Drew               | 1 Employees
  Sam Snedden               | 1 Employees
```
