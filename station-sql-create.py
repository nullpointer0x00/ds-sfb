rf = open('', 'r')
wf = open('sql/station.sql', 'w')
insert_prefix = 'INSERT INTO `sfbike`.`station` (`station_id`, `name`, `lat`, `long`, `dockcount`, `landmark`, `installation`) VALUES ('


def formatDate(date):
    parts = date.split("/")
    if not parts[2].startswith('20'):
        parts[2] = "20" + parts[2]
    return parts[2] + "-" + parts[0] + "-" + parts[1]


def create_insert(parts):
    statement = insert_prefix + part[0] + ",'" + parts[5] + "'," + part[2] + "," + parts[3] + "," + parts[4] + ",'" + \
                parts[1] + "','" + parts[6] + "');"
    print statement
    return statement


lineParts = []
for line in rf.readlines():
    parts = line.split(",")
    lineParts.append(parts)

stations = []
for part in lineParts:
    if '' != part[0].strip():
        station = []
        station.append(part[0].strip())
        station.append(part[1].strip())
        station.append(part[2].strip())
        station.append(part[3].strip())
        station.append(part[4].strip())
        station.append(part[5].strip())
        station.append(formatDate(part[6].strip()))
        statement = create_insert(station)
        wf.write(statement + "\n")

wf.close()
