import pandas as pd 
import xlrd 
import openpyxl 
from io import StringIO  
import boto3
import json
s3_resource = boto3.resource('s3')

#VARIABLES TO DEFINE
s3_bucket_name = "YOUR_BUCKET_NAME"
input_filename = 'YOUR_INPUT_FILE_NAME.xlsx'
output_filename = 'YOUR_OUTPUT_FILE_NAME'

def lambda_handler(event, context):
   
    # Set some display options for the dataframe 
    pd.set_option('display.max_rows', 10) 
    pd.set_option('display.max_columns', 10)    
    pd.set_option('display.width', 1000) 
    
    df=pd.read_excel('s3://'+s3_bucket_name+'/'+input_filename, engine='openpyxl')
    
    # Print the excel files 
    print(df)   
    
    # Transform data as csv
    csv_buffer = StringIO() 
    df.to_csv(csv_buffer) 

    # Write the data back as a CSV 

    s3_resource.Object(s3_bucket_name,output_filename).put(Body=csv_buffer.getvalue()) 
    
    return {
        'statusCode': 200,
        'body': json.dumps('File transformed!')
    }
