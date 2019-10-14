import os
import string

from decouple import config


BASE_DIR = os.path.abspath('.')

DEBUG = config('DEBUG', cast=bool)

SECRET_KEY = config('SECRET_KEY') or \
    ''.join(random.choice(string.ascii_letters) for i in range(42))

SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI') or \
    'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')

SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', True, cast=bool)
