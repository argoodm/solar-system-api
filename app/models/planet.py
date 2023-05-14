# give the file access to the SQLAlchemy db
from app import db

from sqlalchemy.sql import expression
# from sqlalchemy import Boolean, Column


# define the Planet class and name it after the model, planet.py 
# follow the SQLAchemy pattern for creating a class for the Planet model
# Connect the Planet model with our SQL database: solar_system_development

# (db.Model) The class Planet inherits from db.Model from SQLAlchemy
# this allows Flask to work with Planet instances (OOP)
# which then allows us to access instance of Planet that correspond to a db row
# SQLAlchemy will use the lowercase version of this class name as the name of the table it will create.

# map attributes to table columns
# attributecolumnname = db.Column(db.DataType)

class Planet(db.Model):
    
    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    has_flag= db.Column(db.Boolean, unique=False, server_default=expression.false(), default=False, nullable=False)
    
    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description
        planet_as_dict["has_flag"] = self.has_flag

        return planet_as_dict
    
    
    
    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(name=planet_data["name"],
                        description=planet_data["description"],
                        has_flag=planet_data["has_flag"])
        return new_planet
    
    
    
    # def __init__(self, id, name, description, has_flag= False):
    #     self.id = id
    #     self.name = name
    #     self.description = description
        # self.has_flag = has_flag
