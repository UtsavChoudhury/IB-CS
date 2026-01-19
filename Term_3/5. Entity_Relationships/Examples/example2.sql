CREATE TABLE teacher (
       teacher_email VARCHAR PRIMARY KEY,
       name VARCHAR NOT NULL);

CREATE TABLE course (
       course_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
       topic VARCHAR NOT NULL,
       teacher_email VARCHAR REFERENCES teacher(teacher_email));

CREATE TABLE student (
       student_email VARCHAR PRIMARY KEY,
       name VARCHAR NULL NULL);

CREATE TABLE enrollment (
       course_id INTEGER,
       student_email VARCHAR,
       PRIMARY KEY (course_id, student_email),
       FOREIGN KEY (course_id) REFERENCES course(course_id), -- alternative FK
       FOREIGN KEY (student_email) REFERENCES student(student_email));

CREATE TABLE product (
       product_id INTEGER PRIMARY KEY,
       stock INTEGER NOT NULL);

CREATE TABLE purchase (
       purchase_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
       product_id INTEGER REFERENCES product(product_id),
       quantity INTEGER NOT NULL);

INSERT INTO product VALUES (1, 100), (2, 50);

INSERT INTO purchase (product_id, quantity) VALUES (1, 10);
UPDATE product SET stock = stock - 10 WHERE product_id = 1;
