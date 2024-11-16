import os

class Config:
    UPLOAD_FOLDER = './uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx'}
    SECRET_KEY = 'your_secret_key'  # Replace with a real secret key for production
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
