# import modules
from app import db

# importing the Planet model
from app.models.planet import Planet

# import dependencies
from flask import Blueprint, jsonify, abort, make_response, request



# ================================== HARD CODED DATA =========================

# Define a `Planet` class with attributes:
# `id`, `name`,`description`, and one additional(has_flag)

# class Planet:
#     def __init__(self, id, name, description, has_flag= False):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.has_flag = has_flag



# Create a list of `Planet` instances
# (ordered nearest to the sun to the furthest)

# planets = [
#     Planet(1, "Mercury", "The closest to the sun. Rocky terrestrial planet."),
#     Planet(2, "Venus", "2nd closest to the sun. Rocky terrestrial planet."),
#     Planet(3, "Earth", "3rd closest to the sun. Rocky terrestrial planet."),
#     Planet(4, "Mars", "4th closest to the sun. Rocky terrestrial planet."),
#     Planet(5, "Jupiter", "5th closest to the sun. Jovian planet, one of the gas giants."),
#     Planet(6, "Saturn", "6th closest to the sun. Jovian planet, one of the gas giants."),
#     Planet(7, "Uranus", "7th closest to the sun. Jovian planet,one of the ice giants."),
#     Planet(8, "Neptune", "8th closest to the sun. Jovian planet, one of the ice giants."),
#     Planet(9, "Pluto", "9th closets to the sun. A controversial dwarf planet, with wildly tilted, elliptical orbit"),
# ]


# ================================== BLUEPRINT =========================
# creating the Blueprint instance to group all routes that 
# start with /planets
# "planets" is the debugging name for this Blueprint
# __name__ provides information the blueprint uses for certain aspects of routing

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


# ================================== HELPER FUNCTION =========================
# search for planet_id in data, return planet
# handle invalid planet_id, return 400
# responsible for validating & returning the instance of the planet
# orignal:
# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet_id

#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))


def validate_model(cls,model_id):
    try: 
        model_id = int(model_id)
    except: 
        abort(make_response({"message" :f"{cls.__name__} id {model_id}  is invalid ({type(model_id)}. Must be an integer"}, 400)) 
    
    model = cls.query.get(model_id)
    
    if not model:
        abort(make_response({"message" :f"{cls.__name__} {model_id} does not exist"}, 404))

    # search for planet_id in data, return planet
    # for planet in planets:
    if  model.id == model_id:
        return model
    
    
        

# ============================= CREATE ============================= 
# route for creating a planet
# the decorator that uses the planets_bp Blueprint to define an endpoint and method

# The function after the decorator will execute whenever a 
# matching HTTP request is received.

    # request_body variable holds the body contents of the HTTP request 
    # in a Python data structure
    
    # new_planet variable to hold the new instance of Planet 
    # and uses the data in request_body. 
    
    # name, description and has_flag are keyword arguments that match our model attributes, 
    # and access the request_body values to create the Planet instance
@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    
    # error checking/ input validation
    # fixes 500 internal error for invalid request
    if "name" not in request_body or "description" not in request_body:
        return make_response("Invalid request", 400)
    
    # new_planet = Planet(name = request_body["name"],
    #     description = request_body["description"],
    #     has_flag = request_body["has_flag"]
    # )
    # refactored:
    new_planet = Planet.from_dict(request_body)
    

#     # the database's way of collecting changes(add(new_planet)) that need to be made
    db.session.add(new_planet)
    
#     # database to save and commit the collected changes
    db.session.commit()

    
#     # return the HTTP response for the endpoint
#     # make_response instantiates a Response object.
#     # (parameter) is the HTTP response body as a string, 
#     # unless we have more specific requirements
#     # 201 response code, 200 is the default
    return make_response(f"Planet {new_planet.name} successfully created", 201)


# ============================= READ ALL ============================= 
# Defining READ Routes with GET method for Planets
@planets_bp.route("", methods=["GET"])

def get_all_planets():
    planets_response = []
    # planets = validate_planet(planet_id)
    
    # updated from query params lesson
    name_query = request.args.get("name")
    
    if name_query is not None: 
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()

    
    for planet in planets:
        # planets_response.append({
        #     "id" : planet.id,
        #     "name" : planet.name,
        #     "description" : planet.description,
        #     "has_flag" : planet.has_flag
        # }) 
        # refactor:
        planets_response.append(planet.to_dict())
        
    return jsonify(planets_response, 200)

# ============================= READ ONE ============================= 
# route with GET method to read one planet
# @planets_bp.route("/planets", methods=["GET"])
# get one planet, example: http://localhost:5000/planets/2:
@planets_bp.route("/<planet_id>", methods = ["GET"])

# using helper function: 
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    
    # return {
    #         "id" : planet.id,
    #         "name" : planet.name,
    #         "description" : planet.description,
    #         "has_flag" : planet.has_flag
    # }    
    # refactor:
    return planet.to_dict()

# original :
# def get_one_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         return {"message":f"Planet id {planet_id} is invalid"}, 400
    
    
#     for planet in planets:
#         if planet.id == planet_id:
#             return {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "has_flag": planet.has_flag
#             }
#     return {"message":f"planet {planet_id} not found"}, 404


# ============================= UPDATE ============================= 
# route for updating a planet with PUT method
@planets_bp.route("/<planet_id>", methods = ["PUT"])
def update_planet(planet_id):
    
    # query our db to grab the planet that has the id we want
    # planet = Planet.query.get(planet_id)
    planet = validate_model(Planet,planet_id)
    
    request_body = request.get_json()
    
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.has_flag = request_body["has_flag"]
    
    db.session.commit()
    
    # send back the updated planet
    return make_response(f"Planet #{planet.id} successfully updated"), 200
    # return ({"id": planet.id,
    #         "name": planet.name,
    #         "description": planet.description,
    #         "has_flag": planet.has_flag
    #         }), 200


# ============================= DELETE ============================= 
# route for deleting a planet with DELETE method
@planets_bp.route("/<planet_id>", methods = ["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(Planet,planet_id) 

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet: {planet_id} succesfully deleted", 200)



