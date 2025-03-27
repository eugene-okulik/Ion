insert into students (name,second_name) values ('student','test');
insert into books (title,taken_by_student_id) values ('Mathematics',20000);
insert into books (title,taken_by_student_id) values ('Economy',20000);
insert into groups(title,start_date,end_date) values ('Automation Testers','Feb 2020','June 2020');
insert into subjets (title) values
('operation basic'),
('economy');
INSERT INTO lessons (title) VALUES 
('math base'),
('fundamental economy');
insert into marks (value) values (8),(10);


SELECT m.value AS mark, l.title AS lesson_title, s.title AS subject_title
FROM marks m
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets s ON l.subject_id = s.id
WHERE m.student_id = 20000;

SELECT b.title AS book_title
FROM books b
WHERE b.taken_by_student_id = 20000;

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
WHERE st.id = 20000;
