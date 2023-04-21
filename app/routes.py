from flask import Blueprint


class Planets:
    def __init__(id, name, description, has_flag, has_moon):
        self.id = id
        self.name = name
        self.description = description
        self.has_flag = False

