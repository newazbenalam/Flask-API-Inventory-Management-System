from app import db

# SQLAlchemy model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float)

    def __repr__(self):
        return f'<Product {self.id}: {self.name}>'
