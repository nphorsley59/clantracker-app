from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Player(Base):
    __tablename__ = "players"
    tag = Column(String(20), primary_key=True)
    name = Column(String(100))
    role = Column(String(10))

    def __repr__(self):
        return f"Player(id={self.tag!r}, name={self.name!r}, fullname={self.role!r})"
