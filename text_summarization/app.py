from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    generated_summary = None

    if request.method == 'POST':
        # Get the user input from the form
        user_text = request.form['user_text']

        # Call the summarize.py script as a subprocess
        cmd = ['python', 'summarize.py', user_text]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        out, _ = proc.communicate()

        # Get the summary from the output of the script
        generated_summary = out.strip()

    return render_template('index.html', generated_summary=generated_summary)

if __name__ == '__main__':
    app.run(debug=True)
