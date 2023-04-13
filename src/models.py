import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250),nullable=False)
    firstName = Column(String(250),nullable=False)
    lastName = Column(String(250),nullable=False)
    email = Column(String(250),nullable=False)


class UserFavorites(Base):
    __tablename__ = 'user_favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable=False)
    gender = Column(String(250),nullable=False)
    height = Column(String(250),nullable=False)
    mass = Column(String(250),nullable=False)
    hairColor = Column(String(250),nullable=False)
    eyeColor = Column(String(250),nullable=False)
    skinColor = Column(String(250),nullable=False)
    birthYear = Column(String(250),nullable=False)
    homeworld = Column(String(250),ForeignKey('homeworld.id'), nullable=True)
    
    description = Column(String(250),nullable=False)

class Vechicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable=False)
    crew = Column(String(250), ForiegnKey (('character.id', 'pilot.id', 'films.id' nullable =False))
    model = Column(String(250),nullable=False)
    cargoCapacity = Column(String(250),nullable=False)
    maxAtmospheringSpeed = Column(String(250),nullable=False)
    passengers = Column(String(250),nullable=False)
    consumables = Column(String(250),nullable=False)
    vehiclesClass = Column(String(250),nullable=False)

class Films(Base):
    __tablename__ ='films'
    id = Column(Integer, primary_key=True)
    films_id = Column(Integer, ForeignKey('films.id'))

class Pilot(Base):   
    __tablename__ ='pilot' 
    id = Column(Integer,primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id', 'vechicles.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy bases
render_er(Base, 'diagram.png')
