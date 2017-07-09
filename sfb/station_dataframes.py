from database import MySqlDataSouce
import pandas as pd

class StationDataframes:
    FIND_BY_ID_STATION_STATUS = '''
    SELECT ss.station_id, ss.bikes_available, ss.docks_available, ss.time
    FROM `sfbike`.`station_status` ss
    where ss.station_id in (#)
    GROUP BY ss.station_id, year(ss.time), day(ss.time), month(ss.time), hour(ss.time), ss.bikes_available
    order by time asc;
    '''

    FETCH_ALL_STATION_ACTIVITY_WEATHER = '''
    SELECT * FROM sfbike.sf_station_activity_weather where station_id in (#) order by time desc;'''

    def __init__(self):
        self.dao = MySqlDataSouce()

    def get_station_activity_weather(self, station_ids):
        query = self.FETCH_ALL_STATION_ACTIVITY_WEATHER.replace('#', str(station_ids))
        return pd.read_sql(query, con=self.dao.get_connection())
