import mysql.connector

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
