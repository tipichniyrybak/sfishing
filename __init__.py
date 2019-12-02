from flask import Flask
from config import Config

fl_app = Flask(__name__)
fl_app.config.from_object(Config)


from routes import *


if __name__ == '__main__':
    print("init...")
    fl_app.debug = True
    fl_app.run()