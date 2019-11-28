DROP DATABASE IF EXISTS team70;

#team70 Schema Creation
CREATE SCHEMA `team70` ;

#Users
CREATE TABLE `team70`.`users` (
  `username` VARCHAR(45) NOT NULL,
  `firstname` VARCHAR(45) NULL,
  `lastname` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  `usertype` VARCHAR(45) NULL,
  `status` VARCHAR(8) NULL,
  PRIMARY KEY (`username`));


#Company:
CREATE TABLE `team70`.`company` (
  `comname` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`comname`));


#Movie:
CREATE TABLE `team70`.`movie` (
  `movname` VARCHAR(45) NOT NULL,
  `movreleasedate` DATE NULL,
  `duration` INT NULL,
  PRIMARY KEY (`movname`),
  INDEX `movie_idx` (`movname` ASC, `movreleasedate` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


#CustomerCreditcard
CREATE TABLE `team70`.`customercreditcard` (
  `username` VARCHAR(45) NULL,
  `creditcardnum` VARCHAR(16) NOT NULL,
  PRIMARY KEY (`creditcardnum`),
  INDEX `cred_username_idx` (`username` ASC) VISIBLE,
  CONSTRAINT `cred_username`
    FOREIGN KEY (`username`)
    REFERENCES `team70`.`users` (`username`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);


#Theater
CREATE TABLE `team70`.`theater` (
  `comname` VARCHAR(45) NOT NULL,
  `thname` VARCHAR(45) NOT NULL,
  `capacity` INT NULL,
  `thstreet` VARCHAR(45) NULL,
  `thcity` VARCHAR(45) NULL,
  `thstate` VARCHAR(2) NULL,
  `thzipcode` INT(5) NULL,
  PRIMARY KEY (`comname`,`thname`),
  INDEX `emp_thname` (`thname` ASC) VISIBLE,
  CONSTRAINT `th_comname`
    FOREIGN KEY (`comname`)
    REFERENCES `team70`.`company` (`comname`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


#Employee
CREATE TABLE `team70`.`employee` (
  `username` VARCHAR(45) NOT NULL,
  `manstreet` VARCHAR(45) NULL,
  `mancity` VARCHAR(45) NULL,
  `manstate` VARCHAR(2) NULL,
  `manzipcode` INT(5) NULL,
  `employeetype` VARCHAR(45) NULL,
  `comname` VARCHAR(45) NULL,
  `thname` VARCHAR(45) NULL,
  PRIMARY KEY (`username`),
  INDEX `emp_company_idx` (`comname` ASC) VISIBLE,
  INDEX `emp_thname_idx` (`thname` ASC) VISIBLE,
  CONSTRAINT `emp_username`
    FOREIGN KEY (`username`)
    REFERENCES `team70`.`users` (`username`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `emp_comname`
    FOREIGN KEY (`comname`)
    REFERENCES `team70`.`company` (`comname`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `emp_thname`
    FOREIGN KEY (`thname`)
    REFERENCES `team70`.`theater` (`thname`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


#UserVisitTheater

CREATE TABLE `team70`.`uservisittheater` (
  `username` VARCHAR(45) NULL,
  `thname` VARCHAR(45) NULL,
  `comname` VARCHAR(45) NULL,
  `visitdate` DATE NULL,
  `visitid` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`visitid`),
  INDEX `visit_comname_idx` (`comname` ASC) VISIBLE,
  INDEX `visit_thname_idx` (`thname` ASC) VISIBLE,
  INDEX `visit_username_idx` (`username` ASC) VISIBLE,
  CONSTRAINT `visit_comname`
    FOREIGN KEY (`comname`)
    REFERENCES `team70`.`theater` (`comname`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `visit_thname`
    FOREIGN KEY (`thname`)
    REFERENCES `team70`.`theater` (`thname`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `visit_username`
    FOREIGN KEY (`username`)
    REFERENCES `team70`.`users` (`username`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;



#MoviePlay
CREATE TABLE `team70`.`movieplay` (
  `movname` VARCHAR(45) NOT NULL,
  `movreleasedate` DATE NOT NULL,
  `movplaydate` DATE NOT NULL,
  `thname` VARCHAR(45) NOT NULL,
  `comname` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`movname`, `movreleasedate`, `movplaydate`, `thname`, `comname`),
  INDEX `play_theater_idx` (`thname` ASC, `comname` ASC) VISIBLE,
  INDEX `view_playdate_idx` (`movplaydate` ASC) VISIBLE,
  CONSTRAINT `play_movie`
    FOREIGN KEY (`movname` , `movreleasedate`)
    REFERENCES `team70`.`movie` (`movname` , `movreleasedate`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `play_theater`
    FOREIGN KEY (`thname` , `comname`)
    REFERENCES `team70`.`theater` (`thname` , `comname`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


#CustomerViewMovie
CREATE TABLE `team70`.`customerviewmovie` (
  `movname` VARCHAR(45) NOT NULL,
  `movreleasedate` DATE NOT NULL,
  `movplaydate` DATE NOT NULL,
  `thname` VARCHAR(45) NOT NULL,
  `comname` VARCHAR(45) NOT NULL,
  `creditcardnum` VARCHAR(16) NOT NULL,
  PRIMARY KEY (`movname`, `movreleasedate`, `movplaydate`, `comname`, `thname`, `creditcardnum`),
  INDEX `cus_thname_idx` (`thname` ASC) VISIBLE,
  INDEX `cus_comname_idx` (`comname` ASC) VISIBLE,
  INDEX `cus_creditcardnum_idx` (`creditcardnum` ASC) VISIBLE,
  CONSTRAINT `cus_movname`
    FOREIGN KEY (`movname` , `movreleasedate`)
    REFERENCES `team70`.`movie` (`movname` , `movreleasedate`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `cus_thname`
    FOREIGN KEY (`thname`)
    REFERENCES `team70`.`theater` (`thname`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `cus_comname`
    FOREIGN KEY (`comname`)
    REFERENCES `team70`.`theater` (`comname`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `cus_creditcardnum`
    FOREIGN KEY (`creditcardnum`)
    REFERENCES `team70`.`customercreditcard` (`creditcardnum`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;
