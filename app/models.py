from sqlalchemy import Column, Integer, String
from .database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, default="pending")
    result = Column(String, nullable=True)