import sys
import os
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')

load_dotenv(dotenv_path, verbose=True)

class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'uni123-402-amen-f-a32')    
    DOWNLOAD_FOLDER = os.getenv('DOWNLOAD_FOLDER')
    WEB_FOLDER = os.getenv('WEB_FOLDER')

class ProductionConfig(Config):
    DEBUG = False
    DEVELOPMENT = False