import json 
import os
from flask import Flask,render_template,request

app = Flask(__name__)
file_path = 'data.json'
path = 'static/images'
contents = os.listdir(path)
con = []
@app.route('/')
def index():

    for i in contents:
        con.append(i)
    print(con)
    page_size = int(request.args.get('page_size',default=10))
    cache_version = '1.0'
    print(page_size)
    
       
    return render_template("data.html",cache_version = cache_version,page_size=page_size,con = con)
if __name__ == '__main__':
    app.run(debug=True)
# print(json.dumps(data, indent=4))