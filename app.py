from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
from controllers import recipes
from werkzeug import exceptions
from controllers import movies
import asyncio


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
       'GET':recipes.show_method_by_id 
    }
    resp, code = fns[request.method](request, recipe_id)
    return jsonify(resp), code

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"message": f"Wilkes company is sorry you haven't found the resource you're looking for {err} contact:0123456789"})

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"message" : f"It's not you, it's us {err}"})


@app.route('/searchmovies/', methods = ['GET', 'POST'])
async def get_all():
    data = await movies.get_all_movies()
    if request.method == 'POST':
        movie_name = request.form['movie']
        return redirect(url_for('get_movie', movie_name = movie_name))
    movie_name = ''
    
    return render_template('searchResults.html',movies = data )


@app.route('/searchmovies/<string:movie_name>', methods = ['GET', 'POST'])
async def get_movie(movie_name):
    if request.method == 'POST':
        movie_name = request.form['movie']
        return redirect(url_for('get_movie', movie_name = movie_name))
    data = await movies.get_by_name(movie_name)
    return render_template('searchResults.html',movies = data )



# if __name__ == "__main__":
#   asyncio.run(app)
