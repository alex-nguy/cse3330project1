# CSE3330 Project 1
Group Members Alexander Nguyen, Myles Guiam, Andy Vu, An Nguyen

## Motivation
In this project, the group started on how to use a relational DBMS. We used SQLite for creating tables, populating them with data, and querying
the tables.

## Technologies & Installation
This project is created using:
* [Python3](https://www.python.org/)
* [SQLite3](https://www.sqlite.org/index.html)

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
