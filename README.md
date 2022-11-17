# EMPLOYEE MANAGEMENT SYSTEM

## Description:

The application is backend server of an "Employee Management System" of a company where the employees are \organized in
separate teams with one team leader per team.

- Every employee has an hourly rate they get paid for their work.
- Not everybody in the company is a full time employee. Their work can be either "Part Time" or "Full Time".
- An employee can have multiple combinations of part-time work arrangements.
- Team leaders are paid an additional 10% for their work.
- No employee can have a full-time(100%) work arrangement along with a part-time work arrangement.
- An employee can be the team leader of a different team other than the team he/she belongs to.
- No two cannot be the team leader of the same team.
- API for company accountant, retrieves the list of employees with their respective
  pay for the month based on their work arrangements and role (whether a team leader or not)

### Additional Features:

When an Employee or Team object is create their respective code is generated automatically in a sequential order using
signals. `EDI-EMP-ID`(eg: EDI-EMP-21) and `EDI-TM-ID`(eg: EDI-EMP-13) for Employee and Team objects respectively.

## Models:

### Employee Module

- [Employee](https://github.com/noulmon/edi_employee_management/blob/master/employee/models.py#L32-L57)
- [Team](https://github.com/noulmon/edi_employee_management/blob/master/employee/models.py#L13-L18)
- [Team Leader](https://github.com/noulmon/edi_employee_management/blob/master/employee/models.py#L87-L92)

### Work Module

- [Work Arrangement](https://github.com/noulmon/edi_employee_management/blob/master/work/models.py#L10-L30)
- [Employee Work Arrangement](https://github.com/noulmon/edi_employee_management/blob/master/work/models.py#L34-L55)

## API Endpoints:



### Employee

- `/employee/api/employees/` `POST`: creates a new employee.
- `/employee/api/employees/` `GET`: retrieves the list of all employees
- `/employee/api/employee/<pk>/` `GET`: retrieves the details of an employee with `id = <pk>`
- `/employee/api/employee/<pk>/` `PATCH`: updates the details of an employee with `id = <pk>`
- `/employee/api/employee/<pk>/` `DELETE`: deletes the employee instance with `id = <pk>`

### Team

- `/employee/api/teams/` `POST`: creates a new team
- `/employee/api/teams/` `GET`: retrieves the list of all teams
- `/employee/api/team/<PK>/` `GET`: retrieves the details of a team with `id = <pk>`
- `/employee/api/team/<PK>/` `PATCH`: updates the details of a team with `id = <pk>`
- `/employee/api/team/<PK>/` `DELETE`: deletes the team with `id = <pk>`

### Team Leader:

- `/employee/api/team_leaders/` `POST`: creates a new team leader.
- `/employee/api/team_leaders/` `GET`: retrieves the list of all team leaders
- `/employee/api/team_leader/<pk>/` `GET`: retrieves the details of a team leader with `id = <pk>`
- `/employee/api/team_leader/<pk>/` `PATCH`: updates the details of a team leader with `id = <pk>`
- `/employee/api/team_leader/<pk>/` `DELETE`: deletes the team leader with `id = <pk>`

### Work Arrangement:

- `/work/api/work_arrangements/` `POST`: creates a new work arrangement
- `/work/api/work_arrangements/` `GET`: retrieves the list of all work arrangements
- `/work/api/work_arrangements/<pk>>/` `GET`: retrieves the details of a work arrangement with `id = <pk>`
- `/work/api/work_arrangements/<pk>>/` `PATCH`: updates the details of a work arrangement with `id = <pk>`
- `/work/api/work_arrangements/<pk>>/` `DELETE`: deletes the work arrangement with `id = <pk>`

### Employee Work Arrangement:

- `/work/api/employee_work_arrangements/` `POST`: creates a new employee work arrangement
- `/work/api/employee_work_arrangements/` `GET`: retrieves the list of all employee work arrangements
- `/work/api/employee_work_arrangements/<pk>>/` `GET`: retrieves the details of an employee work arrangement
  with `id = <pk>`
- `/work/api/employee_work_arrangements/<pk>>/` `PATCH`: updates the details of an employee work arrangement
  with `id = <pk>`
- `/work/api/employee_work_arrangements/<pk>>/` `DELETE`: deletes the employee work arrangement with `id = <pk>`

### Employee Monthly Payment:

`/employee/api/payment_list/` `GET`: retrieves the list of employees with their respective pay for the month

### API Documentation(Swagger):
`/api/docs/` `GET`: Redirects to Swagger GUI for API documentation.


## To Run the Project:

1. Clone the project from git repository.
2. Create a python environment and activate it.
3. Got project directory. 
4. Install the required packages: `pip install requirements.txt`.
5. Run the project: `python manage.py runserver`.

## To Run Unit Tests:
`python manage.py test`: run the unit tests in the command line.

## To Generate the Test Coverage Report:
1. Run Coverage: `coverage run manage.py test`.
2. Generate a coverage report: `coverage report -m` (generates a coverage report in the commandline).
3. Generate an HTML coverage report: coverage html: `coverage html` (report can be found in _htmlcov/index.html_ in project root directory).

## Possible Future Enhancements in the Project:
- Add user authentication for the APIs.
- Restrict 'employee monthly payment list' to user with accounts role (and admins) only.
- Containerize(using Docker) the project to avoid the infrastructure dependency.
