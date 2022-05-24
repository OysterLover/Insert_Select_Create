import sqlalchemy
from pprint import pprint

db = 'postgresql://test:test@localhost:5432/test'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

pprint(connection.execute(
"""
SELECT title, year FROM album
WHERE year = 2018;
""").fetchall())

pprint(connection.execute(
"""
SELECT title, playing_time FROM track
WHERE playing_time = (
    SELECT MAX(playing_time) FROM track);
""").fetchall())

pprint(connection.execute(
"""
SELECT title FROM track
WHERE playing_time >= 240;
""").fetchall())

pprint(connection.execute(
"""
SELECT title FROM compilation
WHERE year >= 2018 AND year <= 2020;
""").fetchall())

# запрет на пробелы в имени дает псевдонимы состоящ. из 1 слова
pprint(connection.execute(
"""
SELECT pseudonym FROM musician
WHERE pseudonym NOT LIKE '%% %%';
""").fetchall())

pprint(connection.execute(
"""
SELECT title FROM track
WHERE title LIKE '%%my%%';
""").fetchall())