from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Movie(db.Document):
    movie_id = db.SequenceField()
    name = db.StringField(required=True, unique=True)
    genres = db.ListField(db.StringField(), required=True)
    # added_by = db.ReferenceField('User')

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=8)
    watch_list = db.ListField()
    # isSeen = db.BooleanField(default=True)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf-8')
        
    def check_password(self, password):
        return check_password_hash(self.password, password)

User.register_delete_rule(Movie, 'added_by', db.CASCADE)