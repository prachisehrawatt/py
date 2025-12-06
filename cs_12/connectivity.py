
import mysql.connector

con = mysql.connector.connect(
    unix_socket="/var/run/mysqld/mysqld.sock",
    user="root",
    password="yourpassword",
    database="PRACHI"
)
cursor = con.cursor()

query = """
SELECT STUDENT.ADMNO, STUDENT.NAME, STUDENT.CLASS, FEES.AMOUNT
FROM STUDENT
JOIN FEES
ON STUDENT.ADMNO = FEES.ADMNO
"""

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print(row)

con.close()


