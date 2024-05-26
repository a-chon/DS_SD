from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    mbti = Column(String)

class MBTIDescription(Base):
    __tablename__ = 'mbti_descriptions'
    mbti = Column(String, primary_key=True)
    description = Column(String)

class MBTIType(Base):
    __tablename__ = 'mbti_types'
    id = Column(Integer, primary_key=True)
    name = Column(String)

# class Compatibility(Base):
#     __tablename__ = 'compatibilities'
#     id = Column(Integer, primary_key=True)
#     mbti_type1 = Column(String)
#     mbti_type2 = Column(String)
#     compatibility_score = Column(Integer)


engine = create_engine('sqlite:///mbti_app.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
