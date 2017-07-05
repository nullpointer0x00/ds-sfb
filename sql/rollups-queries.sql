CREATE TABLE `sfbike`.`sf_station_activity` SELECT
ss.station_id,
ss.bikes_available,
ss.docks_available,
ss.time,
sfs.dockcount,
sfs.name,
sfs.lat as latitude,
sfs.long as longitude,
sfs.landmark,
sfs.installation
concat(YEAR(ss.time), '-', MONTH(ss.time), '-', DAY(ss.time)) as date_str
FROM `sfbike`.`station_status` as ss
INNER JOIN `sfbike`.`station` as sfs
ON ss.station_id = sfs.station_id
WHERE  sfs.name = "San Francisco"
GROUP BY
ss.station_id,
year(ss.time),
day(ss.time),
month(ss.time),
hour(ss.time),
ss.bikes_available
order by time asc;

CREATE TABLE `sfbike`.`sf_station_activity_weather` SELECT
sfsa.*,
ws.*
FROM `sfbike`.`sf_station_activity` as sfsa
left Join `sfbike`.`weather_summary` as ws
on concat(YEAR(ws.date), '-', MONTH(ws.date), '-', DAY(ws.date)) = concat(YEAR(sfsa.time), '-', MONTH(sfsa.time), '-', DAY(sfsa.time))
order by time asc;