from config import db
from models import User, UserSparkSession, SparkSessionTask

# Create the database
db.create_all()
