from flask import render_template, request
from app import app, mongo
from comprehend import aws_comprehend

@app.route('/C1L1', methods=["GET","POST"])
def upload():
    error=''
    try:
        if request.method== "POST":
            uploaded_txt= request.form.to_dict()['file1']
            returned_txt= aws_comprehend(uploaded_txt)
            # mongo.insert(returned_txt)
            print(returned_txt)
        return render_template('C1L1.html', title='Home')
    except Exception as e:
        return render_template("/C1L1", error=error)
@app.route('/HOME', methods=["GET"])
def home():
    ##api request
    ## api_ret
    # x = 'hello there'
    return render_template('HOME.html')