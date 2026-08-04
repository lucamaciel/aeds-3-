-- Exemplo de esquema relacional para exercícios
CREATE TABLE Student (
  student_id SERIAL PRIMARY KEY,
  name VARCHAR(150),
  matricula VARCHAR(50) UNIQUE
);

CREATE TABLE Course (
  course_id SERIAL PRIMARY KEY,
  code VARCHAR(20) UNIQUE,
  title VARCHAR(200)
);

CREATE TABLE Enrollment (
  enrollment_id SERIAL PRIMARY KEY,
  student_id INT REFERENCES Student(student_id),
  course_id INT REFERENCES Course(course_id),
  grade NUMERIC(4,2)
);

-- Exemplo de consulta: média por disciplina
SELECT c.code, c.title, AVG(e.grade) as avg_grade
FROM Course c
JOIN Enrollment e ON e.course_id = c.course_id
GROUP BY c.course_id, c.code, c.title;
