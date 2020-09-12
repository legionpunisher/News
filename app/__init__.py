from flask import Flask
from .config import DevConfig
# we initialize our applicarion
app = Flask(__name__)

#we set up configuration
app.config.from_object(DevConfig)

from app import views