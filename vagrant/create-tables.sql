CREATE TABLE `station` (
  `station_id` INT NOT NULL,
  `name` VARCHAR(256) NULL,
  `lat` DECIMAL(20,6) NULL,
  `long` DECIMAL(20,6) NULL,
  `dockcount` INT NULL,
  `landmark` VARCHAR(45) NULL,
  `installation` DATE NULL,
  PRIMARY KEY (`station_id`));

  CREATE TABLE `station_status` (
  `station_id` INT NOT NULL,
  `bikes_available` INT NULL,
  `docks_available` INT NULL,
  `time` DATETIME NULL,
  PRIMARY KEY (`station_id`));
  
  CREATE TABLE `trip_data` (
  `trip_id` INT NOT NULL,
  `duration` INT NULL,
  `start_date` DATETIME NULL,
  `start_station` VARCHAR(128) NULL,
  `start_station_id` INT NULL,
  `end_date` DATETIME NULL,
  `end_station` VARCHAR(128) NULL,
  `end_station_id` INT NULL,
  `bike_id` INT NULL,
  `subscriber_type` VARCHAR(45) NULL,
  `zip_code` INT NULL,
  PRIMARY KEY (`trip_id`));


