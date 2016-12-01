import sqlite3

cnx = sqlite3.connect('chinook.db')

cursor = cnx.cursor()
query = ("SELECT * FROM albums")

cursor.execute(query)

def test():
    idArray = []
    nameArray = []
    line = []
    for (albumid, title, artistid) in cursor:
        idArray.append(title)
        nameArray.append(artistid)
        line.append((title, artistid))
    return line

print test()

cursor.close()
cnx.close()