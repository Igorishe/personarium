from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import declarative_base

from src.constants import ColorTypes, DifficultyLevels


Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name_ru = Column(String(255), nullable=False)
    name_en = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    created = Column(DateTime, default=datetime.utcnow)
    difficulty = Column(Enum(DifficultyLevels), default=DifficultyLevels.easy)
    color = Column(Enum(ColorTypes), default=ColorTypes.green)

    def __repr__(self):
        return f'{self.name_en}: {self.difficulty}: {self.color}'
