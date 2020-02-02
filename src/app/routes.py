from flask import render_template, request
from app import app, mongo
import boto3

@app.route('/')
@app.route('/home', methods=["GET"])
def home():
    return render_template('home.html')
@app.route('/C1L1', methods=["GET","POST"])
def upload():
    error=''
    # try:
    if request.method== "POST":
        f = request.files['file']
        f.save("test.txt")
        file=open("test.txt","r")
        text=''
        for line in file:
            text+=line
        returned_txt= aws_comprehend(text)
        for item in returned_txt['KeyPhrases']:
            del item['BeginOffset']
            del item['EndOffset']
        # mongo.collection.insert(returned_txt)
        print(returned_txt)
    return render_template('C1L1.html', title='Home')
    # except Exception as e:
    #     return render_template("C1L1", error=e)


def aws_comprehend(text):
    comprehend_client=boto3.client('comprehend')
    comprehend_response=comprehend_client.detect_key_phrases(Text=text, LanguageCode='en')
    return comprehend_response
