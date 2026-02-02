from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, ForeignKey, Column, Integer, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


db = SQLAlchemy()

favorites_characters = Table(
    "favorites_characters",
    db.Model.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("character_id", Integer, ForeignKey(
        "character.id"), primary_key=True)
)
favorites_location = Table(
    "favorites_location",
    db.Model.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("location_id", Integer, ForeignKey("location.id"), primary_key=True)
)


class User(db.Model):
    __table__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    fav_characters: Mapped[list["Characters"]] = relationship(
        secondary=favorites_characters, back_populates="favorites_by")
    fav_location: Mapped[list["Location"]] = relationship(
        secondary=favorites_location, back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
           

        }


class Characters(db.Model):
    __tablename__ = "characters"
    id: Mapped[int] = mapped_column(primary_key=True)
    age: Mapped[int] = mapped_column(String(25))
    birthdate: Mapped[str] = mapped_column(String(25))
    gender: Mapped[str] = mapped_column(String(25))
    name: Mapped[str] = mapped_column(String(25)) 
    occupation: Mapped[str] = mapped_column(String(25))
    portrait_path: Mapped[str] = mapped_column(String(25))
    phrases: Mapped[str] =mapped_column(String(300))

    favorites_by: Mapped[list["User"]] = relationship(
        secondary=favorites_characters, back_populates="fav_characters")

    def serialize(self):
        return {
            "id": self.id,
            "age": self.age,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "name": self.name,
            "occupation": self.occupation,
            "portrait_path": self.portrait_path,
            "phrases": self.phrases,

        }


class Location(db.Model):
    __tablename__ = "location"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(), String(25),
    image_path: Mapped[str] = String(100),
    use: Mapped[str] = String(300),

    favorites: Mapped[list["User"]] = relationship(
        secondary=favorites_location, back_populates="fav_location")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation,
            "image_path": self.image_path,
            "phrases": self.phrases,

        }
