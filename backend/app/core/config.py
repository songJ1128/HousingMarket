import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = os.getenv("DEBUG", True)
    DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///housing.db")
