-- MySQL dump 10.13  Distrib 8.0.18, for Linux (x86_64)
--
-- Host: localhost    Database: team70
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company` (
  `comname` varchar(45) NOT NULL,
  PRIMARY KEY (`comname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES ('4400 Theater Company'),('AI Theater Company'),('Awesome Theater Company'),('EZ Theater Company');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customercreditcard`
--

DROP TABLE IF EXISTS `customercreditcard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customercreditcard` (
  `username` varchar(45) DEFAULT NULL,
  `creditcardnum` varchar(16) NOT NULL,
  PRIMARY KEY (`creditcardnum`),
  KEY `cred_username_idx` (`username`),
  CONSTRAINT `cred_username` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customercreditcard`
--

LOCK TABLES `customercreditcard` WRITE;
/*!40000 ALTER TABLE `customercreditcard` DISABLE KEYS */;
INSERT INTO `customercreditcard` VALUES ('calcultron','1111111111000000'),('calcultron2','1111111100000000'),('calcultron2','1111111110000000'),('calcwizard','1111111111100000'),('cool_class4400','2222222222000000'),('DNAhelix','2220000000000000'),('does2Much','2222222200000000'),('eeqmcsquare','2222222222222200'),('entropyRox','2222222222200000'),('entropyRox','2222222222220000'),('fullMetal','1100000000000000'),('georgep','1111111111110000'),('georgep','1111111111111000'),('georgep','1111111111111100'),('georgep','1111111111111110'),('georgep','1111111111111111'),('ilikemoney$$','2222222222222220'),('ilikemoney$$','2222222222222222'),('ilikemoney$$','9000000000000000'),('imready','1111110000000000'),('isthisthekrustykrab','1110000000000000'),('isthisthekrustykrab','1111000000000000'),('isthisthekrustykrab','1111100000000000'),('newCustomer','1234567898012381'),('newCustomer','9989898989898989'),('newUsername','5555555555888888'),('newUsername','9898979465416431'),('notFullMetal','1000000000000000'),('programerAAL','2222222000000000'),('RitzLover28','3333333333333300'),('testCustomer','9999999999998888'),('testManagerCustomer','6666666666666666'),('testManagerCustomer','7777777777777777'),('testManagerCustomer','8888888888888888'),('testManagerCustomer','9999888888888888'),('thePiGuy3.14','2222222220000000'),('theScienceGuy','2222222222222000');
/*!40000 ALTER TABLE `customercreditcard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customerviewmovie`
--

DROP TABLE IF EXISTS `customerviewmovie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customerviewmovie` (
  `movname` varchar(45) NOT NULL,
  `movreleasedate` date NOT NULL,
  `movplaydate` date NOT NULL,
  `thname` varchar(45) NOT NULL,
  `comname` varchar(45) NOT NULL,
  `creditcardnum` varchar(16) NOT NULL,
  PRIMARY KEY (`movname`,`movreleasedate`,`movplaydate`,`comname`,`thname`,`creditcardnum`),
  KEY `cus_thname_idx` (`thname`),
  KEY `cus_comname_idx` (`comname`),
  KEY `cus_creditcardnum_idx` (`creditcardnum`),
  CONSTRAINT `cus_comname` FOREIGN KEY (`comname`) REFERENCES `theater` (`comname`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `cus_creditcardnum` FOREIGN KEY (`creditcardnum`) REFERENCES `customercreditcard` (`creditcardnum`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `cus_movname` FOREIGN KEY (`movname`, `movreleasedate`) REFERENCES `movie` (`movname`, `movreleasedate`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `cus_thname` FOREIGN KEY (`thname`) REFERENCES `theater` (`thname`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customerviewmovie`
--

LOCK TABLES `customerviewmovie` WRITE;
/*!40000 ALTER TABLE `customerviewmovie` DISABLE KEYS */;
INSERT INTO `customerviewmovie` VALUES ('How to Train Your Dragon','2010-03-21','2010-03-25','Star Movies','EZ Theater Company','1111111111111100'),('How to Train Your Dragon','2010-03-21','2010-03-22','Main Movies','EZ Theater Company','1111111111111111'),('How to Train Your Dragon','2010-03-21','2010-03-23','Main Movies','EZ Theater Company','1111111111111111'),('How to Train Your Dragon','2010-03-21','2010-04-02','Cinema Star','4400 Theater Company','1111111111111111'),('How to Train Your Dragon','2010-03-21','2010-03-23','Main Movies','EZ Theater Company','6666666666666666'),('The King\'s Speech','2010-11-26','2019-12-20','Main Movies','EZ Theater Company','6666666666666666'),('The King\'s Speech','2010-11-26','2019-12-20','Main Movies','EZ Theater Company','7777777777777777'),('4400 The Movie','2019-08-12','2019-08-12','Star Movies','EZ Theater Company','9898979465416431'),('How to Train Your Dragon','2010-03-21','2010-03-25','Star Movies','EZ Theater Company','9898979465416431'),('Spaceballs','1987-06-24','1999-06-24','Main Movies','EZ Theater Company','9999888888888888');
/*!40000 ALTER TABLE `customerviewmovie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `username` varchar(45) NOT NULL,
  `manstreet` varchar(45) DEFAULT NULL,
  `mancity` varchar(45) DEFAULT NULL,
  `manstate` varchar(2) DEFAULT NULL,
  `manzipcode` int(5) DEFAULT NULL,
  `employeetype` varchar(45) DEFAULT NULL,
  `comname` varchar(45) DEFAULT NULL,
  `thname` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`username`),
  KEY `emp_company_idx` (`comname`),
  KEY `emp_thname_idx` (`thname`),
  CONSTRAINT `emp_comname` FOREIGN KEY (`comname`) REFERENCES `company` (`comname`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `emp_thname` FOREIGN KEY (`thname`) REFERENCES `theater` (`thname`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `emp_username` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('calcultron','123 Peachtree St','Atlanta','GA',30308,'Manager','EZ Theater Company','Star Movies'),('cool_class4400',NULL,NULL,NULL,NULL,'Admin',NULL,NULL),('entropyRox','200 Cool Place','San Francisco','CA',94016,'Manager','4400 Theater Company','Cinema Star'),('fatherAI','456 Main St','New York','NY',10001,'Manager','EZ Theater Company','Main Movies'),('georgep','10 Pearl Dr','Seattle','WA',98105,'Manager','4400 Theater Company','Jonathan\'s Movies'),('ghcghc','100 Pi St','Pallet Town','KS',31415,'Manager','AI Theater Company','ML Movies'),('imbatman','800 Color Dr','Austin','TX',78653,'Manager','Awesome Theater Company','ABC Theater'),('manager1','123 Ferst Drive','Atlanta','GA',30332,'Manager','4400 Theater Company',NULL),('manager2','456 Ferst Drive','Atlanta','GA',30332,'Manager','AI Theater Company','NewTheaterTest'),('manager3','789 Ferst Drive','Atlanta','GA',30332,'Manager','4400 Theater Company','balsdkfjfa;sldfk'),('manager4','000 Ferst Drive','Atlanta','GA',30332,'Manager','4400 Theater Company','asdfas'),('manageUser3','200 Cool Place','San Francisco','CA',94016,'Manager','4400 Theater Company','NULL'),('radioactivePoRa','100 Blu St','Sunnyvale','CA',94088,'Manager','4400 Theater Company','Star Movies'),('testManager','Manger Street','Manager City','GA',37332,'Manager','4400 Theater Company','NULL'),('testManager2','200 Cool Place','San Francisco','CA',94016,'Manager','4400 Theater Company','NULL'),('testManagerCustomer','Manager Customer Street','Manager Customer City','GA',37332,'Manager','4400 Theater Company','NULL');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie` (
  `movname` varchar(45) NOT NULL,
  `movreleasedate` date NOT NULL,
  `duration` int(11) DEFAULT NULL,
  PRIMARY KEY (`movname`,`movreleasedate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie`
--

LOCK TABLES `movie` WRITE;
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` VALUES ('4400 The Movie','2019-08-12',130),('Avengers: Endgame','2019-04-26',181),('Calculus Returns: A ML Story','2019-09-19',314),('George P Burdell\'s Life Story','1927-08-12',100),('Georgia Tech The Movie','1985-08-13',100),('How to Train Your Dragon','2010-03-21',98),('Spaceballs','1987-06-24',96),('Spider-Man: Into the Spider-Verse','2018-12-01',117),('testMovie','2019-12-01',120),('testMovie','2019-12-02',120),('testMovie2','2019-12-01',120),('The First Pokemon Movie','1998-07-19',75),('The King\'s Speech','2010-11-26',119);
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movieplay`
--

DROP TABLE IF EXISTS `movieplay`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movieplay` (
  `movname` varchar(45) NOT NULL,
  `movreleasedate` date NOT NULL,
  `movplaydate` date NOT NULL,
  `thname` varchar(45) NOT NULL,
  `comname` varchar(45) NOT NULL,
  PRIMARY KEY (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`),
  KEY `play_theater_idx` (`thname`,`comname`),
  KEY `view_playdate_idx` (`movplaydate`),
  CONSTRAINT `play_movie` FOREIGN KEY (`movname`, `movreleasedate`) REFERENCES `movie` (`movname`, `movreleasedate`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `play_theater` FOREIGN KEY (`thname`, `comname`) REFERENCES `theater` (`thname`, `comname`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movieplay`
--

LOCK TABLES `movieplay` WRITE;
/*!40000 ALTER TABLE `movieplay` DISABLE KEYS */;
INSERT INTO `movieplay` VALUES ('Georgia Tech The Movie','1985-08-13','1985-08-13','ABC Theater','Awesome Theater Company'),('Spaceballs','1987-06-24','1999-06-24','Main Movies','EZ Theater Company'),('Spaceballs','1987-06-24','2000-02-02','Cinema Star','4400 Theater Company'),('How to Train Your Dragon','2010-03-21','2010-03-22','Main Movies','EZ Theater Company'),('How to Train Your Dragon','2010-03-21','2010-03-23','Main Movies','EZ Theater Company'),('How to Train Your Dragon','2010-03-21','2010-03-25','Star Movies','EZ Theater Company'),('How to Train Your Dragon','2010-03-21','2010-04-02','Cinema Star','4400 Theater Company'),('Spaceballs','1987-06-24','2010-04-02','ML Movies','AI Theater Company'),('George P Burdell\'s Life Story','1927-08-12','2010-05-20','Cinema Star','4400 Theater Company'),('The First Pokemon Movie','1998-07-19','2018-07-19','ABC Theater','Awesome Theater Company'),('George P Burdell\'s Life Story','1927-08-12','2019-07-14','Main Movies','EZ Theater Company'),('4400 The Movie','2019-08-12','2019-08-12','Star Movies','EZ Theater Company'),('4400 The Movie','2019-08-12','2019-09-12','Cinema Star','4400 Theater Company'),('Georgia Tech The Movie','1985-08-13','2019-09-30','Cinema Star','4400 Theater Company'),('Spider-Man: Into the Spider-Verse','2018-12-01','2019-09-30','ML Movies','AI Theater Company'),('Calculus Returns: A ML Story','2019-09-19','2019-10-10','ML Movies','AI Theater Company'),('4400 The Movie','2019-08-12','2019-10-12','ABC Theater','Awesome Theater Company'),('George P Burdell\'s Life Story','1927-08-12','2019-10-22','Main Movies','EZ Theater Company'),('4400 The Movie','2019-08-12','2019-12-06','Cinema Star','4400 Theater Company'),('The King\'s Speech','2010-11-26','2019-12-20','Cinema Star','4400 Theater Company'),('The King\'s Speech','2010-11-26','2019-12-20','Main Movies','EZ Theater Company'),('Calculus Returns: A ML Story','2019-09-19','2019-12-30','ML Movies','AI Theater Company'),('The First Pokemon Movie','1998-07-19','2020-02-20','Cinema Star','4400 Theater Company'),('Spaceballs','1987-06-24','2023-01-23','ML Movies','AI Theater Company'),('Avengers: Endgame','2019-04-26','2045-12-07','Cinema Star','4400 Theater Company');
/*!40000 ALTER TABLE `movieplay` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `theater`
--

DROP TABLE IF EXISTS `theater`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `theater` (
  `comname` varchar(45) NOT NULL,
  `thname` varchar(45) NOT NULL,
  `capacity` int(11) DEFAULT NULL,
  `thstreet` varchar(45) DEFAULT NULL,
  `thcity` varchar(45) DEFAULT NULL,
  `thstate` varchar(2) DEFAULT NULL,
  `thzipcode` int(5) DEFAULT NULL,
  PRIMARY KEY (`comname`,`thname`),
  KEY `emp_thname` (`thname`),
  CONSTRAINT `th_comname` FOREIGN KEY (`comname`) REFERENCES `company` (`comname`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `theater`
--

LOCK TABLES `theater` WRITE;
/*!40000 ALTER TABLE `theater` DISABLE KEYS */;
INSERT INTO `theater` VALUES ('4400 Theater Company','asdfas',123,'afdsasdf','asdfasdf','AZ',12312),('4400 Theater Company','balsdkfjfa;sldfk',12,'alsdkjfa;l','sadlkfjas','AL',12312),('4400 Theater Company','Cinema Star',4,'100 Cool Place','San Francisco','CA',94016),('4400 Theater Company','Jonathan\'s Movies',2,'67 Pearl Dr','Seattle','WA',98101),('4400 Theater Company','Star Movies',5,'4400 Rocks Ave','Boulder','CA',80301),('AI Theater Company','ML Movies',3,'314 Pi St','Pallet Town','KS',31415),('AI Theater Company','NewTheaterTest',100,'TheaterAddress','TheaterCity','GA',30022),('Awesome Theater Company','ABC Theater',5,'880 Color Dr','Austin','TX',73301),('EZ Theater Company','Main Movies',3,'123 Main St','New York','NY',10001),('EZ Theater Company','Star Movies',2,'745 GT St','Atlanta','GA',30332);
/*!40000 ALTER TABLE `theater` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `username` varchar(45) NOT NULL,
  `firstname` varchar(45) DEFAULT NULL,
  `lastname` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `usertype` varchar(45) DEFAULT NULL,
  `status` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('asdfasdf','asdf','asdf','3dbe00a167653a1aaee01d93e77e730e','Employee','Approved'),('calcultron','Dwight','Schrute','77c9749b451ab8c713c48037ddfbb2c4','Employee, Customer','Approved'),('calcultron2','Jim','Halpert','8792b8cf71d27dc96173b2ac79b96e0d','Customer','Approved'),('calcwizard','Issac','Newton','0d777e9e30b918e9034ab610712c90cf','Customer','Approved'),('clarinetbeast','Squidward','Tentacles','c8c605999f3d8352d7bb792cf3fdb25b','Customer','Approved'),('cool_class4400','A. TA','Washere','77c9749b451ab8c713c48037ddfbb2c4','Employee, Customer','Approved'),('DNAhelix','Rosalind','Franklin','ca94efe2a58c27168edf3d35102dbb6d','Customer','Approved'),('does2Much','Carl','Gauss','00cedcf91beffa9ee69f6cfe23a4602d','Customer','Approved'),('eeqmcsquare','Albert','Einstein','7c5858f7fcf63ec268f42565be3abb95','Customer','Approved'),('entropyRox','Claude','Shannon','c8c605999f3d8352d7bb792cf3fdb25b','Employee, Customer','Approved'),('fatherAI','Alan','Turing','0d777e9e30b918e9034ab610712c90cf','Employee','Approved'),('fullMetal','Edward','Elric','d009d70ae4164e8989725e828db8c7c2','Customer','Approved'),('gdanger','Gary','Danger','3665a76e271ada5a75368b99f774e404','User','Declined'),('georgep','George P.','Burdell','bbb8aae57c104cda40c93843ad5e6db8','Employee, Customer','Approved'),('ghcghc','Grace','Hopper','9f0863dd5f0256b0f586a7b523f8cfe8','Employee','Approved'),('ilikemoney$$','Eugene','Krabs','7c5858f7fcf63ec268f42565be3abb95','Customer','Approved'),('imbatman','Bruce','Wayne','9f0863dd5f0256b0f586a7b523f8cfe8','Employee','Approved'),('imready','Spongebob','Squarepants','ca94efe2a58c27168edf3d35102dbb6d','Customer','Approved'),('isthisthekrustykrab','Patrick','Star','134fb0bf3bdd54ee9098f4cbc4351b9a','Customer','Approved'),('manager1','Manager','One','e58cce4fab03d2aea056398750dee16b','Employee','Approved'),('manager2','Manager','Two','ba9485f02fc98cdbd2edadb0aa8f6390','Employee','Approved'),('manager3','Three','Three','6e4fb18b49aa3219bef65195dac7be8c','Employee','Approved'),('manager4','Four','Four','d61dfee83aa2a6f9e32f268d60e789f5','Employee','Approved'),('manageUser3','test','manager','3665a76e271ada5a75368b99f774e404','Employee','Approved'),('newCustomer','FirstName','LastName','5f4dcc3b5aa765d61d8327deb882cf99','Customer','Pending'),('newUsername','qwerty','berty','5f4dcc3b5aa765d61d8327deb882cf99','Customer','Pending'),('notFullMetal','Alphonse','Elric','d009d70ae4164e8989725e828db8c7c2','Customer','Approved'),('programerAAL','Ada','Lovelace','ba9485f02fc98cdbd2edadb0aa8f6390','Customer','Approved'),('radioactivePoRa','Marie','Curie','e5d4b739db1226088177e6f8b70c3a6f','Employee','Approved'),('RitzLover28','Abby','Normal','8792b8cf71d27dc96173b2ac79b96e0d','Customer','Approved'),('smith_j','John','Smith','77c9749b451ab8c713c48037ddfbb2c4','User','Approved'),('testCustomer','Test','Customer','3665a76e271ada5a75368b99f774e404','Customer','Declined'),('testManager','Test','Manager','3665a76e271ada5a75368b99f774e404','Employee','Approved'),('testManager2','test','Manager','3665a76e271ada5a75368b99f774e404','Employee','Approved'),('testManagerCustomer','Test','ManagerCustomer','3665a76e271ada5a75368b99f774e404','Employee, Customer','Approved'),('testUser','Test','User','3665a76e271ada5a75368b99f774e404','User','Declined'),('texasStarKarate','Sandy','Cheeks','7c5858f7fcf63ec268f42565be3abb95','User','Declined'),('thePiGuy3.14','Archimedes','Syracuse','e11170b8cbd2d74102651cb967fa28e5','Customer','Approved'),('theScienceGuy','Bill','Nye','c8c605999f3d8352d7bb792cf3fdb25b','Customer','Approved');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uservisittheater`
--

DROP TABLE IF EXISTS `uservisittheater`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uservisittheater` (
  `username` varchar(45) DEFAULT NULL,
  `thname` varchar(45) DEFAULT NULL,
  `comname` varchar(45) DEFAULT NULL,
  `visitdate` date DEFAULT NULL,
  `visitid` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`visitid`),
  KEY `visit_comname_idx` (`comname`),
  KEY `visit_thname_idx` (`thname`),
  KEY `visit_username_idx` (`username`),
  CONSTRAINT `visit_comname` FOREIGN KEY (`comname`) REFERENCES `theater` (`comname`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `visit_thname` FOREIGN KEY (`thname`) REFERENCES `theater` (`thname`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `visit_username` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uservisittheater`
--

LOCK TABLES `uservisittheater` WRITE;
/*!40000 ALTER TABLE `uservisittheater` DISABLE KEYS */;
INSERT INTO `uservisittheater` VALUES ('georgep','Main Movies','EZ Theater Company','2010-03-22',1),('calcwizard','Main Movies','EZ Theater Company','2010-03-22',2),('calcwizard','Star Movies','EZ Theater Company','2010-03-25',3),('imready','Star Movies','EZ Theater Company','2010-03-25',4),('newUsername','Star Movies','4400 Theater Company','2019-12-26',23),('cool_class4400','Star Movies','EZ Theater Company','2019-12-31',24),('testManagerCustomer','NewTheaterTest','AI Theater Company','2019-12-02',25);
/*!40000 ALTER TABLE `uservisittheater` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-02 12:11:50
