insert into students (id,name,second_name,group_id) values (20000,'student','test',50000);
insert into books (id,title,taken_by_student_id) values (5,'Mathematics',50000);
insert into books (id,title,taken_by_student_id) values (6,'Economy',50000);
insert into groups(id,title,start_date,end_date) values (50000,'Automation Testers','Feb 2020','June 2020');
insert into subjets (id,title) values
(10001,'operation basic'),
(10002,'economy');
INSERT INTO lessons (title,subject_id) VALUES 
('math base',10001),
('fundamental economy',10002);
insert into marks (value,lesson_id,student_id) values (8,10001,50000),(10,10002,50000);


SELECT m.value AS mark, l.title AS lesson_title, s.title AS subject_title
FROM marks m
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets s ON l.subject_id = s.id
WHERE m.student_id = 50000;

SELECT b.title AS book_title
FROM books b
WHERE b.taken_by_student_id = 50000;

SELECT 
    st.name AS student_name,
    st.second_name AS student_second_name,
    g.title AS group_title,
    g.start_date AS group_start_date,
    g.end_date AS group_end_date,
    b.title AS book_title,
    m.value AS mark,
    l.title AS lesson_title,
    s.title AS subject_title
FROM students st
LEFT JOIN groups g ON st.group_id = g.id
LEFT JOIN books b ON st.id = b.taken_by_student_id
LEFT JOIN marks m ON st.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjets s ON l.subject_id = s.id
WHERE st.id = 50000;
