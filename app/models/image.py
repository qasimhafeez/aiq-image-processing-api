from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    depth = db.Column(db.Float, nullable=False)
    image_data = db.Column(db.LargeBinary, nullable=False)

    @validates('depth')
    def validate_depth(self, key, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Depth must be a number')
        return value

    @validates('image_data')
    def validate_image_data(self, key, value):
        if not value:
            raise ValueError('Image data cannot be empty')
        return value
