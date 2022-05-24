import sqlalchemy
from pprint import pprint

db = 'postgresql://test:test@localhost:5432/test'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# #INSERT INTO genre_musician
# connection.execute(
# """
# INSERT INTO genre_musician
# VALUES (1, 1, 1);
# """)
#
# connection.execute(
# """
# INSERT INTO genre_musician
# VALUES (2, 2, 3);
# """)
#
# connection.execute(
# """
# INSERT INTO genre_musician
# VALUES (3, 2, 4);
# """)
#
# connection.execute(
# """
# INSERT INTO genre_musician
# VALUES (4, 2, 5);
# """)
#
# connection.execute(
# """
# INSERT INTO genre_musician
# VALUES (5, 3, 6);
# """)
#
# connection.execute(
# """
# INSERT INTO genre_musician
# VALUES (6, 3, 8);
# """)
#
# connection.execute(
# """
# INSERT INTO genre_musician
# VALUES (7, 4, 7);
# """)
#
# connection.execute(
# """
# INSERT INTO genre_musician
# VALUES (8, 5, 2);
# """)

# INSERT INTO album
# connection.execute(
# """
# INSERT INTO album
# VALUES (1, 'sunshine', 1989);
# """)
#
# connection.execute(
# """
# INSERT INTO album
# VALUES (2, 'beautiful_life', 2000);
# """)
#
# connection.execute(
# """
# INSERT INTO album
# VALUES (3, 'life_and_death', 1964);
# """)
#
# connection.execute(
# """
# INSERT INTO album
# VALUES (4, 'pinkblack', 1999);
# """)
#
# connection.execute(
# """
# INSERT INTO album
# VALUES (5, 'just_music', 1972);
# """)
#
# connection.execute(
# """
# INSERT INTO album
# VALUES (6, 'ice_cream', 1950);
# """)
#
# connection.execute(
# """
# INSERT INTO album
# VALUES (7, 'just_business', 2006);
# """)
#
# connection.execute(
# """
# INSERT INTO album
# VALUES (8, 'thats_it', 1980);
# """)

# INSERT INTO musician_album
# connection.execute(
# """
# INSERT INTO musician_album
# VALUES (1, 1, 8);
# """)
#
# connection.execute(
# """
# INSERT INTO musician_album
# VALUES (2, 2, 7);
# """)
#
# connection.execute(
# """
# INSERT INTO musician_album
# VALUES (3, 3, 6);
# """)
#
# connection.execute(
# """
# INSERT INTO musician_album
# VALUES (4, 4, 5);
# """)
#
# connection.execute(
# """
# INSERT INTO musician_album
# VALUES (5, 5, 4);
# """)
#
# connection.execute(
# """
# INSERT INTO musician_album
# VALUES (6, 6, 3);
# """)
#
# connection.execute(
# """
# INSERT INTO musician_album
# VALUES (7, 7, 2);
# """)
#
# connection.execute(
# """
# INSERT INTO musician_album
# VALUES (8, 8, 1);
# """)

# pprint(connection.execute(
# """
# SELECT * FROM musician_album;
# """).fetchall())

# INSERT INTO track
# connection.execute(
# """
# INSERT INTO track
# VALUES (1, 1, 'sun', 180);
# """)
#
# connection.execute(
# """
# INSERT INTO track
# VALUES (2, 1, 'shine', 280);
# """)
#
# connection.execute(
# """
# INSERT INTO track
# VALUES (3, 2, 'night', 647);
# """)
#
# connection.execute(
# """
# INSERT INTO track
# VALUES (4, 2, 'day', 90);
# """)
#
# connection.execute(
# """
# INSERT INTO track
# VALUES (5, 3, 'girl', 267);
# """)
#
# connection.execute(
# """
# INSERT INTO track
# VALUES (6, 3, 'cat', 387);
# """)
#
# connection.execute(
# """
# INSERT INTO track
# VALUES (7, 4, 'math', 240);
# """)
#
# connection.execute(
# """
# INSERT INTO track
# VALUES (8, 4, 'chemistry', 280);
# """)
#
# connection.execute(
# """
# INSERT INTO track
# VALUES (9, 5, 'color', 180);
# """)
#
# connection.execute(
# """
# INSERT INTO track
# VALUES (10, 5, 'rainbow', 180);
# """)
#
# connection.execute(
# """
# INSERT INTO track
# VALUES (11, 6, 'pick', 70);
# """)
#
# connection.execute(
# """
# INSERT INTO track
# VALUES (12, 6, 'blue', 90);
# """)
#
# connection.execute(
# """
# INSERT INTO track
# VALUES (13, 7, 'fish', 167);
# """)
#
# connection.execute(
# """
# INSERT INTO track
# VALUES (14, 7, 'chips', 280);
# """)
#
# connection.execute(
# """
# INSERT INTO track
# VALUES (15, 8, 'dream', 340);
# """)

# pprint(connection.execute(
# """
# SELECT * FROM track;
# """).fetchall())

#INSERT INTO compilation
# connection.execute(
# """
# INSERT INTO compilation
# VALUES (1, 'daisy', 2000);
# """)
#
# connection.execute(
# """
# INSERT INTO compilation
# VALUES (2, 'sunflower', 2018);
# """)
#
# connection.execute(
# """
# INSERT INTO compilation
# VALUES (3,  'chamomile', 2020);
# """)
#
# connection.execute(
# """
# INSERT INTO compilation
# VALUES (4, 'watermelon', 2019);
# """)
#
# connection.execute(
# """
# INSERT INTO compilation
# VALUES (5, 'rose', 2016);
# """)
#
# connection.execute(
# """
# INSERT INTO compilation
# VALUES (6, 'lilac', 2009);
# """)
#
# connection.execute(
# """
# INSERT INTO compilation
# VALUES (7, 'forgetmenot', 2005);
# """)
#
# connection.execute(
# """
# INSERT INTO compilation
# VALUES (8, 'primrose', 2021);
# """)

#INSERT INTO track_compilation
# connection.execute(
# """
# INSERT INTO track_compilation
# VALUES (1, 15, 1);
# """)
#
# connection.execute(
# """
# INSERT INTO track_compilation
# VALUES (2, 14, 8);
# """)
#
# connection.execute(
# """
# INSERT INTO track_compilation
# VALUES (3, 13, 6);
# """)
#
# connection.execute(
# """
# INSERT INTO track_compilation
# VALUES (4, 12, 5);
# """)
#
# connection.execute(
# """
# INSERT INTO track_compilation
# VALUES (5, 11, 5);
# """)
#
# connection.execute(
# """
# INSERT INTO track_compilation
# VALUES (6, 10, 4);
# """)
#
# connection.execute(
# """
# INSERT INTO track_compilation
# VALUES (7, 9, 3);
# """)
#
# connection.execute(
# """
# INSERT INTO track_compilation
# VALUES (8, 8, 2);
# """)
#
# connection.execute(
# """
# INSERT INTO track_compilation
# VALUES (9, 7, 1);
# """)
#
# connection.execute(
# """
# INSERT INTO track_compilation
# VALUES (10, 6, 8);
# """)
#
# connection.execute(
# """
# INSERT INTO track_compilation
# VALUES (11, 5, 6);
# """)
#
# connection.execute(
# """
# INSERT INTO track_compilation
# VALUES (12, 4, 3);
# """)
#
# connection.execute(
# """
# INSERT INTO track_compilation
# VALUES (13, 3, 4);
# """)
#
# connection.execute(
# """
# INSERT INTO track_compilation
# VALUES (14, 2, 7);
# """)
#
# connection.execute(
# """
# INSERT INTO track_compilation
# VALUES (15, 1, 8);
# """)

# connection.execute(
# """
# UPDATE album
#     SET year = 2018
#     WHERE id = 1 OR id = 2
# """)

# connection.execute(
# """
# UPDATE track
#     SET title = 'oh_my_god'
#     WHERE id = 5
# """)

# connection.execute(
# """
# UPDATE track
#     SET title = 'my_parrot'
#     WHERE id = 8
# """)