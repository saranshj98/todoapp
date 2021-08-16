from os import environ

SECRET_KEY = environ.get('SECRET_KEY')
API_KEY = environ.get('API_KEY')
MONGO_URI = environ.get('MONGO_URI')