# CSE3330 Project 1
Group Members Alexander Nguyen, Myles Guiam, Andy Vu, An Nguyen

## Motivation
In this project, the group started on how to use a relational DBMS. We used SQLite for creating tables, populating them with data, and querying
the tables.

#### Requirements
1. Create the following tables specified in the textbook(Figure 3.2): EMPLOYEE,
DEPARTMENT, PROJECT, WORKS_ON, DEPT_LOCATIONS.
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
  Enter First Name:
  Enter Last Name:
  Enter a department to find their total salary:
```

## Example
When ran with test cases:
* Research
* James Borg
* Research

Should output the following:
```
  Enter department to find all employees and salaries: Research
  [('Research', 'Franklin', 40000), ('Research', 'John', 30000), ('Research', 'Ramesh', 38000), ('Research', 'Joyce', 25000), ('Research', 'Michael', 73500), ('Research', 'Andrea', 65000), ('Research', 'James', 75000)]
  Enter First Name: James
  Enter Last Name: Borg
  [('Reorganization', 5)]
  Enter a department to find their total salary: Research
  [(346500,)]
```
