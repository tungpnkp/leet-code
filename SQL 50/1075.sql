select project_id, round(sum(Employee.experience_years)/count(*), 2) as average_years from Project inner join Employee on Project.employee_id = Employee.employee_id
group by project_id