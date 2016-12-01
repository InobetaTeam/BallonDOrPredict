import mysql.connector

cnx = mysql.connector.connect(user='InobetaTeam', password='jScr59~5',
                              host='198.71.227.90',
                              database='medelhamdani_BallonDOr')
cursor = cnx.cursor()
query = ("SELECT * FROM medelhamdani_BallonDOr.Country;")


cursor.execute(query)

for (id, name) in cursor:
    print("{} - {}".format(id, name))
cnx.close()
