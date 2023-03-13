
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()



class Category(db.Model):
    __tablename__= 'category'
    id = db.Column(db.Integer, primary_key=True)
    cateoryName = db.Column(db.String(100))
    post = db.relationship('Post', backref='category', lazy=True)

    def __repr__(self):
        return f"{self.name}"

    @classmethod
    def get_all_Category(cls):
        return cls.query.all()

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(255), nullable=True,default='image.png')
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow, onupdate=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable= True,default=1)

    @staticmethod
    def create(title, body, description,image,created_at,updated_at,category_id):  
        new_post = Post(title=title, body=body, description=description,image=image,
                        created_at=created_at, updated_at=updated_at,category_id=category_id)
        db.session.add(new_post)
        db.session.commit()

    def __repr__(self):
        return f"Post {self.id}: {self.title}"

