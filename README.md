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

## Sample Product JSON

```json
{
	"name": "Potato",
	"description": "Nice fresh potato",
	"price": 40.99
}
```

## Application Structure
```
project/
|-- app/
|   |-- models/
|   |   |-- __init__.py
|   |   |-- product.py
|   |
|   |-- views/
|   |   |-- __init__.py
|   |   |-- product_views.py
|   |
|   |-- controllers/
|   |   |-- __init__.py
|   |   |-- product_controller.py
|   |
|   |-- services/
|   |   |-- __init__.py
|   |   |-- product_service.py
|   |
|   |-- templates/
|   |   |-- index.html
|   |   |-- user/
|   |   |   |-- profile.html
|   |   |-- product/
|   |   |   |-- list.html
|   |
|   |-- static/
|       |-- style.css
|
|-- config.py
|-- run.py

```

- app/models: Contains your database models (e.g., User, Product).
- app/views: Defines your routes, and views, and handles HTTP requests.
- app/controllers: Contains functions to manage complex business logic.
- app/templates: Stores HTML templates for rendering views.
- app/static: Stores static files like CSS, JavaScript, images, etc.
- app/services: Components responsible for specific business logic.
- config.py: Configuration settings for your Flask app.
- run.py: Entry point to start your Flask app.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Screenshot

![Screenshot 1](https://raw.githubusercontent.com/newazbenalam/Flask-API-Inventory-Management-System/656985c65fbb492aae6f3bd5bba03926a2762f4a/docs/Screenshot-1.png)
