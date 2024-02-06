import sqlite3
import pandas as pd

class DataBase:
    def create_db(self):
        connection = sqlite3.connect('students.db')
        cursor = connection.cursor()
        create_table = '''
        CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        course TEXT NOT NULL,
        mobile TEXT NOT NULL )       
        '''
        cursor.execute(create_table)
        connection.commit()
        cursor.close()
        connection.close()


    def load_data(self):
        connection = sqlite3.connect('students.db')
        result = connection.execute('SELECT * FROM student')
        records = list(result)

        df = pd.DataFrame(records, columns=['id', 'name', 'course', 'mobile'])
        df.set_index('id', inplace=True)

        return df

class Student:
    def add_student(self, name, course, mobile):
        self.name = name
        self.course = course
        self.mobile = mobile

        connection = sqlite3.connect('students.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO student (name, course, mobile) VALUES (?, ?, ?)',
                       (self.name, self.course, self.mobile))
        connection.commit()
        cursor.close()
        connection.close()


    def delete_student(self, id):
        connection = sqlite3.connect('students.db')
        cursor = connection.cursor()

        #Check if student exists
        cursor.execute('SELECT * FROM student where id = ?', (id,))
        existing_student = cursor.fetchone()

        if existing_student:
            cursor.execute('DELETE FROM student where id = ?', (id,))
            connection.commit()
            return f'Student {id} has been deleted'

        else:
            return 'No such student exists'




#  Uncomment commands below to see what they do

database = DataBase()

# Create the database
# database.create_db()

student = Student()

# Add students
# student.add_student('Mary Smart', 'Math', '03232232324')
# student.add_student('Leah Smith', 'Biology', '088344322324')
# student.add_student('Mark Twist', 'Biology', '07986554323')

# View data in terminal
# print(database.load_data())

# Delete a student
# delete_student = student.delete_student(2)
# print(delete_student)



