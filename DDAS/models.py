from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dataset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    checksum = db.Column(db.String(64), unique=True, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(512), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Dataset {self.name}>'
