USE `cityfo`;
CREATE TABLE `cityfo`.`city_population` (
  `Id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `City` VARCHAR(128) NOT NULL,
  `State` VARCHAR(2) NOT NULL,
  `Population` INTEGER DEFAULT NULL,
  `Created` TIMESTAMP DEFAULT now(),
  `Updated` TIMESTAMP DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`Id`));