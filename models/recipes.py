
recipes =  [
    {'id': 1, 'name': 'toast', 'ingredients': 'Bread, Butter', 'method': 'Put bread in toaster, then put butter on bread'},
    {'id': 2, 'name': 'pasta', 'ingredients': 'Pasta, salt', 'method': "Boilg pot of water, add salt to water and add pasta"},
    {'id': 3, 'name': 'chips', 'ingredients': 'Potatos', 'method': "preheat oven and add"}
]

def return_all(req):
    return_arr = []
    for r in recipes:
        return_arr.append({'id': r['id'], 'name' : r['name']})
    return_arr.append("For more info go /recpies/id or /recipes/name or recipes/name/method")
    return return_arr, 200

def show_by_id(req, recipe_id):
    try:
        return next(recipe for recipe in recipes if recipe['id'] == recipe_id), 200
    except:
        return f"We don't have a recipe with the id {recipe_id}", 404

def show_by_name(req,recipe_name):
    try:
        return_arr = []

        for r in recipes:
            if r['name'] == recipe_name.lower():
                return_arr.append({'id': r['id'], 'name' : r['name'], 'ingredients' : r['ingredients']})

        return return_arr,200

    except:
        return f"We don't have a recipe with that name ( {recipe_name} )", 404

def show_method_by_name(req, recipe_name):
    try:
        return_arr = []

        for r in recipes:
            if r['name'] == recipe_name.lower():
                return_arr.append({'id': r['id'], 'name' : r['name'], 'method' : r['method']})

        return return_arr,200

    except:
        return f"We don't have a recipe with that name ( {recipe_name} )", 404

def show_method_by_id(req, recipe_id):
    try:
        return_arr = []

        for r in recipes:
            if r['id'] == recipe_id:
                return_arr.append({'id': r['id'], 'name' : r['name'], 'method' : r['method']})

        return return_arr,200

    except:
        return f"We don't have a recipe with that name ( {recipe_id} )", 404


def create(req):    
    new_recipe = req.get_json()
    new_recipe['id'] = sorted([r['id'] for r in recipes]) [-1] +1
    recipes.append(new_recipe)
    return new_recipe, 201

# def update_by_id(req, recipe_id):
#     u_recipe = find_by_recipe_id(recipe_id)
#     data = req.get_json()
#     print(data)
#     for key, val in data.items():
#         u_recipe[key] = val
#     return u_recipe, 200


