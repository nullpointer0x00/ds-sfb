from database import MySqlDataSouce
import pandas as pd

dao = MySqlDataSouce()

results = dao.fetch_all_stations();
sf_coords ="[['Lat', 'Long', 'Name'],\n"
coord_strs = []
for row in results :
    if row[1] == 'San Francisco' :
        coord_strs.append("[" + str(row[2]) +", " + str(row[3]) + ", '" +str(row[5])+ "']")
sf_coords += ",\n".join(coord_strs) + "]"
print sf_coords

df = pd.read_sql("SELECT * FROM station", con = dao.get_connection())

print df.head()