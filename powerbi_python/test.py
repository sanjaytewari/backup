import connection1
import connection2
import pandas as pd 

db_connection1 = connection1.connection()
db_connection2 = connection2.connection()


if db_connection1:
    if db_connection2:   
        try:
            cursor1 = db_connection1.cursor()
            cursor2 = db_connection2.cursor()
            query1 = """
            select distinct UPPER(TRIM(sample_number)) as sample_number, UPPER(trim(district)) as district 
            from soil_data.vw_sample_data
            """
            query2 = """
            select distinct  UPPER(trim(content)) as content,transactional_id from agriculture_dept.vw_t_whatsapp_integration_data 
            """
            sql_result1 = cursor1.execute(query1)
            sql_result2 = cursor2.execute(query2)
            rows1 = cursor1.fetchall()
            rows2 = cursor2.fetchall()
            columns1 = [desc[0] for desc in cursor1.description]
            columns2 = [desc[0] for desc in cursor2.description]
            df1 = pd.DataFrame(rows1, columns= columns1)
            df2 = pd.DataFrame(rows2, columns= columns2) 
            # print(f"Columns in df1: {df1.columns}")
            # print(f"Columns in df2: {df2.columns}")
            df3 = pd.merge(df1,df2, left_on = "sample_number",right_on= "content", how= 'inner')
            df_grouped = df3.groupby('district').agg(transaction_count=('transactional_id', 'count')).reset_index()
            print(df_grouped)
        except Exception as e:
            print(f"Error executing query: {e}")
        finally:
            cursor1.close()
            cursor2.close()
            db_connection1.close()
            db_connection2.close()
    else:
        print("Failed to connect to the database1.")
else:
    print("Failed to connect to the database2.")
