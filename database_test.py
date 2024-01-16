import sqlite3

conn = sqlite3.connect('students.db')
# conn = sqlite3.connect('students.db', check_same_thread=False)

#build a cursor alias c
db = conn.cursor()

#Create a table
# c.execute("""CREATE TABLE customers (
#     first_name TEXT,
#     last_name TEXT,
#     email TEXT
# )        
# """)

# Insert single customers
# db.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?)", (2, "tim", "joseph", "tim", "pbkdf2:sha256:600000$ma8mabWloXgQ3y5I$edcc6ced43785d9be4c1ee0e3a1867bcf9f4180ef32952fdd2ebfa298c1ecb34", 0))

#insert Multiple customers
# many_customers = [
#     ('wes', 'brown', 'wes@emailcom'),
#     ('Stephanie', 'joe', 'stephanie@email.com')
#     ]
# db.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)

# john = 'John'
# Select'=
# db.execute("SELECT * FROM students WHERE user_name = ?", ('John',))
db.execute("SELECT * FROM students")
# print(db.fetchone())
# c.fetchmany()
# c.fetchall()
for customer in db.fetchall():
    print(customer)
    

# Commit our command
conn.commit()

# Close connection
conn.close()