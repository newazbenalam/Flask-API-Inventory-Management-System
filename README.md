# Inventory Management System API

This API serves as the backend for BongoDev's Inventory Management System, providing endpoints to manage product inventory.

## Author

- **Author:** Newaz Ben Alam
- **Email:** newazbenalam@gmail.com

## Description

This Flask-based API powers the Inventory Management System for BongoDev. It handles CRUD operations for managing product inventory, allowing users to add, retrieve, update, and delete products.

## Features

- **Create Product:** Add a new product to the inventory.
- **Read Products:** Fetch all products or retrieve a specific product by ID.
- **Update Product:** Modify existing product information.
- **Delete Product:** Remove a product from the inventory.

## Technologies Used

- **Flask:** Python web framework used for building the API.
- **SQLAlchemy:** ORM used for database interactions.
- **MySQL:** Database management system for storing product data.

## Setup Instructions

1. Clone the repository: `git clone https://github.com/newazbenalam/Flask-API-Inventory-Management-System.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up the database configuration in `config.py`.
4. Run the Flask application: `python app.py`
5. Access the API endpoints via `http://localhost:5000`.

## API Endpoints

- `GET /api/products`: Retrieve all products.
- `GET /api/products/<product_id>`: Get details of a specific product by ID.
- `POST /api/products`: Add a new product to the inventory.
- `PUT /api/products/<product_id>`: Update details of a specific product.
- `DELETE /api/products/<product_id>`: Delete a product from the inventory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
