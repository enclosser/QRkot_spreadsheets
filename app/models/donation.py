from fastapi_users_db_sqlalchemy.guid import GUID
from sqlalchemy import Column, ForeignKey, String

from app.core.db import Base, InvestFields


class Donation(Base, InvestFields):
    user_id = Column(GUID, ForeignKey('user.id'), nullable=False)
    comment = Column(String)
