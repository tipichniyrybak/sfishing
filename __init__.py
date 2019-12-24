from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

fl_app = Flask(__name__)
fl_app.config.from_object(Config)
bootstrap = Bootstrap(fl_app)



from routes import *


if __name__ == '__main__':
    print("init...")
    fl_app.debug = True
    fl_app.run()