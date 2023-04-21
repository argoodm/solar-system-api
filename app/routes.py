from flask import Blueprint


class Planets:
    def __init__(id, name, description, has_flag= False):
        self.id = id
        self.name = name
        self.description = description
        self.has_flag = has_flag

planets = [
    Planets(name, description),
    Planets(name, description),
    Planets(name, description),
    Planets(nname, description),
    Planets(name, description),


]