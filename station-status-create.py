# "station_id","bikes_available","docks_available","time"
# "2","18","9","9/1/2015 00:00:02"
wf = open('sql/station-status.sql', 'w')
insert_prefix = "INSERT INTO `sfbike`.`station_status` (`station_id`, `bikes_available`, `docks_available`, `time`) VALUES ("


def formatDate(date):
    parts = date.split("/")
    if not parts[2].startswith('20'):
        parts[2] = "20" + parts[2]
    return parts[2] + "-" + parts[0] + "-" + parts[1]


def clean_array(parts):
    cleaned_parts = []
    for part in parts:
        cleaned_parts.append(part.replace("\"", "").strip())
    return cleaned_parts


def tranform_line(line):
    part = clean_array(line.split(","))
    statement = ""
    if '' != part[0] and 'station_id' != part[0]:
        station = []
        station.append(part[0])
        station.append(part[1])
        station.append(part[2])
        date_split = part[3].split(" ")
        formatted_date = formatDate(date_split[0]) + " " + date_split[1]
        station.append(formatted_date)
        statement = create_insert(station)
    return statement


def create_insert(parts):
    statement = insert_prefix + parts[0] + "," + parts[1] + "," + parts[2] + ",'" + parts[3] + "');"
    return statement


with open("") as infile:
    for line in infile:
        statement = tranform_line(line)
        if "" != statement:
            wf.write(statement + "\n")
    wf.close()
