# models.py
from sqlalchemy import Column, Integer, String, Text, Date
from db import Base

class JobPost(Base):
    __tablename__ = "job_posts"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String(100), nullable=False)
    title = Column(String(255), nullable=False)
    location = Column(String(255), nullable=True)
    url = Column(String(500), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    date_posted = Column(Date, nullable=True)
    date_scraped = Column(Date, nullable=False)
