from database import engine, Base
from models import User, Profile

Base.metadata.create_all(bind=engine)