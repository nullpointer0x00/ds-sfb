f = open('/Users/nullpointer0x00/Downloads/babs_open_data_year_3/201608_station_data.csv', 'r')
insert_prefix =  'INSERT INTO `sfbike`.`station` (`station_id`, `name`, `lat`, `long`, `dockcount`, `landmark`, `installation`) VALUES ('

def formatDate(date) :
    parts = date.split("/")
    if not parts[2].startWith('20'):
        parts[2] = "20" + parts[2]
    return parts[2] + "-" + parts[0] + "-" + parts[1]

lineParts = []
for line in f.readlines() :
    parts = line.split(",")
    lineParts.append(parts)

stations = []
for part in lineParts :
    if '' != part[0].strip() :
        station = []
        station.append(part[0].strip())
        station.append(part[1].strip())
        station.append(part[2].strip())
        station.append(part[3].strip())
        station.append(part[4].strip())
        station.append(part[5].strip())
        station.append(formatDate(part[6].strip()))
        print station

