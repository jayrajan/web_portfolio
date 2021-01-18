from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def main():
    title = 'JR Home'
    name = 'Jay Rajan'
    return render_template('home.html',name=name,title=title)

if __name__== '__main__':
    app.run(debug=True)