from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return '<h1> Welcome to Main Page </h1>'

if __name__== '__main__':
    app.run(debg=True)

