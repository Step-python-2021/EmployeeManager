from config import mysql


class Employee(object):

    @staticmethod
    def add_employee(name, surname, photo):
        connection = mysql.get_db()
        cursor = mysql.get_db().cursor()
        sql_query = """
            insert into employees (name, surname, photo)
            values (%s, %s, %s)
        """
        cursor.execute(sql_query, (name, surname, photo))
        connection.commit()
        cursor.close()
        connection.close()
