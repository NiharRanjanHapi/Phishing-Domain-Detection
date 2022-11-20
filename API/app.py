import os
from urllib import request
from flask import Flask, render_template, url_for, request, redirect
from forms import PredictFromOneVal 
from werkzeug.utils import secure_filename
from datetime import datetime
import pandas as pd
import pickle

app=Flask(__name__)

app.config['SECRET_KEY']='a7f49e2b2869482714eb22559b7bd0c0'


ALLOWED_EXTENSIONS=set(['csv']) #allow upload csv file only
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/home')
def home():
    form=PredictFromOneVal()
    return render_template('one_website.html',form=form)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # new_filename = f'{filename.split(".")[0]}_{str(datetime.now())}.csv'
            save_location = os.path.join('input\\',filename)
            file.save(save_location)
            
            #return send_from_directory('output', output_file)
            df=pd.read_csv(f'input\\{filename}')
            ind=df.index #to get the index of the file

            #selecting the important featute(This is got from the notebook observation)
            impf=['time_response', 'ttl_hostname', 'asn_ip', 'length_url','domain_length',
                    'time_domain_activation', 'time_domain_expiration', 'qty_vowels_domain', 'directory_length']
            
            #loading model
            file=open('model.pkl','rb')
            model=pickle.load(file)  
            file.close()
            return render_template('aset.html', title='From CSV',df=df,impf=impf,model=model,ind=ind)

    return render_template('upload.html', title='From CSV')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/oneweb')
def oneweb():
    form=PredictFromOneVal()
    return render_template('one_website.html',form=form)

@app.route('/oneres', methods=['GET', 'POST'])
def oneres():
    if request.method=='POST':
        form=PredictFromOneVal()

        #getting input values
        time_response=form.time_response.data
        ttl_hostname=form.ttl_hostname.data
        asn_ip=form.asn_ip.data
        length_url=form.length_url.data
        domain_length=form.domain_length.data
        time_domain_activation=form.time_domain_activation.data
        time_domain_expiration=form.time_domain_expiration.data
        qty_vowels_domain=form.qty_vowels_domain.data
        directory_length=form.directory_length.data

        #selecting the important featute(This is got from the notebook observation)
        lst=[[time_response,ttl_hostname,asn_ip,length_url,domain_length,time_domain_activation,time_domain_expiration,qty_vowels_domain,directory_length]]
        data=pd.DataFrame(lst)

        #loading model
        file=open('model.pkl','rb')
        model=pickle.load(file)  
        file.close()

        return render_template('one_response.html',data=data,model=model)


if __name__=='__main__':
    app.run()