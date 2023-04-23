from flask import Blueprint

# Creating the Blueprints 
planets_bp = Blueprint("planets", __name__)
moons_bp = Blueprint("moons", __name__)

# Defining READ Routes with GET method
@planets_bp.route("/planets", methods=["GET"])
def endpoint_name():
    response_body = "Hello, Planets!"
    return response_body

@moons_bp.route("/moons", methods=["GET"])
def endpoint_name():
    response_body = "Hello, Moons!"
    return response_body


class Planets:
    def __init__(id, name, description, has_flag= False):
        self.id = id
        self.name = name
        self.description = description
        self.has_flag = has_flag

# planets = [
#     Planets(name, description),
#     Planets(name, description),
#     Planets(name, description),
#     Planets(nname, description),
#     Planets(name, description),
# ]