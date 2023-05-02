from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from appapp.models.planets import Planet

# ================================== HELPER FUNCTION =========================
# search for planet_id in data, return planet
# handle invalid planet_id, return 400
# responsible for validating & returning the instance of the planet

def validate_planet(planet_id):
    try: 
        planet_id = int(planet_id)
    except: 
        abort(make_response( {"message":f"planet id {planet_id}  is invalid"}, 400)) 

    # search for planet_id in data, return planet
    for planet in planets :
        if planet.id == int(planet.id):
            return planet
    # return a 404 for non-existing 
    abort(make_response({"message" : f"book {book_id} not found"}, 404))


# ================================== BLUEPRINT =========================
planet_bp = Blueprint("planets", __name__, url_prefix="/planets")


# ============================= CREATE ============================= 
# route for creating a planet
@planet_bp.route("", methods=["POST"])
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


# ============================= READ ALL ============================= 
# route with GET method to read all planets
# @planets_bp.route("/planets", methods=["GET"])
@planet_bp.route("", methods=["GET"])
def get_all_planets():
    planet_response_body = []
    
    for planet in planets:
        planet_response_body.append({
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "has_flag" : planet.has_flag
        }) 
    return jsonify(planet_response_body)

# ============================= READ ONE ============================= 

# route with GET method to read one planet
# @planets_bp.route("/planets", methods=["GET"])
# get one planet, example: http://localhost:5000/planets/2:
@planet_bp.route("/<planet_id>", methods = ["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    
    return {
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "has_flag" : planet.has_flag
    }    
    

#  ORIGINAL 
# def get_one_planet(planet_id):
#     try: 
#         planet_id = int(planet_id)    
#     except: 
#         return {"message":f"Planet {planet_id} is invalid"}, 400
#     for planet in planets:
#         if planet.id == planet_id:
#             return {
#                 "id" : planet.id,
#                 "name" : planet.name,
#                 "description" : planet.description,
#                 "has_flag" : planet.has_flag
#             }
#     # handles non-existing planet id numbers, like http://localhost:5000/planets/12 : 
#     return {"message":f"planet {planet_id} not found"}, 404

# ============================= UPDATE ============================= 

# ============================= DELETE ============================= 

@planet_bp.route("<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return {"message":f"planet id {planet_id}  is invalid"}, 400 

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet: {crystal_id} succesfully deleted", 200)

# Creating the Moon Blueprint 
# moons_bp = Blueprint("moons", __name__)

# Defining READ Routes with GET method for Moons
# @moons_bp.route("/moons", methods=["GET"])
# def endpoint_name():
#     response_body = "Hello, Moons!"
#     return response_body


