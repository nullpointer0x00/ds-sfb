import pymysql


class MySqlDataSouce:
    def __init__(self):
        self.config = {
            'user': 'sfbike',
            'password': 'sfbikepass',
            'host': '127.0.0.1',
            'port': 3406,
            'database': 'sfbike',
            'charset': 'utf8mb4'
        }
        self.cnx = pymysql.connect(**self.config)

    def get_connection(self):
        return self.cnx

    def fetch_all_stations(self):
        cursor = self.cnx.cursor()
        query = ("SELECT * FROM station")
        cursor.execute(query)
        return cursor.fetchall()

    def insert_into_strava_activity(self, id, athlete_id, name, distance, kilojoules, moving_time, elapsed_time, total_elevation_gain, elev_high, elev_low, type, start_date, start_date_local, timezone, athlete_count, workout_type,average_speed,max_speed,location_city, location_state,location_country):
        query = ("INSERT INTO `strava_activity` "
                 "(`id`, `athlete_id`, `name`, `distance`, `kilojoules`, "
                 "`moving_time`, `elapsed_time`, "
                 "`total_elevation_gain`, `elev_high`, `elev_low`,"
                 "`type`,`start_date`,`start_date_local`,`timezone`,"
                 "`utc_offset`,`start_latitude`,`start_longitude`,`achievement_count`,`workout_type`,`average_speed`,`max_speed`,"
                 "`location_city`,`location_state`, `location_country`) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data = (id, athlete_id, name, distance, kilojoules, moving_time, elapsed_time, total_elevation_gain, elev_high, elev_low, type, start_date, start_date_local, timezone, athlete_count, workout_type,average_speed,max_speed,location_city, location_state,location_country)
        return self.insert_record(query, data)

    def __del__(self):
        try:
            self.cnx.close()
        except Exception as e:
            print("Error closing MySql connection: ", e)
            pass
