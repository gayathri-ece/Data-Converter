import pandas as pd
from flask import Flask,render_template,send_file,url_for,request,jsonify,redirect
from werkzeug.datastructures import FileStorage

app=Flask(__name__)
app.secret_key = "secret key"
UPLOAD_FOLDER = '/content'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH']= 1024 * 1024

@app.route('/',methods=['POST','GET'])
def home():
    if(request.method=='POST'):
        if not all(i in request.files for i in ['file']):
            return jsonify(error = 'Incorrect payload!')    
        f=request.form
        print(f)
        image = request.files["file"]
        im='./content/input'+str(image.filename[image.filename.find('.'):])
        image.save(im)
        if('.csv' in im):
            df=pd.read_csv(im)
        elif('.xls' in im):
            df=pd.read_excel(im)
        else:
            df=pd.read_json(im)
        to=request.form['to']
        global file
        file=image.filename[:image.filename.find('.')]
        if('csv' in to):
            file=file+'.csv'
            df.to_csv(file)
        elif('excel' in to):
            file=file+'.xls'
            df.to_excel(file)
        else:
            file=file+'.json'
            df.to_json(file,orient='records')
        return(redirect(url_for('download')))
    else:
        return(render_template('main.html'))

@app.route('/download')
def download():
    return(send_file(file,as_attachment=True))
if __name__=="__main__":
    app.run(debug=True)
