# Emotion-Based Student Wellness Tracker

import mysql.connector
from datetime import date

# ---------- DATABASE CONNECTION ----------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="wellness_db"
)

cursor = conn.cursor()

# ---------- CLASS DEFINITION ----------
class WellnessTracker:

    def add_student(self):
        sid = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        clas = input("Enter Class: ")

        query = "INSERT INTO students VALUES (%s, %s, %s)"
        cursor.execute(query, (sid, name, clas))
        conn.commit()
        print("Student added successfully")

    def add_daily_entry(self):
        sid = int(input("Enter Student ID: "))
        mood = input("Enter Mood (Happy/Neutral/Tired): ")
        hours = int(input("Enter Study Hours: "))

        query = "INSERT INTO daily_log (student_id, log_date, mood, study_hours) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (sid, date.today(), mood, hours))
        conn.commit()
        print("Daily wellness entry added")

    def view_report(self):
        sid = int(input("Enter Student ID: "))
        query = "SELECT log_date, mood, study_hours FROM daily_log WHERE student_id=%s"
        cursor.execute(query, (sid,))
        records = cursor.fetchall()

        print("\nDATE\t\tMOOD\tSTUDY HOURS")
        for row in records:
            print(row[0], "\t", row[1], "\t", row[2])

    def weekly_summary(self):
        sid = int(input("Enter Student ID: "))
        query = "SELECT mood, study_hours FROM daily_log WHERE student_id=%s AND log_date >= CURDATE() - INTERVAL 7 DAY"
        cursor.execute(query, (sid,))
        data = cursor.fetchall()

        if not data:
            print("No data for last 7 days")
            return

        total_hours = 0
        mood_count = {}

        for mood, hours in data:
            total_hours += hours
            mood_count[mood] = mood_count.get(mood, 0) + 1

        avg = total_hours / len(data)
        best_mood = max(mood_count, key=mood_count.get)

        print("\nWeekly Summary")
        print("Average Study Hours:", round(avg, 2))
        print("Most Productive Mood:", best_mood)

    def low_productivity_days(self):
        sid = int(input("Enter Student ID: "))
        query = "SELECT log_date, study_hours FROM daily_log WHERE student_id=%s AND study_hours < 3"
        cursor.execute(query, (sid,))
        data = cursor.fetchall()

        print("\nLow Productivity Days:")
        for row in data:
            print(row[0], "-", row[1], "hours")


# ---------- MENU DRIVEN PROGRAM ----------
tracker = WellnessTracker()

while True:
    print("\n===== STUDENT WELLNESS TRACKER =====")
    print("1. Add New Student")
    print("2. Add Daily Wellness Entry")
    print("3. View Student Report")
    print("4. Weekly Productivity Summary")
    print("5. View Low Productivity Days")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        tracker.add_student()
    elif choice == '2':
        tracker.add_daily_entry()
    elif choice == '3':
        tracker.view_report()
    elif choice == '4':
        tracker.weekly_summary()
    elif choice == '5':
        tracker.low_productivity_days()
    elif choice == '6':
        print("Thank you for using the system")
        break
    else:
        print("Invalid choice")
