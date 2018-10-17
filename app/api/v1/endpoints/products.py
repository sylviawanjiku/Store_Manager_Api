from flask import Flask, make_response, jsonify, request
from flask_restful import Api, Resource ,reqparse
from ..models.product_model import Product

parser =reqparse.RequestParser()

parser =reqparse.RequestParser()
parser.add_argument('product_name')
parser.add_argument('brand',type =str)
parser.add_argument('quantity',type = int)
parser.add_argument('price', type =int)
class Products(Resource):
    products = []
    def get(self,product_id = None):
        # Get all products in the list
        if product_id is None:
            # If the list is empty
            if len(Products.products) == 0:
                return make_response(jsonify({
                'message': 'The product list is empty'
                }), 200)
            # If the list is not empty
            product = Product.get_products(self)
            return make_response(jsonify(
                {
                    'status': 'Ok',
                    'Message': 'success',
                    'product': product
                }
            ), 200)
        # # Get a single product from the products list
        # single_product = [product for product in Products.products if int(product['id']) == int(product_id)]
        
        # # Identify a single item with it's id and fetch it
        # if single_product:
             one_product = Product.get_single_product(self,product_id) 
             return make_response(jsonify({
                'status': 'ok',
                'message': 'success',
                'product': one_product
            }), 200)
         # Identify a single item with it's id and fetch it and if it's not present return the following    
        return make_response(jsonify({
            'status': 'failed',
            'message': 'not found'
        }), 404)

       
    def post(self):
        # Posting items to products
        
        args = parser.parse_args()
        product_name = args['product_name']
        brand = args['brand']
        quantity = args['quantity']
        price = args['price']     
        
        my_product = Product(product_name,brand,quantity,price)
        new_product = my_product.post_product()
        return make_response(jsonify({
                'product': new_product
            }), 201)