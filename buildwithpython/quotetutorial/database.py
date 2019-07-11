import sqlite3

conn = sqlite3.connect('myquotes.db')
curr = conn.cursor()

# Perintah dibawah ini hanya sekali dilakukan

# curr.execute("""create table quotes_tb(
#     title text,
#     author text,
#     tag text
#     )""")

curr.execute("""insert into quotes_tb values ('python is awesome','buildwithpython','python')""")

conn.commit()
conn.close()