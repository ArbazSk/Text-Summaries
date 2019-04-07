from flask import Flask,render_template,url_for
# from summaries import summary
app = Flask(__name__)

@app.route('/')
def summaries():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
