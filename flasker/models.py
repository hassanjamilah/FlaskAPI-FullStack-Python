import os
from flask_sqlalchemy import SQLAlchemy
import json

database_name = 'plantsdb'
database_path= 'postgres://postgres@localhost:5432/{}'.format(database_name)

db = SQLAlchemy()

'''
Setup the DB
'''
def setup_db(app ):
    app.config["SQLALCHEMY_DATABASE_URI"]= database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
    db.app = app
    db.init_app(app)
    db.create_all()
    
    
class Plant(db.Model):
    __tablename__ = 'plants'
    
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String)
    scientific_name = db.Column(db.String)
    is_poisinous = db.Column(db.Boolean)
    primary_color = db.Column(db.String)
    
    def __init__(self , name , scientificName , isPoisinous , primaryColor):
        self.name = name
        self.scientific_name = scientificName
        self.is_poisinous = isPoisinous
        self.primary_color = primaryColor
        
    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def format(self):
        return {
            'id':self.id , 
            'name':self.name , 
            'scientific_name':self.scientific_name , 
            'is_poisinous':self.is_poisinous , 
            'primary_color':self.primary_color
        }