import sqlite3

conn = sqlite3.connect('student.db')
c = conn.cursor()

# Create tables
c.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS enrollments (student_id INTEGER, subject TEXT, mark INTEGER)")

# Insert student and get ID
c.execute("INSERT INTO students (name) VALUES ('ANNA SHARMA')")
sid = c.lastrowid

# Insert subjects and marks
data = [(sid, 'Python', 95), (sid, 'Math', 88), (sid, 'Physics', 92)]
c.executemany("INSERT INTO enrollments VALUES (?, ?, ?)", data)
conn.commit()

# Show results
for name, subject, mark in c.execute('''
    SELECT s.name, e.subject, e.mark
    FROM students s JOIN enrollments e ON s.id = e.student_id
    WHERE s.id = ?''', (sid,)):
    print(f"Name: {name}, Subject: {subject}, Mark: {mark}")

conn.close()
