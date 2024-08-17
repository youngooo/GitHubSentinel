import os

class Config:
    API_KEY = os.getenv('GITHUB_API_KEY')
    DATABASE_URI = os.getenv('DATABASE_URI')
