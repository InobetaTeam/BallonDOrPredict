import mysql.connector

cnx = mysql.connector.connect(user='InobetaTeam', password='jScr59~5',
                              host='198.71.227.90',
                              database='medelhamdani_BallonDOr')
cursor = cnx.cursor()
query = ("SELECT * FROM medelhamdani_BallonDOr.Country;")

cursor.execute(query)

def test():
    idArray = []
    nameArray = []
    line = []
    for (id, name) in cursor:
        idArray.append(id)
        nameArray.append(name)
        line.append((id, name))
    return line

print test()

cursor.close()
cnx.close()
