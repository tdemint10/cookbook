def register_routes(api, app, root="api"):
    from app.recipe import register_routes as attach_recipe
    from app.shopping_list import register_routes as attach_shopping_list

    # add routes
    attach_recipe(api, app)
    attach_shopping_list(api, app)
