from database import MySqlDataSouce

HTML_FIRST_PART = '''
<html><head></head><body>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  <script>
      google.charts.load('current', { 'packages': ['map'] });
    google.charts.setOnLoadCallback(drawMap);

    function drawMap() {

var data = google.visualization.arrayToDataTable(
'''

HTML_SECOND_PART = '''
);
    var options = {
      showTooltip: true,
      showInfoWindow: true
    };

    var map = new google.visualization.Map(document.getElementById('chart_div'));

    map.draw(data, options);
  };
  </script>
    <div id="chart_div"></div>
    </body></head>
'''


class MapStations:
    def __init__(self):
        self.dao = MySqlDataSouce()

    def sf_locations_string(self):
        results = self.dao.fetch_all_stations();
        sf_coords = "[['Lat', 'Long', 'Name'],\n"
        coord_strs = []
        for row in results:
            if row[1] == 'San Francisco':
                coord_strs.append("[" + str(row[2]) + ", " + str(row[3]) + ", '" + str(row[5]) + "-" + str(row[0]) + "']")
        sf_coords += ",\n".join(coord_strs) + "]"
        return sf_coords

    def html(self):
        return HTML_FIRST_PART + self.sf_locations_string() + HTML_SECOND_PART