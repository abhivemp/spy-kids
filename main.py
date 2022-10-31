from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

# match result db
class Match(db.Model):
    id = 
    table_name = 
    column = 
    index = 
    spi_filter = 
    

@app.route('/')
def hello():
    return "Hello World!"