import datetime
from datetime import timedelta
import requests

class WunderGroundApi :

    def get_api_key(self) :
        with open('api-key.txt', 'r') as f:
            api_key = f.readline()
        return api_key.strip()

    def get_date_str(self, date) :
        # if not isinstance(date, type(dt.date)) :
        #     return ""
        return date.strftime("%Y%m%d")

    def get_history(self, api_key, date) :
        url = "http://api.wunderground.com/api/" + api_key + "/history_"
        url += self.get_date_str(date) + '/q/CA/San_Francisco.json'
        print "calling url: " + url
        return requests.get(url)


    def execute_history_cache(self, date, range):
        api_key = self.get_api_key()
        for i in range(0, range):
            json_response = self.get_history(api_key, date)
            if json_response.status_code == 200:
                text = json_response.text
                file_name = "wunder_cache/history_" + self.get_date_str(date) + ".json"
                print "response text: " + text
                print "writing file: " + file_name
                json_file = open(file_name, "w")
                json_file.write(text)
                json_file.close()
            date = date + timedelta(days=1)

    def read_cached_files(self):
        return []

    def create_insert(parts):
        return "todo"

    def execute_history_cache_to_sql(self):
        print "todo"

def main():
    date = datetime.date(2015, 9, 3)
    wg = WunderGroundApi()
    # wg.execute_history_cache(date, 365)
    wg.execute_history_cache_to_sql()

if __name__ == "__main__": main()
