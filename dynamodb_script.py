import boto3
from contextlib import redirect_stdout

__TableName__ = "devops-challenge"
Primary_Column_Name = 'code_name'
Primary_Key = 'thedoctor'
columns = ["secret_code"]

client = boto3.client('dynamodb')

DB = boto3.resource('dynamodb')
table = DB.Table(__TableName__)

response = table.get_item(Key={Primary_Column_Name:Primary_Key})

#print(response['Item'])

with open ('./secret_code', 'w') as f:
    with redirect_stdout(f):
        print(response['Item'])
