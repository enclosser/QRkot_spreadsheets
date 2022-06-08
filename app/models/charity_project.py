from sqlalchemy import Column, String

from app.core.db import Base, InvestFields


class CharityProject(Base, InvestFields):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String, nullable=False)
