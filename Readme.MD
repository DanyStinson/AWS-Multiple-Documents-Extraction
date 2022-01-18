![Banner](src/img/banner.png)

Documents contain valuable information and come in. In most cases, you are manually processing the documents which is time consuming, prone to error, and costly. Not only do you want this information quickly but you can automate business processes that today rely on manual inputs and intervention various file types and formats. 

**Amazon Textract** is a document analysis service that detects and extracts printed text, and handwriting, structured data, such as fields of interest and their values, and tables from images and scans of documents. Amazon Textract's machine learning models have been trained on millions of documents so that virtually any document type you upload is automatically recognized and processed for text extraction. When information is extracted from documents, the service returns a confidence score for each element it identifies so that you can make informed decisions about how you want to use the results. **Amazon Textract currently supports PNG, JPEG, TIFF, and PDF formats.**

Information we receive may also come in .docx or .xlsx format, which are not currently supported by Amazon Textract. Nevertherless, thanks to **AWS Lambda** and different extraction libraries, we can process the data that resides in these documents. I will leave you the MVP code (**REMEMBER, NOT PRODUCTION READY**) for you to begin your text extraction journey. 

### What do I need?
**AWS Account** If you don't already have an account or you have not been handed one as part of a workshop, please visit the following [link](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start)! 

## Extracting data from Excel files
To extract data from xlsx files we are going to create a lambda function with additional libraries for manipulation. 

### How do I deploy my function?

#### Step 1, Deploy your Lambda function
 * [Launch](https://eu-west-1.console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?templateURL=https://aidemos-document-extraction.s3.eu-west-1.amazonaws.com/excel-extraction.yaml&stackName=ExcelExtract) the following **AWS CloudFormation Template** in your account (The link will automatically open the AWS CloudFormation console). **THIS TEMPLATE IS TO BE DEPLOYED IN EU-WEST-1 REGION ONLY**
  * You will have to fill some parameters, make sure you insert unique names for your resources, check the AWS CloudFormation acknowledgements and click Create stack.
  * Wait until the stack goes into the **CREATE_COMPLETE** status.
  * You can now head over to the AWS Lambda service and will find your new function 

#### Step 2, Create and add Lambda Layers
  * Inside the AWS Lambda service, head to Layers --> Create Layer
  * Create a new layer uploading the following [.zip file](/layers/Excel-Layer.zip), and select x86_64 as compatible architecture and Python 3.8 as compatible runtime.
  * Return to your function and in your layers section, select **Add Layer**
    * Select your layer which will be available at the Custom AWS layers dropdown.
    * We are also going to add additional layers, but we are going to add them specifying an ARN
    * Add new layers with the following ARNs
      * **arn:aws:lambda:eu-west-1:770693421928:layer:Klayers-python38-pandas:43**
      * **arn:aws:lambda:eu-west-1:770693421928:layer:Klayers-python38-numpy:22** 
      * **arn:aws:lambda:eu-west-1:770693421928:layer:Klayers-python38-openpyxl:9**

#### Step 3, Try out your Lambda Function
You are now ready to start extracting information from your xlsx files! Remember to change your function parameters to try out with your data.
```
#VARIABLES TO DEFINE
s3_bucket_name = "XXX" -- The bucket where your file resides.
input_filename = 'YYY.xlsx' --- The path and name of file.
output_filename = 'ZZZ' --- The output path and name you whish to give to your resulting CSV file. 
```

## Extracting data from Word files
To extract data from .docx files we are going to create a lambda function with additional libraries for manipulation. 

### How do I deploy my function?

#### Step 1, Deploy your Lambda function
 * [Launch](https://eu-west-1.console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?templateURL=https://aidemos-document-extraction.s3.eu-west-1.amazonaws.com/docx-extraction.yaml&stackName=DocxExtract) the following **AWS CloudFormation Template** in your account (The link will automatically open the AWS CloudFormation console).**THIS TEMPLATE IS TO BE DEPLOYED IN EU-WEST-1 REGION ONLY**
  * You will have to fill some parameters, make sure you insert unique names for your resources, check the AWS CloudFormation acknowledgements and click Create stack.
  * Wait until the stack goes into the **CREATE_COMPLETE** status.
  * You can now head over to the AWS Lambda service and will find your new function

#### Step 2, Add Lambda Layers
 * Inside your function, in your layers section, select **Add Layer**
 * We are going to add additional layers specifying an ARN
    * Add a new layers with the following ARN:
      * **arn:aws:lambda:eu-west-1:770693421928:layer:Klayers-python38-python-docx:4**

#### Step 3, Try out your Lambda Function
You are now ready to start extracting information from your docx files! Remember to change your function parameters to try out with your data. Amazon Comprehend is integrated in the code to extract relevant entities from the processed document.
```
#VARIABLES TO DEFINE
s3_bucket_name = "XXX" #The bucket where your file resides.
input_filename = 'Y.docx' #The path and name of file.
