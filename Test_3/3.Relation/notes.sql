1. Creating a table

CREATE TABLE table_name (
    column_name data_type constraints,
    column_name data_type constraints,
    PRIMARY KEY (column_name)
);



2. INSERTING

INSERT INTO table_name (column1, column2, ...)
VALUES
    (value1, value2, ...),
    (value1, value2, ...),
    (value1, value2, ...);


3. 

INT

DECIMAL / NUMERIC

FLOAT / REAL

CHAR

VARCHAR

DATE

TIME

TIMESTAMP

BOOLEAN

BLOB

NULL


4. Queries all data_type

SELECT * FROM LOCATION


5. Removing a table

DROP TABLE LOCATION


6. Specifying that an attribute must be set

CREATE TABLE table_name (
    column_name data_type NOT NULL,
    column_name data_type NOT NULL,
    PRIMARY KEY (column_name)
);

