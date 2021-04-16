import os
#from secret_db_creds import CREDENTIALS

if os.environ.get("DATABASE_URL"):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://" + (os.environ.get("DATABASE_URL"))[11:] + "?sslmode=require?client_encoding=utf8"
else:
    #SQLALCHEMY_DATABASE_URI = CREDENTIALS
    print('Switch on your local creds!')

SQLALCHEMY_TRACK_MODIFICATIONS = False
