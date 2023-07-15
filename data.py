import json 
import os
from flask import Flask,render_template,request

app = Flask(__name__)
file_path = 'data.json'
@app.route('/')
def index():
    with open('data.json','r') as f:
        data = json.load(f)
    page_size = int(request.args.get('page_size',default=10))
    transaction = data['Payload'][0]['data'][0]['decryptedFI']['account']['transactions']['transaction']
    cache_version = '1.0'
    print(page_size)
    
       
    return render_template("data.html",data= data,transaction=transaction,cache_version = cache_version,page_size=page_size)
if __name__ == '__main__':
    app.run(debug=True)
# print(json.dumps(data, indent=4))