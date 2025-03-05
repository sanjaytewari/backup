import pandas as pd
from sqlalchemy import create_engine
import os
import shutil

mysql_user = 'root'  
mysql_password = 'root'  
mysql_host = 'localhost'  
mysql_database = 'practice'

csv_directory = r'C:\Users\ASPLGGNADMN\Downloads\to_upload_in_local_host_mysql_practice_airteL-call_detail\to_upload'
uploaded_directory = r'C:\Users\ASPLGGNADMN\Downloads\to_upload_in_local_host_mysql_practice_airteL-call_detail\uploaded'
table_name = 'airtel_call_detail' 

csv_columns = ['Target /A PARTY NUMBER', 'CALL_TYPE', 'Type of Connection', 'B PARTY NUMBER', 'LRN- B Party Number', 
               'Translation of LRN', 'Call date', 'Call Initiation Time', 'Call Duration', 'First BTS Location', 
               'First Cell Global Id', 'Last BTS Location', 'Last Cell Global Id', 'SMS Centre Number', 'Service Type', 
               'IMEI', 'IMSI', 'Call Forwarding Number', 'Roaming Network/Circle', 'MSC ID', 'In TG ', 'Out TG']
mysql_columns = ['TargetNo', 'CallType', 'TOC', 'BPartyNo', 'LRNNo', 'LRNTSPLSA', 'Date', 'Time', 'DurationInSeconds', 
                 'FirstCGI', 'FirstCGILatLong', 'LastCGI', 'LastCGILatLong', 'SMSNo', 'ServiceType', 'IMEI', 'IMSI', 
                 'CallFowNo', 'RoamNw', 'SWMSCID', 'IN_TG', 'OUT_TG']

column_mapping = dict(zip(csv_columns, mysql_columns))

connection_string = f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_database}"
engine = create_engine(connection_string)

def upload_csv_to_mysql(file_path, table_name):
    try:
        df = pd.read_csv(file_path, skiprows=10, skipfooter=1, engine='python')

        # Check if the DataFrame is empty
        if df.empty:
            print(f"Warning: The file {file_path} contains no valid data.")
            return

        # Inspect the first few rows to ensure it's loaded correctly
        print(f"Data from {file_path}:\n", df.head())

        # Drop gibberish lines if necessary (e.g., based on column conditions)
        # df = df[~df[csv_columns[0]].str.contains('Vodafone Idea Call Data Records|Report Type|DEL_', na=False)]
        
        # Rename the DataFrame columns to match MySQL table columns
        df = df.rename(columns=column_mapping)

        # Check DataFrame columns and data types
        print("DataFrame columns and data types:")
        print(df.dtypes)

        # Upload DataFrame to MySQL table
        df.to_sql(table_name, con=engine, if_exists='append', index=False)
        print(f"File '{file_path}' successfully uploaded to MySQL.")
    except Exception as e:
        print(f"Error uploading file '{file_path}': {e}")

# Function to move the processed file to another directory
def move_file(file_path, target_directory):
    try:
        # Ensure the target directory exists
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
        
        # Construct the target file path
        target_file_path = os.path.join(target_directory, os.path.basename(file_path))
        
        # Move the file
        shutil.move(file_path, target_file_path)
        print(f"File '{file_path}' moved to '{target_directory}'.")
    except Exception as e:
        print(f"Error moving file '{file_path}': {e}")

# Process each CSV file in the given directory
for filename in os.listdir(csv_directory):
    file_path = os.path.join(csv_directory, filename)
    
    if filename.endswith('.csv') and os.path.isfile(file_path):
        # Upload the CSV file to MySQL
        upload_csv_to_mysql(file_path, table_name)
        
        # Move the processed file to the 'uploaded' directory
        move_file(file_path, uploaded_directory)
