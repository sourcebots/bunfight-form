from flask import Flask, render_template, request
from email.utils import parseaddr
app = Flask(__name__)

file_loc = "details.csv"

@app.route("/", methods=['GET', 'POST'])
def signup_form():
    modal = False
    if request.method == 'POST':
        with open(file_loc,'a') as f:
            email = request.form["email"]
            if email:
                f.write(email + ",\n")
                modal = True
    return render_template('signup_form.html', modal=modal)

if __name__ == "__main__":
    app.run()
