from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func


Base = declarative_base()


class Player(Base):
    __tablename__ = "players"

    tag = Column(String(20), primary_key=True)
    name = Column(String(100))
    role = Column(String(10))

    status_logs = relationship("PlayerStatusLog", back_populates="tag")
    activity_logs = relationship("PlayerActivityLog", back_populates="tag")

    def __repr__(self):
        return f"Player(tag={self.tag!r}, name={self.name!r}, " \
               f"role={self.role!r})"


class PlayerStatusLog(Base):
    __tablename__ = "player_status_logs"

    id = Column(Integer, primary_key=True)
    player_tag = Column(String(20), ForeignKey("players.tag"))
    exp_level = Column(Integer)
    town_hall_level = Column(Integer)
    log_date = Column(DateTime, server_default=func.current_timestamp())

    tag = relationship("Player", back_populates="status_logs")

    def __repr__(self):
        return f"PlayerLog(id={self.id!r}, player_tag={self.player_tag!r}, " \
               f"exp_level={self.exp_level!r}, town_hall_level={self.town_hall_level!r}, " \
               f"log_date={self.log_date!r})"


class PlayerActivityLog(Base):
    __tablename__ = "player_activity_logs"

    id = Column(Integer, primary_key=True)
    player_tag = Column(String(20), ForeignKey("players.tag"))
    league = Column(String(25))
    trophies = Column(Integer)
    attack_wins = Column(Integer)
    donations_sent = Column(Integer)
    donations_received = Column(Integer)
    log_date = Column(DateTime, server_default=func.current_timestamp())

    tag = relationship("Player", back_populates="activity_logs")

    def __repr__(self):
        return f"PlayerLog(id={self.id!r}, player_tag={self.player_tag!r}, " \
               f"league={self.league!r}, trophies={self.trophies!r}, " \
               f"attack_wins={self.attack_wins!r}, donations_sent={self.donation_sent!r}, " \
               f"donations_received={self.donations_received!r}, " \
               f"log_date={self.log_date!r})"
