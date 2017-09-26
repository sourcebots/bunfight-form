from flask import Flask, render_template, request
from email.utils import parseaddr
from csv import DictWriter
app = Flask(__name__)

file_loc = "details.csv"

@app.route("/", methods=['GET', 'POST'])
def signup_form():
    modal = False
    if request.method == 'POST':
        with open(file_loc,'a') as f:
            fieldnames = ['name', 'email']
            csvwriter = DictWriter(f, fieldnames)
            response = request.form.to_dict()
            if response['email']:
                csvwriter.writerow(response)
                modal = True
    return render_template('signup_form.html', modal=modal)

if __name__ == "__main__":
    app.run()
