from flask import Flask

fl_app = Flask(__name__)

from routes import *


if __name__ == '__main__':
    print("init...")
    fl_app.debug = True
    fl_app.run()