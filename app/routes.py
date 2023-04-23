from flask import Blueprint
from flask import jsonify

# Define a `Planet` class with attributes:
# `id`, `name`,`description`, and one additional(has_flag)
class Planet:
    def __init__(self, id, name, description, has_flag= False):
        self.id = id
        self.name = name
        self.description = description
        self.has_flag = has_flag

# Create a list of `Planet` instances
# (ordered nearest to the sun to the furthest)
planets = [
    Planet(1, "Mercury", "The closest to the sun. Rocky terrestrial planet."),
    Planet(2, "Venus", "2nd closest to the sun. Rocky terrestrial planet."),
    Planet(3, "Earth", "3rd closest to the sun. Rocky terrestrial planet."),
    Planet(4, "Mars", "4th closest to the sun. Rocky terrestrial planet."),
    Planet(5, "Jupiter", "5th closest to the sun. Jovian planet, one of the gas giants."),
    Planet(6, "Saturn", "6th closest to the sun. Jovian planet, one of the gas giants."),
    Planet(7, "Uranus", "7th closest to the sun. Jovian planet,one of the ice giants."),
    Planet(8, "Neptune", "8th closest to the sun. Jovian planet, one of the ice giants."),
    Planet(9, "Pluto", "9th closets to the sun. A controversial dwarf planet, with wildly tilted, elliptical orbit"),
]


# Creating the Planet Blueprint 
# planets_bp = Blueprint("planets", __name__)
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


# Defining READ Routes with GET method for Planets
# @planets_bp.route("/planets", methods=["GET"])
@planets_bp.route("", methods=["GET"])

def endpoint_name():
    planet_response_body = []
    
    for planet in planets:
        planet_response_body.append({
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "has_flag" : planet.has_flag
        }) 
    return jsonify(planet_response_body)


# Creating the Moon Blueprint 
# moons_bp = Blueprint("moons", __name__)

# Defining READ Routes with GET method for Moons
# @moons_bp.route("/moons", methods=["GET"])
# def endpoint_name():
#     response_body = "Hello, Moons!"
#     return response_body

