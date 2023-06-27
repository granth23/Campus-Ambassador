from flask import Flask, render_template, request
from db import new_user

app = Flask(__name__)
app.secret_key = "granthbagadiagranthbagadia"


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get(f'name')
        college = request.form.get(f'college')
        phone = request.form.get(f'phone')
        email = request.form.get(f'email')
        message = new_user(name, college, phone, email)
        return render_template('index.html', message = message)
    return render_template('index.html', message = "")



if __name__ == '__main__':
    app.run(debug=True)