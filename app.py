import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tool', methods=['GET','POST'])
def tool():
    result = None
    if request.method == 'POST':
        total = int(request.form['total'])
        attended = int(request.form['attended'])

        percentage = (attended / total) * 100
        result = f"Attendance: {percentage:.2f}%"
    
    return render_template('tool.html', result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)