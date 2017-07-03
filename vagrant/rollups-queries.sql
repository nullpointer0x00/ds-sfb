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