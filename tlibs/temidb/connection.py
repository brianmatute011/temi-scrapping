import mysql.connector
import os
import pandas as pd

class temidb_connection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connection success")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Closed.")

class mat_base:
    def __init__(self, connection):
        self.connection = connection
        try:
            self.connection.connect()
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def fetch_all(self):
        try:
            query = "SELECT * FROM mat_base"
            cursor = self.connection.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print(f"Error fetching all records: {e}")
            return []

    def fetch_by_code(self, code):
        try:
            query = "SELECT * FROM mat_base WHERE code = %s"
            cursor = self.connection.connection.cursor()
            cursor.execute(query, (code,))
            result = cursor.fetchall()
            cursor.close()
            return result[0] if result else None
        except Exception as e:
            print(f"Error fetching record by code: {e}")
            return None
        
    def fetch_by_description(self, description):
        try:
            query = "SELECT * FROM mat_base WHERE mat_description LIKE %s"
            cursor = self.connection.connection.cursor()
            cursor.execute(query, ('%' + description + '%',))
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print(f"Error fetching records by description: {e}")
            return []
class equipment_base:
    def __init__(self, connection):
        self.connection = connection
        try:
            self.connection.connect()
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def fetch_all(self):
        try:
            query = "SELECT * FROM equipment_base"
            cursor = self.connection.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print(f"Error fetching all records: {e}")
            return []

    def fetch_by_code(self, code):
        try:
            query = "SELECT * FROM equipment_base WHERE code = %s"
            cursor = self.connection.connection.cursor()
            cursor.execute(query, (code,))
            result = cursor.fetchall()
            cursor.close()
            return result[0] if result else None
        except Exception as e:
            print(f"Error fetching record by code: {e}")
            return None
        
    def fetch_by_description(self, description):
        try:
            query = "SELECT * FROM equipment_base WHERE equipment_description LIKE %s"
            cursor = self.connection.connection.cursor()
            cursor.execute(query, ('%' + description + '%',))
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print(f"Error fetching records by description: {e}")
            return []
        
    def fetch_by_cpc(self, cpc):
        try:
            query = "SELECT * FROM equipment_base WHERE cpc = %s"
            cursor = self.connection.connection.cursor()
            cursor.execute(query, (cpc,))
            result = cursor.fetchall()
            cursor.close()
            return result[0] if result else None
        except Exception as e:
            print(f"Error fetching record by code: {e}")
            return None
class salary_base_dollars:
    def __init__(self, connection):
        self.connection = connection
        try:
            self.connection.connect()
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def fetch_all(self):
        try:
            query = "SELECT * FROM salary_base_dollars"
            cursor = self.connection.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print(f"Error fetching all records: {e}")
            return []

    def fetch_by_code(self, code):
        try:
            query = "SELECT * FROM salary_base_dollars WHERE code = %s"
            cursor = self.connection.connection.cursor()
            cursor.execute(query, (code,))
            result = cursor.fetchall()
            cursor.close()
            return result[0] if result else None
        except Exception as e:
            print(f"Error fetching record by code: {e}")
            return None
        
    def fetch_by_worker_category(self, description):
        try:
            query = "SELECT * FROM salary_base_dollars WHERE worker_category LIKE %s"
            cursor = self.connection.connection.cursor()
            cursor.execute(query, ('%' + description + '%',))
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print(f"Error fetching records by description: {e}")
            return []
        
    def fetch_by_identifier(self, cpc):
        try:
            query = "SELECT * FROM salary_base_dollars WHERE identifier = %s"
            cursor = self.connection.connection.cursor()
            cursor.execute(query, (cpc,))
            result = cursor.fetchall()
            cursor.close()
            return result[0] if result else None
        except Exception as e:
            print(f"Error fetching record by code: {e}")
            return None                    
class result:
    def __init__(self, connection):
        self.connection = connection
        try:
            self.connection.connect()
        except Exception as e:
            print(f"Error connecting to database: {e}")
    
    def fetch_all(self):
        try:
            query = "SELECT * FROM result"
            cursor = self.connection.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print(f"Error fetching all records: {e}")
            return []        
    
    def insert_result_from_recoverylist(self, _recovery_list):
        sql_insert = f"INSERT INTO result VALUES ({', '.join(['%s']*(208))})"
        try:
            cursor = self.connection.connection.cursor()
            for sublist in _recovery_list:
                purified_sublist_s1 = [value if not (isinstance(value, float) or value == 'nan') else None  for value in sublist]
                purified_tuple_s2 = tuple(0 if index > 7 and value == None else value for index, value in enumerate(purified_sublist_s1))
                print(purified_tuple_s2)
                cursor.execute(sql_insert, purified_tuple_s2)
            self.connection.connection.commit()  
            cursor.close()  
        except Exception as e:
            print(f'Error insert into result table: {e}')

    def export_to_excel(self, filename):
        try:
            query = "SELECT * FROM result"
            df = pd.read_sql(query, self.connection.connection)

            if os.path.isfile(filename):
                os.remove(filename)

            df.to_excel(filename, index=False, header=True)
            print(f"Data exported to {filename} successfully.") 
        except Exception as e:
            print(f"Error exporting data to Excel: {e}")
