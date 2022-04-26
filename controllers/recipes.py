
from models import recipes

def all(req):
    resp = recipes.return_all(req)
    return resp

def create(req):
    resp = recipes.create(req)
    return resp

def show_by_id(req, recipe_id):
    resp = recipes.show_by_id(req, recipe_id)
    return resp

def show_by_name(req, recipe_name):
    resp = recipes.show_by_name(req, recipe_name)
    return resp

def show_method_by_name(req, recipe_name):
    resp = recipes.show_method_by_name(req, recipe_name)
    return resp

def show_method_by_id(req, recipe_id):
    resp = recipes.show_method_by_id(req, recipe_id)
    return resp


