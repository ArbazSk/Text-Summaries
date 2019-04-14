from flask import Flask,render_template,url_for
from flask import request,abort,Response,redirect
from summaries_Rough import summaries
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summary',methods=['GET','POST'])
def summary():
    if request.method == 'POST':
        raw_text = request.form['inputText']
        final_summary = summaries(raw_text)
        print(final_summary)

    return render_template('output.html',result=final_summary,input_text=raw_text)


if __name__ == '__main__':
    app.run(debug=True)
