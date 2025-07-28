# scripts/init_db.py
from db import Base, engine
from models import JobPost

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done.")
