from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from .models.planet import Planet


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        has_flag = request_body["has_flag"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return f"Planet: {request_body['name']} was created.", 201
# Defining READ Routes with GET method for Planets
# @planets_bp.route("/planets", methods=["GET"])


@planets_bp.route("", methods=["GET"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planets(
        name = request_body["name"],
        description= request_body["description"],
        has_flag= request_body["has_flag"]
    )

def get_planets_endpoint():
    planet_response_body = []
    
    for planet in planets:
        planet_response_body.append({
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "has_flag" : planet.has_flag
        }) 
    return jsonify(planet_response_body)




# ================================== WAVE 2 =========================
#helper function



# get one planet, example: http://localhost:5000/planets/2:
@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_planet(planet_id):
    # planet_id = int(planet_id)
    
    # placing the above line within a try/ except block
    try:
        planet_id = int(planet_id)
    except:
        return {"message":f"planet id {planet_id}  is invalid"}, 400 
    
    for planet in planets:
        if planet.id == planet_id:
            return {
                "id" : planet.id,
                "name" : planet.name,
                "description" : planet.description,
                "has_flag" : planet.has_flag
            }
    # handles non-existing planet id numbers, like http://localhost:5000/planets/12 : 
    return {"message":f"planet {planet_id} not found"}, 404


# Creating the Moon Blueprint 
# moons_bp = Blueprint("moons", __name__)

# Defining READ Routes with GET method for Moons
# @moons_bp.route("/moons", methods=["GET"])
# def endpoint_name():
#     response_body = "Hello, Moons!"
#     return response_body

