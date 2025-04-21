from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import random
import string

db = SQLAlchemy()

def generate_short_code(length=6):
    """Generate a random short code"""
    chars = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choice(chars) for _ in range(length))
        # Check if code already exists
        if not URL.query.filter_by(short_code=short_code).first():
            return short_code

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    access_count = db.Column(db.Integer, default=0)

    def to_dict(self):
        """Convert URL object to dictionary"""
        return {
            'id': self.id,
            'url': self.original_url,
            'shortCode': self.short_code,
            'createdAt': self.created_at.isoformat() + 'Z',
            'updatedAt': self.updated_at.isoformat() + 'Z',
            'accessCount': self.access_count
        }