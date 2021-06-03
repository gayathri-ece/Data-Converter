import pandas as pd
from flask import Flask,render_template,send_file,url_for,request

app=Flask(__name__)

@app.route('/',method=['POST'])
def home:
    if(request.method=='POST'):
        f=request.files('file')
        #Get file name extension and then change the data to required format
        ext=fileextension
        if('.csv' in ext):
            df=pd.read_csv(f)
        elif('.xls' in ext):
            df=pd.read_excel(f)
        else:
            df=pd.read_json(f)
        to=request.form['to']
        if('.csv' in to):
            return(df.to_csv('filename.csv'))
        elif('.excel' in to):
            return(df.to_excel('filename.xls'))
        else:
            return(df.to_json('filename.json'))
        return('Hello')
    else:
        return(render_template('main.html'))

if __name__=="__main__":
    app.run(debug=True)
