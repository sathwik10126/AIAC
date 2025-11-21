/* ==========================================================
   LIBRARY MANAGEMENT SYSTEM - FIXED SQL SCRIPT (MySQL)
   Includes:
   1. Table Creation (books, members, loans)
   2. Sample Data Insert (available + borrowed books)
   3. Query: Overdue Books
   4. Query: Most Popular Author (fixed)
   =========================================================*/

-- Use a database (create if you want)
CREATE DATABASE IF NOT EXISTS library_fixed;
USE library_fixed;

-- ===============================
-- 1. CREATE TABLES
-- ===============================

DROP TABLE IF EXISTS loans;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS books;

CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(150) NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    publication_year INT,
    available_copies INT DEFAULT 0
);

CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    join_date DATE NOT NULL DEFAULT (CURRENT_DATE),
    membership_type ENUM('Regular','Premium') DEFAULT 'Regular'
);

CREATE TABLE loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    loan_date DATE NOT NULL DEFAULT (CURRENT_DATE),
    due_date DATE NOT NULL,
    return_date DATE NULL,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);

-- ===============================
-- 2. INSERT SAMPLE DATA
-- ===============================

INSERT INTO books (title, author, isbn, publication_year, available_copies) VALUES
('Atomic Habits', 'James Clear', '9780735211292', 2018, 3),
('The Alchemist', 'Paulo Coelho', '9780061122415', 1993, 2),
('1984', 'George Orwell', '9780451524935', 1949, 0),
('The Pragmatic Programmer', 'Andrew Hunt', '9780201616224', 1999, 1);

INSERT INTO members (name, email, join_date, membership_type) VALUES
('Alice Johnson', 'alice@example.com', '2022-01-10', 'Regular'),
('Bob Smith', 'bob@example.com', '2023-02-14', 'Premium'),
('Charlie Brown', 'charlie@example.com', '2021-11-20', 'Regular');

-- Loans (mix)
INSERT INTO loans (book_id, member_id, loan_date, due_date, return_date) VALUES
(1, 1, '2024-01-01', '2024-01-15', '2024-01-14'),
(2, 2, '2024-01-10', '2024-01-20', NULL),
(3, 3, '2023-12-20', '2024-01-05', NULL);

-- ===============================
-- 3. QUERY: FIND OVERDUE BOOKS
-- ===============================

SELECT
    l.loan_id,
    b.title AS book_title,
    m.name AS member_name,
    l.loan_date,
    l.due_date,
    DATEDIFF(CURDATE(), l.due_date) AS days_overdue
FROM loans l
JOIN books b ON l.book_id = b.book_id
JOIN members m ON l.member_id = m.member_id
WHERE l.return_date IS NULL
  AND l.due_date < CURDATE()
ORDER BY l.due_date ASC;

-- ===============================
-- 4. QUERY: MOST POPULAR AUTHOR (FIXED)
-- ===============================

-- Simple: top author by loan count
SELECT 
    b.author,
    COUNT(l.loan_id) AS total_loans
FROM loans l
JOIN books b ON l.book_id = b.book_id
GROUP BY b.author
ORDER BY total_loans DESC
LIMIT 1;

-- To return all authors tied for first place (optional):
-- SELECT author, total_loans FROM (
--   SELECT b.author, COUNT(l.loan_id) AS total_loans
--   FROM loans l
--   JOIN books b ON l.book_id = b.book_id
--   GROUP BY b.author
-- ) t
-- WHERE total_loans = (
--   SELECT MAX(total_loans) FROM (
--     SELECT COUNT(l2.loan_id) AS total_loans
--     FROM loans l2
--     JOIN books b2 ON l2.book_id = b2.book_id
--     GROUP BY b2.author
--   ) x
-- );

-- End of fixed script
