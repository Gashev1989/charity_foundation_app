from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.base_model import BaseModel


class Donation(BaseModel):
    """Модель пожертвования."""
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
