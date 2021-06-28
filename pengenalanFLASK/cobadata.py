from flask import Flask, render_template
from models import CobaData

application = Flask(__name__)
@application.route('/')

def index():
    model = CobaData()
    return render_template('helloworld.html',model=model)

if __name__ == '__main__':
    application.run(debug=True)