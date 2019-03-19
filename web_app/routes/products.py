
from flask import Blueprint, request, render_template, jsonify, flash, redirect #, url_for

product_routes = Blueprint("product_routes", __name__)

#
# LIST (TABLE)
#

@product_routes.route("/products")
def index():
    print("VISITING THE PRODUCTS INDEX PAGE")
    products = [ # TODO: get these products from a datastore
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
        {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
        {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
        {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
        {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
        {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
        {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
        {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
        {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
        {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
        {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
        {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
    ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017
    return render_template("products/index.html", products=products)

#
# NEW (FORM)
#

@product_routes.route("/products/new")
def new():
    print("VISITING THE NEW PRODUCT PAGE")
    print("REQUEST PARAMS:", dict(request.args))
    return render_template("products/new.html")

#
# CREATE
#

@product_routes.route("/products", methods=["POST"])
def create():
    print("CREATING A PRODUCT...")
    print("FORM DATA:", dict(request.form))
    product_name = request.form["product_name"]
    flash(f"Product '{product_name}' created successfully!", "success") # use the "success" category to correspond with twitter bootstrap alert colors
    return redirect("/products")

#
# SHOW
#

@product_routes.route("/products/<id>")
def show(id):
    print(f"VISITING THE PRODUCT SHOW PAGE (#{id})")

    # TODO: lookup product from the datastore by its id
    product = {"id":16, "name": "Product X", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50}

    if product:
        return render_template("products/show.html", product=product)
    else:
        flash(f"OOPS, Couldn't find a product with an identifier of '{id}'", "danger") # use the "danger" category to correspond with twitter bootstrap alert colors
        return redirect("/products")

#
# EDIT (FORM)
#

@product_routes.route("/products/<id>/edit")
def edit(id):
    print(f"VISITING THE PRODUCT EDIT PAGE (#{id})")

    # TODO: lookup product from the datastore by its id
    product = {"id":16, "name": "Product X", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50}

    if product:
        return render_template("products/edit.html", product=product)
    else:
        flash(f"OOPS, Couldn't find a product with an identifier of '{id}'", "danger") # use the "danger" category to correspond with twitter bootstrap alert colors
        return redirect("/products")

#
# UPDATE
#

@product_routes.route("/products/<id>/update", methods=["POST"])
def update(id):
    print(f"UPDATING PRODUCT (#{id})")
    # todo: lookup product from the datastore by its id
    # ... and if exists, delete it from the datastore
    flash(f"Updated product #{id}!", "info") # use the "info" category to correspond with twitter bootstrap alert colors
    return redirect("/products")

#
# DESTROY
#

@product_routes.route("/products/<id>/destroy", methods=["POST"])
def destroy(id):
    print(f"DESTROYING PRODUCT (#{id})")
    # todo: lookup product from the datastore by its id
    # ... and if exists, delete it from the datastore
    flash(f"Destroyed product #{id}!", "info") # use the "info" category to correspond with twitter bootstrap alert colors
    return redirect("/products")
