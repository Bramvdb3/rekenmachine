import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Drop the Counts table if it exists
cur.execute('DROP TABLE IF EXISTS Counts')

# Create the Counts table with org as the primary key
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# Get the file name from the user
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'

# Open the file
fh = open(fname)
for line in fh:
    # Look for lines that start with 'From: '
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    # Extract the domain name from the email address
    org = email.split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))

# Move the commit operation outside the loop for better performance
conn.commit()

# Select the top 10 organizations by count
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

# Print the results
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Close the cursor
cur.close()