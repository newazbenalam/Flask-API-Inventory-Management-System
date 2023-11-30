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
      
# Get a product
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({"id": product.id, "name": product.name, 'description': product.description, "price": product.price}), 200
    return jsonify({"message": "Product not found"}), 404

# Get a product
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_single_products(product_id):
    product = Product.query.get(product_id)
    if product:
        data = request.get_json()
        product.name = data.get('name', product.name)
        product.price = data.get('price', product.price)
        db.session.commit()
        return jsonify({'id': product.id, 'name': product.name, 'price': product.price}), 200
    return jsonify({"message": "Product not found"}), 404
  
# Update a product
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if product:
        data = request.get_json()
        product.name = data.get('name', product.name)
        product.price = data.get('price', product.price)
        db.session.commit()
        return jsonify({"message": f"Product {product_id} updated successfully"}), 200
    return jsonify({"message": "Product not found"}), 404

# Delete a product
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": f"Product {product_id} deleted successfully"}), 200
    return jsonify({"message": "Product not found"}), 404
      
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return "Oh No, 500 Server Error!", 500


@app.errorhandler(404)
def not_found_error(error):
    return "404, Nothing to see here!", 404