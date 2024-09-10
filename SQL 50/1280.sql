# Write your MySQL query statement below



select tmp2.student_id,
tmp2.student_name,
tmp2.subject_name,
(
    case when tmp.cnt is null then 0
    else tmp.cnt end
    ) as attended_exams
from
(select student_id, 
student_name,
subject_name,
order_number
from Students, 
(SELECT subject_name, ROW_NUMBER() OVER (ORDER BY subject_name) AS order_number from  Subjects) as subject_order
) as tmp2
left join (select student_id, subject_name, count(*) as cnt from Examinations group by student_id, subject_name) as tmp
on tmp2.student_id = tmp.student_id and tmp2.subject_name = tmp.subject_name
order by tmp2.student_id asc , tmp2.order_number asc



