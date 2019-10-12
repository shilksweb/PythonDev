import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""create table employees (
#     first text,
#     last text,
#     payment integer
#     )""")

# c.execute("insert into employees values ('Sushil', 'Singh', 1234)")

c.execute("Select * from employees")
print(c.fetchall())


conn.commit()

conn.close()