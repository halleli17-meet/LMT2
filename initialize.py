from model import *


engine = create_engine('sqlite:///fizzBuzz.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()
newUser = User(name="halleli", email= "halleli.busheri@gmail.com", gender= "female",profile_info= "",favorite_videos="", photo= "",password_hash="meet123")
session.add(newUser)

newVideo = Video(name= "Full Makeup", mekeup_area= "face", video_url= "https://www.youtube.com/watch?v=pWxFcyIAWAE",descriptione= "blablabla", usersID= "halleli")

session.commit()