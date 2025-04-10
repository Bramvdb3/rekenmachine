import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

handle = open('tracks.csv')

# Example data format in CSV:
# Another One Bites The Dust,Queen,Greatest Hits,Rock,55,100,217103
#   0                          1      2           3    4   5   6

for line in handle:
    line = line.strip()
    pieces = line.split(',')
    
    # Debugging: print the pieces
    print(pieces)

    if len(pieces) < 7:
        continue

    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    genre = pieces[3]
    count = pieces[4]
    rating = pieces[5]
    length = pieces[6]

    # Debugging: print each parsed field
    print(f"Track: {name}, Artist: {artist}, Album: {album}, Genre: {genre}, Count: {count}, Rating: {rating}, Length: {length}")

    # Ensure count, rating, and length are integers
    try:
        count = int(count)
        rating = int(rating)
        length = int(length)
    except ValueError as e:
        print(f"Error converting count, rating, or length to int: {e}")
        continue

    # Insert Artist and get artist_id
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = cur.fetchone()[0]

    # Insert Genre and get genre_id
    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = cur.fetchone()[0]

    # Insert Album and get album_id
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = cur.fetchone()[0]

    # Insert Track
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        (name, album_id, genre_id, length, rating, count))

    conn.commit()

# Execute the query to get the expected results
cur.execute('''
SELECT Track.title, Artist.name, Album.title, Genre.name 
FROM Track 
JOIN Genre ON Track.genre_id = Genre.id
JOIN Album ON Track.album_id = Album.id
JOIN Artist ON Album.artist_id = Artist.id
ORDER BY Artist.name LIMIT 3;
''')

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()