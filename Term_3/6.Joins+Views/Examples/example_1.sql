CREATE TABLE IF NOT EXISTS teacher (
       teacher_email VARCHAR PRIMARY KEY,
       name VARCHAR NOT NULL);

CREATE TABLE IF NOT EXISTS course (
       course_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
       topic VARCHAR NOT NULL,
       teacher_email VARCHAR REFERENCES teacher(teacher_email));

CREATE TABLE IF NOT EXISTS student (
       student_email VARCHAR PRIMARY KEY,
       name VARCHAR NULL NULL);

CREATE TABLE IF NOT EXISTS enrollment (
       course_id INTEGER,
       student_email VARCHAR,
       PRIMARY KEY (course_id, student_email),
       FOREIGN KEY (course_id) REFERENCES course(course_id),
       FOREIGN KEY (student_email) REFERENCES student(student_email));

INSERT INTO teacher VALUES
       ('f@brilliant.org', 'Farid'),
       ('w@sports.org', 'Wiltsu');

INSERT INTO courses (topic, teacher_email) VALUES
       ('differentiation', 'f@brilliant.com'),
       ('vectors', 'w@sports.org');
