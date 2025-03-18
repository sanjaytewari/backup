import mysql.connector

def connection():
    try:
        conn = mysql.connector.connect(
            host = "educationdoctor.cz5snxflsj5z.ap-south-1.rds.amazonaws.com",
            user = "soil_data",
            password=  "9641b83ca1941a93e1984343eeea6d71",
            database=  "soil_data"
        )
        print("connection_successful")
        return conn
    except mysql.connector.Error as e:
        print(f"Error while connecting to mysql: {e}")
        return None
        