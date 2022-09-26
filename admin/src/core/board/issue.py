from datetime import datetime
from src.core.db import db

class Issue(db.Model):
    __tablename__ = "Issues"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String)
    title = db.Column(db.String)
    description = db.Column(db.String)
    status = db.Column(db.String)
    inserted_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now())
