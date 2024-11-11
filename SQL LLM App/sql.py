import sqlite3

# Connect to sqlite
connection = sqlite3.connect("student.db")
cursor = connection.cursor()

# Create the table if it doesn't already exist
table_info = """
CREATE TABLE IF NOT EXISTS student (
    name VARCHAR(25),
    class VARCHAR(25),
    section VARCHAR(25),
    marks INT
)
"""
cursor.execute(table_info)
print("Table created or already exists.")

# Function to insert a row if it does not exist
def insert_if_not_exists(name, class_name, section, marks):
    # Check if a record with the same name, class, and section already exists
    cursor.execute(
        "SELECT * FROM student WHERE name = ? AND class = ? AND section = ?",
        (name, class_name, section)
    )
    if not cursor.fetchone():  # Only insert if row does not exist
        cursor.execute(
            "INSERT INTO student (name, class, section, marks) VALUES (?, ?, ?, ?)",
            (name, class_name, section, marks)
        )
        print(f"Inserted record: {name}, {class_name}, {section}, {marks}")
    else:
        print(f"Record already exists: {name}, {class_name}, {section}")

# Insert a few records
insert_if_not_exists('Hrishi', 'Data Science', 'A', 90)
insert_if_not_exists('Aditi', 'Data Science', 'B', 85)
insert_if_not_exists('Avanti', 'Data Science', 'A', 93)
insert_if_not_exists('Manha', 'Data Science', 'A', 91)
insert_if_not_exists('Allan', 'Data Science', 'A', 87)
insert_if_not_exists('Samira', 'Statistics', 'B', 78)
insert_if_not_exists('Kiran', 'Data Science', 'A', 91)
insert_if_not_exists('Ravi', 'Machine Learning', 'C', 83)
insert_if_not_exists('Lina', 'Software Engineering', 'A', 95)
insert_if_not_exists('Jonas', 'Statistics', 'B', 86)
insert_if_not_exists('Farah', 'Data Science', 'C', 79)
insert_if_not_exists('Meera', 'Machine Learning', 'A', 92)
insert_if_not_exists('Rohan', 'Software Engineering', 'B', 88)
insert_if_not_exists('Sara', 'Statistics', 'A', 94)
insert_if_not_exists('Kamal', 'Data Science', 'C', 81)
insert_if_not_exists('Aarav', 'Machine Learning', 'B', 82)
insert_if_not_exists('Maya', 'Statistics', 'A', 89)
insert_if_not_exists('Neha', 'Software Engineering', 'C', 77)
insert_if_not_exists('Raj', 'Data Science', 'B', 84)
insert_if_not_exists('Ishaan', 'Statistics', 'A', 92)
insert_if_not_exists('Leena', 'Machine Learning', 'B', 85)
insert_if_not_exists('Amara', 'Data Science', 'C', 76)
insert_if_not_exists('Zara', 'Software Engineering', 'A', 93)
insert_if_not_exists('Kabir', 'Statistics', 'B', 81)
insert_if_not_exists('Vikram', 'Data Science', 'A', 90)
insert_if_not_exists('Tara', 'Machine Learning', 'A', 88)
insert_if_not_exists('Aryan', 'Statistics', 'C', 79)
insert_if_not_exists('Sanya', 'Software Engineering', 'B', 86)
insert_if_not_exists('Rehaan', 'Data Science', 'A', 94)
insert_if_not_exists('Nina', 'Machine Learning', 'C', 80)
insert_if_not_exists('Kunal', 'Statistics', 'A', 89)
insert_if_not_exists('Arjun', 'Data Science', 'B', 87)
insert_if_not_exists('Pooja', 'Software Engineering', 'A', 91)
insert_if_not_exists('Aalia', 'Statistics', 'C', 82)
insert_if_not_exists('Dev', 'Machine Learning', 'B', 83)

# Commit the changes to ensure the data is saved to student.db
connection.commit()
print("Changes committed to the database.")

# Print the inserted records to confirm
print("The records in the student table are:")
data = cursor.execute("SELECT * FROM student")
for row in data:
    print(row)

# Confirm the total number of records in the student table
total_records = cursor.execute("SELECT COUNT(*) FROM student").fetchone()[0]
print(f"Total number of records in the student table: {total_records}")

# Close the connection
connection.close()
print("Database connection closed.")