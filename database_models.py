from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#A user is a website owner that uses Lightning Shield
class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
	username = Column(String, nullable=False)
	password = Column(String, nullable=False)
	email = Column(String, nullable=False)
	time_of_creation = Column(Integer, nullable=False)
	full_name = Column(String, nullable=False)
	admin = Column(Integer, default=0)

#A website is a website that the user has access to
class Website(Base):
	__tablename__ = 'websites'
	id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
	host = Column(String, nullable=False)
	ip = Column(String, nullable=False)
	user_id = Column(Integer, default=0)
	time_of_creation = Column(Integer, nullable=False)

#A BlockedIP is an IP that is blocked by Lightning Shield for causing damage (attacker's IP)
class BlockedIPs(Base):
	__tablename__ = 'blockedips'
	id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
	ip = Column(String, nullable=False)
	reason_id = Column(Integer, default=0)
	time_of_creation = Column(Integer, nullable=False)
