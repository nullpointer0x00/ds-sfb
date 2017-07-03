# Trip ID,Duration,Start Date,Start Station,Start Terminal,End Date,End Station,End Terminal,Bike #,Subscriber Type,Zip Code
# 913465,746,9/1/2015 0:10,San Francisco Caltrain 2 (330 Townsend),69,9/1/2015 0:23,San Francisco City Hall,58,238,Subscriber,94107
wf = open('vagrant/trips.sql', 'w')
insert_prefix = "INSERT INTO `sfbike`.`trip` (`trip_id`, `duration`, `start_date`, `start_station`, `start_station_id`, "
insert_prefix += "`end_date`, `end_station`, `end_station_id`, `bike_id`, `subscriber_type`, `zip_code`) VALUES ("

def formatDate(date) :
    parts = date.split("/")
    if not parts[2].startswith('20'):
        parts[2] = "20" + parts[2]
    return parts[2] + "-" + parts[0] + "-" + parts[1]

def timeFormat(time):
    parts = time.split(":")
    if len(parts[0]) == 1:
        parts[0] = "0" + parts[0]
    return parts[0] + ":" + parts[1] + ":00"

def clean_array(parts) :
    cleaned_parts = []
    for part in parts:
        cleaned_parts.append(part.replace("\"", "").strip())
    return cleaned_parts

def tranform_line(line) :
    part = clean_array(line.split(","))
    statement = ""
    if '' != part[0] and 'Trip ID' != part[0] :
        date_split = part[2].split(" ")

        formatted_date = formatDate(date_split[0]) + " " + timeFormat(date_split[1])
        part[2] = formatted_date

        date_split = part[5].split(" ")
        formatted_date = formatDate(date_split[0]) + " " + timeFormat(date_split[1])
        part[5] = formatted_date

        statement = create_insert(part)
    return statement

def create_insert(parts) :
    if parts[10]  == "nil" :
        parts[10] == 'NULL'
    statement = insert_prefix + parts[0] + "," + parts[1] + ",'" + parts[2] + "','" + parts[3] + "'," + parts[4] + ",'";
    statement += parts[5] + "','" + parts[6] + "'," + parts[7] + "," + parts[8] + ",'" + parts[9] + "'," + parts[10] + ");";
    return statement

with open("") as infile:
    for line in infile:
        statement = tranform_line(line)
        if "" != statement :
            wf.write(statement + "\n")
    wf.close()

