import mysql.connector

def connection():
    try:
        conn = mysql.connector.connect(
            host = "educationdoctor.cz5snxflsj5z.ap-south-1.rds.amazonaws.com",
            user = "sm-tracking",
            password=  "2f4b695cce624ae1e3800157e414820d",
            database=  "agriculture_dept"
        )
        print("connection_successful")
        return conn
    except mysql.connector.Error as e:
        print(f"Error while connecting to mysql: {e}")
        return None
        