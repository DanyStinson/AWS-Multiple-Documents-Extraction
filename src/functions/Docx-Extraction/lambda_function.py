import json, boto3, pprint
from docx import Document
comprehend = boto3.client('comprehend')
s3 = boto3.resource('s3')

s3_bucket_name = "XXX" #The bucket where your file resides.
input_filename = 'Y.docx' #The path and name of file.

def lambda_handler(event, context):
    s3.Bucket(s3_bucket_name).download_file(input_filename, '/tmp/'+(input_filename))
    document = Document('/tmp/'+(input_filename))
    for para in document.paragraphs:
        if(para.text != ""):
            print(para.text)
            response = comprehend.detect_entities(
                Text=para.text,
                LanguageCode='en'
            )
            if(len(response["Entities"]) > 0):
                pprint.pprint(response["Entities"])
    return {
        'statusCode': 200,
        'body': json.dumps('Document Processed')
    }
