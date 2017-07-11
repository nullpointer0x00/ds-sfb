import pymysql


class MySqlDataSource:
    def __init__(self):
        self.config = {
            'user': 'sfbike',
            'password': 'sfbikepass',
            'host': '127.0.0.1',
            'port': 3406,
            'database': 'mushrooms',
            'charset': 'utf8mb4'
        }
        self.cnx = pymysql.connect(**self.config)

    def get_connection(self):
        return self.cnx

    def __del__(self):
        try:
            self.cnx.close()
        except Exception as e:
            print("Error closing MySql connection: ", e)
            pass
