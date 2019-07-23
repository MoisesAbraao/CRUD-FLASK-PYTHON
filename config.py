import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY =  'knbhjnbhjnghj87678b'
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(BASE_DIR, 'db.sqlite')