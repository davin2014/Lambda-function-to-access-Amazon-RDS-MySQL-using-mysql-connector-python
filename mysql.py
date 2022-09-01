import json
import mysql.connector

def lambda_handler(event, context):
    # TODO implement
    connection = mysql.connector.connect(user='', password='',
                                         host='',port=3306,
                                         database='');
    cursor = connection.cursor()  # get the cursor
    cursor.execute('')
    extracted_data = cursor.fetchall();
    for i in extracted_data:
        print(i)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
