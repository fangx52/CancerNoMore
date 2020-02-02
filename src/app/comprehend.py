import boto3

def aws_comprehend(text):
    comprehend_client=boto3.client('comprehend')
    comprehend_response=comprehend_client.detect_key_phrases(Text=text, LanguageCode='en')
    return comprehend_response

