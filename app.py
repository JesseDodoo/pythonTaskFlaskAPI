from flask import Flask, request, jsonify
from flask_cors import CORS
from controllers import recipes


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'API for connecting Zeia and Jesse', 200

@app.route('/recipes', methods=['GET', 'POST'])
def recipes_handler():
    fns = {
        'GET': recipes.all,
        'POST': recipes.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/recipes/<int:recipe_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def recipe_handler(recipe_id):
    fns = {
        'GET': recipes.show_by_id,
        # 'PATCH': recipes.update_by_id,
        # 'PUT': recipes.update_by_id,
        # 'DELETE': recipes.destroy_by_id
    }
    resp, code = fns[request.method](request, recipe_id)
    return jsonify(resp), code

@app.route('/recipes/<string:recipe_name>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def recipe_name_handler(recipe_name):
    fns = {
        'GET': recipes.show_by_name,
        # 'PATCH': recipes.update_by_name,
        # 'PUT': recipes.update_by_name,
        # 'DELETE': recipes.destroy_by_name
    }
    resp, code = fns[request.method](request, recipe_name)
    return jsonify(resp), code

@app.route('/recipes/<string:recipe_name>/method', methods=['GET'])
def recipe_method_handler(recipe_name):
    fns = {
       'GET':recipes.show_method_by_name 
    }
    resp, code = fns[request.method](request, recipe_name)
    return jsonify(resp), code

@app.route('/recipes/<int:recipe_id>/method', methods=['GET'])
def recipe_methodid_handler(recipe_id):
    fns = {
       'GET':recipes.show_method_by_name 
    }
    resp, code = fns[request.method](request, recipe_id)
    return jsonify(resp), code

