from flask import Flask, render_template, request
import os
import secrets

secret_key = secrets.token_hex(16)
print(secret_key)
secret_key = os.environ['SECRET_KEY']
print(f"The secret key is: {secret_key}")

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def user_form():
    if request.method == 'POST':
        pass
    print(request.form)
    return render_template('user_form.html')

if __name__ == 'main':
    port = int(os.environ.get("POST", 80))
    app.run(host="0.0.0.0", port=port)
   
    
    