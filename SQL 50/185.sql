select
    Department.name as Department,
    emp1.name as Employee,
    emp1.salary
from
    Employee emp1 join Department
on
    emp1.departmentId = Department.Id
where
    3 > (
                        select
                            count(distinct emp2.salary)
                        from
                            Employee emp2
                        where
                            emp2.salary > emp1.salary
                            and
                            emp1.DepartmentId = emp2.DepartmentId
                            );