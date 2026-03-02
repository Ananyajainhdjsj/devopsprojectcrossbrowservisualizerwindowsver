import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://devopsuser:devopspass@db:5432/devopsdb"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False