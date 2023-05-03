# give the file access to the SQLAlchemy db
from app import db
from sqlalchemy.sql import expression
# from sqlalchemy import Boolean, Column


# define the Planet class and name it after the model, planet.py 
# follow the SQLAchemy pattern for creating a class for the Planet model
# Connect the Planet model with our SQL database: solar_system_development

#  (db.Model) The class Planet inherits from db.Model from SQLAlchemy
# this allows Flask to work with Planet instances (OOP)
# which then allows us to access instance of Planet that correspond to a db row
# SQLAlchemy will use the lowercase version of this class name as the name of the table it will create.

# map attributes to table columns
# attributecolumnname = db.Column(db.DataType)

class Planet(db.Model):
    
    planet_id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    has_flag= db.Column(db.Boolean, unique=False, server_default=expression.false(), default=False, nullable=False)
    
    def __init__(self, planet_id, name, description, has_flag= False):
        self.planet_id = planet_id
        self.name = name
        self.description = description
        self.has_flag = has_flag
