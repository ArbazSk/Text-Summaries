from flask import Flask,render_template,url_for
from flask import request
from summaries import summaries
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summary',methods=['GET','POST'])
def summary():
    if request.method == 'POST':
        raw_text = request.form['inputText']
        final_summary = summaries(raw_text)

    return render_template('index.html',result=final_summary)

if __name__ == '__main__':
    app.run()
