from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='')
    else:
        value_regular = 32
        value_relaxed = 34
        value_skinny = 30
        value_slim = 29
        value_loose = 35
        num_regular = request.form['regular']
        num_relaxed = request.form['relaxed']
        num_skinny = request.form['skinny']
        num_slim = request.form['slim']
        num_loose = request.form['loose']
        total_regular = int(num_regular)*value_regular
        total_relaxed = int(num_relaxed)*value_relaxed
        total_skinny = int(num_skinny)*value_skinny
        total_slim = int(num_slim)*value_slim
        total_loose = int(num_loose)*value_loose
        
        final_result = total_regular + total_relaxed + total_skinny + total_slim + total_loose
        return render_template('index.html', href2='regular='+num_regular+', relaxed='+num_relaxed+', skinny='+skinny+', slim='+num_slim+', loose='+num_loose+', Total = '+str(final_result))
