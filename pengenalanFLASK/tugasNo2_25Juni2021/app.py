from flask import Flask, render_template,url_for,send_from_directory
from models import RandomAngka
import os

application = Flask(__name__)

@application.route('/')
def index():
    objAngka = RandomAngka()
    return render_template('randomAngka.html',cekAngka=objAngka)

# @application.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(application.root_path, 'assets'),
#                           'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    application.run(debug=True)