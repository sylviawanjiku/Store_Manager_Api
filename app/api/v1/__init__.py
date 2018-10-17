from flask_restful import Api
from flask import Blueprint

from .endpoints.products import Products
from .endpoints.sales import SalesRecord

version1 = Blueprint ('api',__name__, url_prefix='/api/v1')

api = Api(version1)
api.add_resource(Products, '/products','/products/<product_id>')
api.add_resource(SalesRecord ,'/sales','/sales/<sale_id>')