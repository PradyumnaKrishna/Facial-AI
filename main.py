from flask import Flask, redirect
from FER.main import fer
import secrets

app = Flask(__name__)
app.register_blueprint(fer, url_prefix='/FER')
app.secret_key = secrets.token_urlsafe(32)


@app.route('/')
def main():
    return redirect('/FER')


if __name__ == "__main__":
    app.run()
