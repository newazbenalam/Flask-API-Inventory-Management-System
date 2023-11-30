from app import app, db
from app.model import Product
from flask import jsonify, request


@app.route('/api/products', methods=['POST'])
def add_product():
  data = request.get_json()
  name = data['name']
  price = data['price']
  description = data['description']
    
  new_product = Product(name=name, price=price, description=description)
  db.session.add(new_product)
  db.session.commit()

  return jsonify({"message": "Product added successfully"}), 200
  
@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price} for product in products])
      
      
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return "Oh No, 500 Server Error!", 500


@app.errorhandler(404)
def not_found_error(error):
    return "404, Nothing to see here!", 404