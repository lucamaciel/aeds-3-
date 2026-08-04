-- TP1: esquema de exemplo e consultas de verificação (Trabalho Prático 1)
-- Cria tabelas simples para um sistema de biblioteca

CREATE TABLE Author (
  author_id SERIAL PRIMARY KEY,
  name VARCHAR(200) NOT NULL
);

CREATE TABLE Book (
  book_id SERIAL PRIMARY KEY,
  title VARCHAR(300) NOT NULL,
  author_id INTEGER REFERENCES Author(author_id),
  year INT
);

-- Consulta de exemplo: livros por autor
SELECT a.name, b.title, b.year
FROM Author a
JOIN Book b ON b.author_id = a.author_id
ORDER BY a.name, b.year DESC;
