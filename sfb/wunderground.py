import datetime
from datetime import timedelta
import requests
import json
from os import listdir
from os.path import isfile, join

WEATHER_SUMMARY_INSERT_PREFIX = '''
INSERT INTO `sfbike`.`weather_summary`
(`date`,
`region`,
`fog`,
`rain`,
`snow`,
`snowfallm`,
`snowfalli`,
`snowdepthm`,
`snowdepthi`,
`hail`,
`thunder`,
`tornado`,
`meantempm`,
`meantempi`,
`meandewptm`,
`meandewpti`,
`meanpressurem`,
`meanpressurei`,
`meanwindspdm`,
`meanwindspdi`,
`meanwdire`,
`meanwdird`,
`meanvism`,
`meanvisi`,
`humidity`,
`maxtempm`,
`maxtempi`,
`mintempm`,
`mintempi`,
`maxhumidity`,
`minhumidity`,
`maxdewptm`,
`maxdewpti`,
`mindewptm`,
`mindewpti`,
`maxpressurem`,
`maxpressurei`,
`minpressurem`,
`minpressurei`,
`maxwspdm`,
`maxwspdi`,
`minwspdm`,
`minwspdi`,
`maxvism`,
`maxvisi`,
`minvism`,
`minvisi`,
`gdegreedays`,
`heatingdegreedays`,
`coolingdegreedays`,
`precipm`,
`precipi`) VALUES'''


class WunderGroundApi:
    def get_api_key(self):
        with open('api-key.txt', 'r') as f:
            api_key = f.readline()
        return api_key.strip()

    def get_date_str(self, date):
        # if not isinstance(date, type(dt.date)) :
        #     return ""
        return date.strftime("%Y%m%d")

    def get_history(self, api_key, date):
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

    def read_cached_files(self, path):
        cache_files = [f for f in listdir(path) if isfile(join(path, f))]
        json_objects = []
        for file_name in cache_files:
            file = open(join(path, file_name), "r")
            json_str = ""
            for line in file.readlines():
                json_str += line
            json_objects.append(json.loads(json_str))
        return json_objects

    def create_insert(self, json_object):
        statement = WEATHER_SUMMARY_INSERT_PREFIX.strip().replace("\n", " ")
        statement += " ( '" + self.parse_date(json_object) + "','San Francisco', " + self.parse_daily_summary(
            json_object) + ");\n"
        return statement

    def execute_history_cache_to_sql(self):
        wf = open('sql/weather_summary.sql', 'w')
        json_objects = self.read_cached_files("wunder_cache")
        for json_object in json_objects:
            statement = self.create_insert(json_object)
            wf.write(statement)
        wf.close()

    def parse_date(self, json_obj):
        return json_obj["history"]["date"]["year"] + "-" + json_obj["history"]["date"]["mon"] + "-" + \
               json_obj["history"]["date"]["mday"]

    def parse_daily_summary(self, json_obj):
        daily_summary = json_obj["history"]["dailysummary"][0]
        insert_values = "" + self.assure_int_not_empty(daily_summary["fog"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["rain"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["snow"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["snowfallm"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["snowfalli"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["snowdepthm"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["snowdepthi"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["hail"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["thunder"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["tornado"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["meantempm"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["meantempi"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["meandewptm"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["meandewpti"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["meanpressurem"])
        insert_values += "," + self.assure_decimal_not_empty(daily_summary["meanpressurei"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["meanwindspdm"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["meanwindspdi"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["meanwdire"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["meanwdird"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["meanvism"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["meanvisi"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["humidity"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["maxtempm"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["maxtempi"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["mintempm"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["mintempi"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["maxhumidity"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["minhumidity"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["maxdewptm"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["maxdewpti"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["mindewptm"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["mindewpti"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["maxpressurem"])
        insert_values += "," + self.assure_decimal_not_empty(daily_summary["maxpressurei"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["minpressurem"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["minpressurei"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["maxwspdm"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["maxwspdi"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["minwspdm"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["minwspdi"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["maxvism"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["maxvisi"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["minvism"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["minvisi"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["gdegreedays"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["heatingdegreedays"])
        insert_values += "," + self.assure_int_not_empty(daily_summary["coolingdegreedays"])
        insert_values += "," + self.assure_decimal_not_empty(daily_summary["precipm"])  # sometimes equals T ???
        insert_values += "," + self.assure_decimal_not_empty(daily_summary["precipi"])  # sometimes equals T ???
        return insert_values

    def assure_decimal_not_empty(self, d):
        d = d.strip()
        if "" == d or d == "T":
            return "0.0"
        return d

    def assure_int_not_empty(self, int):
        int = int.strip()
        if "" == int:
            return "0"
        return int


def main():
    date = datetime.date(2015, 9, 3)
    wg = WunderGroundApi()
    # wg.execute_history_cache(date, 365)
    wg.execute_history_cache_to_sql()


if __name__ == "__main__": main()
