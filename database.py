import pymysql
from datetime import date, datetime, timedelta

from pymysql import MySQLError


class MySqlDataSouce:
    def __init__(self):
        self.config = {
            'user': 'cityfo',
            'password': 'cityfo',
            'host': '127.0.0.1',
            'port': 3406,
            'database': 'cityfo',
            'charset': 'utf8mb4'
        }
        self.cnx = pymysql.connect(**self.config)

    def __del__(self):
        try:
            self.cnx.close()
        except Exception as e:
            print("Error closing MySql connection: ", e)
            pass

