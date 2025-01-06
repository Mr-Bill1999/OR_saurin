from sqlalchemy import Column, Integer, String
from app.database import Base


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    short_id = Column(String, unique=True, nullable=False)
    full_url = Column(String, nullable=False)
