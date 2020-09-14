from flask_bootstrap import Bootstrap
from flask import Flask
from .config import DevConfig
# we initialize our applicarion
app = Flask(__name__,instance_relative_config= True)

# set up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile("config.py")

bootstrap = Bootstrap(app)
from app import views