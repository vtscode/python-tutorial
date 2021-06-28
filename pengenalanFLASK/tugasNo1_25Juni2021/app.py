from flask import Flask, render_template,url_for

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('gridstyle.html')

if __name__ == '__main__':
    application.run(debug=True)