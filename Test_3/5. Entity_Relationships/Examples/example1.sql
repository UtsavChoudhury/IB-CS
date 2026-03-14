CREATE TABLE teacher (
       teacher_email VARCHAR PRIMARY KEY,
       name VARCHAR NOT NULL);

CREATE TABLE course (
       id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
       topic VARCHAR NOT NULL,
       teacher_email VARCHAR REFERENCES teacher(teacher_email));