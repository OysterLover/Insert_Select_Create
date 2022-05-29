import sqlalchemy
from pprint import pprint

db = 'postgresql://test:test@localhost:5432/test'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# добавляем еще один жанр исполнителю 4
(connection.execute(
"""
INSERT INTO genre_musician
VALUES (9, 5, 4);
"""))

# делаем так, чтобы были альбомы за 2019 и 2020 годы
(connection.execute(
"""
UPDATE album
SET year = 2020
WHERE id = 4;
"""))

# делаем так, чтобы были альбомы за 2019 и 2020 годы
(connection.execute(
"""
UPDATE album
SET year = 2019
WHERE id = 1;
"""))

# 1. количество исполнителей в каждом жанре;
pprint(connection.execute(
"""
SELECT COUNT(musician_id) FROM genre_musician
GROUP BY genre_id;
""").fetchall())


# 2. количество треков, вошедших в альбомы 2019-2020 годов;
pprint(connection.execute(
"""
SELECT COUNT(track.id) FROM track
JOIN album ON track.album_id = album.id
WHERE year = 2019 OR year = 2020;
""").fetchall())

# 3. средняя продолжительность треков по каждому альбому;
pprint(connection.execute(
"""
SELECT AVG(playing_time) FROM track
JOIN album ON track.album_id = album.id
GROUP BY album.id;
""").fetchall())

# 4. все исполнители, которые не выпустили альбомы в 2020 году;
pprint(connection.execute(
"""
SELECT pseudonym FROM musician
JOIN musician_album ON musician.id = musician_album.musician_id
JOIN album ON musician_album.album_id = album.id
WHERE year != 2020;
""").fetchall())

# 5. названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
pprint(connection.execute(
"""
SELECT c.title FROM compilation c
JOIN track_compilation tc ON c.id = tc.compilation_id
JOIN track t ON tc.track_id = t.id
JOIN album a ON t.album_id = a.id
JOIN musician_album ma ON a.id = ma.album_id
JOIN musician m ON ma.musician_id = m.id
WHERE m.pseudonym = 'Zaz';
""").fetchall())

# 6. название альбомов, в которых присутствуют исполнители более 1 жанра;
pprint(connection.execute(
"""
SELECT DISTINCT a.title FROM album a
JOIN musician_album ma ON a.id = ma.album_id
JOIN musician m ON ma.musician_id = m.id
JOIN genre_musician gm ON m.id = gm.musician_id
WHERE gm.musician_id = (
	SELECT gm.musician_id FROM musician m
	JOIN genre_musician gm ON m.id = gm.musician_id
	GROUP BY gm.musician_id
	HAVING COUNT(gm.genre_id) > 1 );
""").fetchall())

# 7. наименование треков, которые не входят в сборники;
pprint(connection.execute(
"""
SELECT t.title  FROM track t
JOIN track_compilation tc ON t.id = tc.track_id
WHERE tc.track_id = (
	SELECT tc.track_id FROM track t
	JOIN track_compilation tc ON t.id = tc.track_id
	GROUP BY tc.track_id
	HAVING COUNT(tc.compilation_id) = 0);
""").fetchall())

# 8. исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
pprint(connection.execute(
"""
SELECT m.pseudonym  FROM musician m
JOIN musician_album ma ON m.id = ma.musician_id
JOIN album a ON ma.album_id = a.id
JOIN track t ON a.id = t.album_id
WHERE t.playing_time = (
	SELECT MIN(t.playing_time) FROM track t);
""").fetchall())

# 9. название альбомов, содержащих наименьшее количество треков.
pprint(connection.execute(
"""
SELECT a.title, COUNT(t.id) count FROM album a 
JOIN track t ON a.id = t.album_id
GROUP BY a.id
ORDER BY count ASC
LIMIT 1;
""").fetchall())