from sqlalchemy import (
    create_engine, Column, Integer, String, Date
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Video Games" table
class Game(base):
    """Model for the Games table."""
    __tablename__ = "Games"

    id = Column(Integer, primary_key=True, autoincrement=True)
    game_name = Column(String(255), nullable=False)
    release_date = Column(Date)
    genre = Column(String(255))
    platform = Column(String(255))
    

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records the Games
pac_man = Game(
    game_name = "Pac Man",
    release_date = datetime.date(1980, 5, 22),
    genre = "Action",
    platform = "Atari 2600"
)    

zelda = Game(
    game_name = "The Legend of Zelda: Breath of the Wild",
    release_date = datetime.date(2017, 3, 3),
    genre = "Action-adventure",
    platform = "Nintendo Switch"
)

witcher = Game(
    game_name = "The Witcher 3: Wild Hunt",
    release_date = datetime.date(2015, 5, 19),
    genre = "Action role-playing",
    platform = "PlayStation 4, Xbox One, PC, Nintendo Switch"
)

god_of_war = Game(
    game_name = "God of War",
    release_date = datetime.date(2018, 4, 20),
    genre = "Action-adventure",
    platform = "PlayStation 4"
)

red_dead_redemption = Game(
    game_name = "Red Dead Redemption 2",
    release_date = datetime.date(2018, 10, 26),
    genre = "Action-adventure",
    platform = "PlayStation 4, Xbox One, PC"
)

minecraft = Game(
    game_name = "Minecraft",
    release_date = datetime.date(2011, 11, 18),
    genre = "Sandbox, survival",
    platform = "PC, PlayStation 4, Xbox One, Nintendo Switch, mobile devices"
)

# adding the games to the session
session.add(pac_man)
session.add(zelda)
session.add(witcher)
session.add(god_of_war)
session.add(red_dead_redemption)
session.add(minecraft)

# committing the records to the database
session.commit()


# query the database to find all games and print their details
games = session.query(Game).all()
for game in games:
    print(
        game.id,
        game.game_name,
        game.release_date,
        game.genre,
        game.platform,
        sep=" | "
    )