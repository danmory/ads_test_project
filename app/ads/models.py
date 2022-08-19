from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from common.database import Base


class Ad(Base):
    __tablename__ = "ads"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True, index=True)
    image_url = Column(String, nullable=True)
    author_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("User", back_populates="ads")
