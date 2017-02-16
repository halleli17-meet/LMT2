from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
#from passlib.apps import custom_app_context as pwd_context
import random, string
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)


Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    gender = Column(String(255))
    profile_info = Column(String(255))
    favorite_videos = relationship("video", back_populates="videoAssociation")
    photo = (String(255))
    password_hash = Column(String(255))
    def hash_password(self, password):
    	self.password_hash = pwd_context.encrypt(password)
    def verify_password(self, password):
    	return pwd_context.verify(password, self.password_hash)

class Video(Base):
	__tablename__ = 'video'
	id = Column(Integer, primary_key=True)
	name = Column(String(255))
	makeup_area = Column(String(255))
	video_url = (String(255))
	description = (String(255))
	usersID = relationship("User", back_populates="videoAssociation")

class VideoAssociation(Base):
	__tablename__ = 'videoAssociation'
	user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
	video_id = Column(Integer, ForeignKey('video.id'), primary_key=True)
	user = relationship("User", back_populates="videodte")
	video = relationship("video", back_populates="user")

engine = create_engine('sqlite:///fizzBuzz.db')

Base.metadata.create_all(engine)