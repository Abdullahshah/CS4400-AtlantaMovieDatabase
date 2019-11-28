USE `team70`;
#USERS

INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('calcultron','Dwight','Schrute',MD5('333333333'),'Employee, Customer','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('calcultron2','Jim','Halpert',MD5('444444444'),'Customer','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('calcwizard','Issac','Newton',MD5('222222222'),'Customer','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('clarinetbeast','Squidward','Tentacles',MD5('999999999'),'Customer','Declined');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('cool_class4400','A. TA','Washere',MD5('333333333'),'Employee, Customer','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('DNAhelix','Rosalind','Franklin',MD5('777777777'),'Customer','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('does2Much','Carl','Gauss',MD5('1212121212'),'Customer','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('eeqmcsquare','Albert','Einstein',MD5('111111110'),'Customer','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('entropyRox','Claude','Shannon',MD5('999999999'),'Employee, Customer','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('fatherAI','Alan','Turing',MD5('222222222'),'Employee','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('fullMetal','Edward','Elric',MD5('111111100'),'Customer','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('gdanger','Gary','Danger',MD5('555555555)','User','Declined');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('georgep','George P.','Burdell',MD5('111111111'),'Employee, Customer','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('ghcghc','Grace','Hopper',MD5('666666666'),'Employee','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('ilikemoney$$','Eugene','Krabs',MD5('111111110'),'Customer','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('imbatman','Bruce','Wayne',MD5('666666666'),'Employee','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('imready','Spongebob','Squarepants',MD5('777777777'),'Customer','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('isthisthekrustykrab','Patrick','Star',MD5('888888888'),'Customer','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('manager1','Manager','One',MD5('1122112211'),'Employee','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('manager2','Manager','Two',MD5('3131313131'),'Employee','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('manager3','Three','Three',MD5('8787878787'),'Employee','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('manager4','Four','Four',MD5('5755555555'),'Employee','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('notFullMetal','Alphonse','Elric',MD5('111111100'),'Customer','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('programerAAL','Ada','Lovelace',MD5('3131313131'),'Customer','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('radioactivePoRa','Marie','Curie',MD5('1313131313'),'Employee','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('RitzLover28','Abby','Normal',MD5('444444444'),'Customer','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('smith_j','John','Smith',MD5('333333333'),'User','Pending');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('texasStarKarate','Sandy','Cheeks',MD5('111111110'),'User','Declined');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('thePiGuy3.14','Archimedes','Syracuse',MD5('1111111111'),'Customer','Approved');
INSERT INTO `users` (`username`,`firstname`,`lastname`,`password`,`usertype`,`status`) VALUES ('theScienceGuy','Bill','Nye',MD5('999999999'),'Customer','Approved');


#COMPANY

INSERT INTO `company` (`comname`) VALUES ('EZ Theater Company');
INSERT INTO `company` (`comname`) VALUES ('4400 Theater Company');
INSERT INTO `company` (`comname`) VALUES ('Awesome Theater Company');
INSERT INTO `company` (`comname`) VALUES ('AI Theater Company');


#MOVIE

INSERT INTO `movie` (`movname`,`movreleasedate`,`duration`) VALUES ('George P Burdell\'s Life Story','1927-08-12',100);
INSERT INTO `movie` (`movname`,`movreleasedate`,`duration`) VALUES ('Georgia Tech The Movie','1985-08-13',100);
INSERT INTO `movie` (`movname`,`movreleasedate`,`duration`) VALUES ('Spaceballs','1987-06-24',96);
INSERT INTO `movie` (`movname`,`movreleasedate`,`duration`) VALUES ('The First Pokemon Movie','1998-07-19',75);
INSERT INTO `movie` (`movname`,`movreleasedate`,`duration`) VALUES ('How to Train Your Dragon','2010-03-21',98);
INSERT INTO `movie` (`movname`,`movreleasedate`,`duration`) VALUES ('The King\'s Speech','2010-11-26',119);
INSERT INTO `movie` (`movname`,`movreleasedate`,`duration`) VALUES ('Spider-Man: Into the Spider-Verse','2018-12-01',117);
INSERT INTO `movie` (`movname`,`movreleasedate`,`duration`) VALUES ('Avengers: Endgame','2019-04-26',181);
INSERT INTO `movie` (`movname`,`movreleasedate`,`duration`) VALUES ('4400 The Movie','2019-08-12',130);
INSERT INTO `movie` (`movname`,`movreleasedate`,`duration`) VALUES ('Calculus Returns: A ML Story','2019-09-19',314);


#CUSTOMERCREDITCARD

INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('calcultron',1111111111000000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('calcultron2',1111111100000000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('calcultron2',1111111110000000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('calcwizard',1111111111100000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('cool_class4400',2222222222000000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('DNAhelix',2220000000000000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('does2Much',2222222200000000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('eeqmcsquare',2222222222222200);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('entropyRox',2222222222200000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('entropyRox',2222222222220000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('fullMetal',1100000000000000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('georgep',1111111111110000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('georgep',1111111111111000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('georgep',1111111111111100);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('georgep',1111111111111110);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('georgep',1111111111111111);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('ilikemoney$$',2222222222222220);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('ilikemoney$$',2222222222222222);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('ilikemoney$$',9000000000000000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('imready',1111110000000000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('isthisthekrustykrab',1110000000000000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('isthisthekrustykrab',1111000000000000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('isthisthekrustykrab',1111100000000000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('notFullMetal',1000000000000000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('programerAAL',2222222000000000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('RitzLover28',3333333333333300);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('thePiGuy3.14',2222222220000000);
INSERT INTO `customercreditcard` (`username`,`creditcardnum`) VALUES ('theScienceGuy',2222222222222000);


#THEATER

INSERT INTO `theater` (`comname`,`thname`,`capacity`,`thstreet`,`thcity`,`thstate`,`thzipcode`) VALUES ('4400 Theater Company','Cinema Star','4','100 Cool Place','San Francisco','CA',94016);
INSERT INTO `theater` (`comname`,`thname`,`capacity`,`thstreet`,`thcity`,`thstate`,`thzipcode`) VALUES ('4400 Theater Company','Jonathan\'s Movies','2','67 Pearl Dr','Seattle','WA',98101);
INSERT INTO `theater` (`comname`,`thname`,`capacity`,`thstreet`,`thcity`,`thstate`,`thzipcode`) VALUES ('4400 Theater Company','Star Movies','5','4400 Rocks Ave','Boulder','CA',80301);
INSERT INTO `theater` (`comname`,`thname`,`capacity`,`thstreet`,`thcity`,`thstate`,`thzipcode`) VALUES ('AI Theater Company','ML Movies','3','314 Pi St','Pallet Town','KS',31415);
INSERT INTO `theater` (`comname`,`thname`,`capacity`,`thstreet`,`thcity`,`thstate`,`thzipcode`) VALUES ('Awesome Theater Company','ABC Theater','5','880 Color Dr','Austin','TX',73301);
INSERT INTO `theater` (`comname`,`thname`,`capacity`,`thstreet`,`thcity`,`thstate`,`thzipcode`) VALUES ('EZ Theater Company','Main Movies','3','123 Main St','New York','NY',10001);
INSERT INTO `theater` (`comname`,`thname`,`capacity`,`thstreet`,`thcity`,`thstate`,`thzipcode`) VALUES ('EZ Theater Company','Star Movies','2','745 GT St','Atlanta','GA',30332);


#EMPLOYEE

INSERT INTO `employee` (`username`,`manstreet`,`mancity`,`manstate`,`manzipcode`,`employeetype`,`comname`,`thname`) VALUES ('cool_class4400',NULL,NULL,NULL,NULL,'Admin',NULL,NULL);
INSERT INTO `employee` (`username`,`manstreet`,`mancity`,`manstate`,`manzipcode`,`employeetype`,`comname`,`thname`) VALUES ('entropyRox','200 Cool Place','San Francisco','CA',94016,'Manager','4400 Theater Company','Cinema Star');
INSERT INTO `employee` (`username`,`manstreet`,`mancity`,`manstate`,`manzipcode`,`employeetype`,`comname`,`thname`) VALUES ('fatherAI','456 Main St','New York','NY',10001,'Manager','EZ Theater Company','Main Movies');
INSERT INTO `employee` (`username`,`manstreet`,`mancity`,`manstate`,`manzipcode`,`employeetype`,`comname`,`thname`) VALUES ('georgep','10 Pearl Dr','Seattle','WA',98105,'Manager','4400 Theater Company','Jonathan\'s Movies');
INSERT INTO `employee` (`username`,`manstreet`,`mancity`,`manstate`,`manzipcode`,`employeetype`,`comname`,`thname`) VALUES ('calcultron','123 Peachtree St','Atlanta','GA',30308,'Manager','EZ Theater Company','Star Movies');
INSERT INTO `employee` (`username`,`manstreet`,`mancity`,`manstate`,`manzipcode`,`employeetype`,`comname`,`thname`) VALUES ('imbatman','800 Color Dr','Austin','TX',78653,'Manager','Awesome Theater Company','ABC Theater');
INSERT INTO `employee` (`username`,`manstreet`,`mancity`,`manstate`,`manzipcode`,`employeetype`,`comname`,`thname`) VALUES ('ghcghc','100 Pi St','Pallet Town','KS',31415,'Manager','AI Theater Company','ML Movies');
INSERT INTO `employee` (`username`,`manstreet`,`mancity`,`manstate`,`manzipcode`,`employeetype`,`comname`,`thname`) VALUES ('radioactivePoRa','100 Blu St','Sunnyvale','CA',94088,'Manager','4400 Theater Company','Star Movies');
INSERT INTO `employee` (`username`,`manstreet`,`mancity`,`manstate`,`manzipcode`,`employeetype`,`comname`,`thname`) VALUES ('manager1','123 Ferst Drive','Atlanta','GA',30332,'Manager','4400 Theater Company', NULL);
INSERT INTO `employee` (`username`,`manstreet`,`mancity`,`manstate`,`manzipcode`,`employeetype`,`comname`,`thname`) VALUES ('manager2','456 Ferst Drive','Atlanta','GA',30332,'Manager','AI Theater Company', NULL);
INSERT INTO `employee` (`username`,`manstreet`,`mancity`,`manstate`,`manzipcode`,`employeetype`,`comname`,`thname`) VALUES ('manager3','789 Ferst Drive','Atlanta','GA',30332,'Manager','4400 Theater Company', NULL);
INSERT INTO `employee` (`username`,`manstreet`,`mancity`,`manstate`,`manzipcode`,`employeetype`,`comname`,`thname`) VALUES ('manager4','000 Ferst Drive','Atlanta','GA',30332,'Manager','4400 Theater Company', NULL);


#USERVISITTHEATER

INSERT INTO `uservisittheater` (`username`,`thname`,`comname`,`visitdate`,`visitID`) VALUES ('georgep','Main Movies','EZ Theater Company','2010-03-22',1);
INSERT INTO `uservisittheater` (`username`,`thname`,`comname`,`visitdate`,`visitID`) VALUES ('calcwizard','Main Movies','EZ Theater Company','2010-03-22',2);
INSERT INTO `uservisittheater` (`username`,`thname`,`comname`,`visitdate`,`visitID`) VALUES ('calcwizard','Star Movies','EZ Theater Company','2010-03-25',3);
INSERT INTO `uservisittheater` (`username`,`thname`,`comname`,`visitdate`,`visitID`) VALUES ('imready','Star Movies','EZ Theater Company','2010-03-25',4);
INSERT INTO `uservisittheater` (`username`,`thname`,`comname`,`visitdate`,`visitID`) VALUES ('calcwizard','ML Movies','AI Theater Company','2010-03-20',5);


#MOVIEPLAY

INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('George P Burdell\'s Life Story','1927-08-12','2010-05-20','Cinema Star','4400 Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('George P Burdell\'s Life Story','1927-08-12','2019-07-14','Main Movies','EZ Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('George P Burdell\'s Life Story','1927-08-12','2019-10-22','Main Movies','EZ Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('Georgia Tech The Movie','1985-08-13','1985-08-13','ABC Theater','Awesome Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('Georgia Tech The Movie','1985-08-13','2019-09-30','Cinema Star','4400 Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('Spaceballs','1987-06-24','1999-06-24','Main Movies','EZ Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('Spaceballs','1987-06-24','2000-02-02','Cinema Star','4400 Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('Spaceballs','1987-06-24','2010-04-02','ML Movies','AI Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('Spaceballs','1987-06-24','2023-01-23','ML Movies','AI Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('The First Pokemon Movie','1998-07-19','2018-07-19','ABC Theater','Awesome Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('How to Train Your Dragon','2010-03-21','2010-03-22','Main Movies','EZ Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('How to Train Your Dragon','2010-03-21','2010-03-23','Main Movies','EZ Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('How to Train Your Dragon','2010-03-21','2010-03-25','Star Movies','EZ Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('How to Train Your Dragon','2010-03-21','2010-04-02','Cinema Star','4400 Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('The King\'s Speech','2010-11-26','2019-12-20','Cinema Star','4400 Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('The King\'s Speech','2010-11-26','2019-12-20','Main Movies','EZ Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('Spider-Man: Into the Spider-Verse','2018-12-01','2019-09-30','ML Movies','AI Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('4400 The Movie','2019-08-12','2019-08-12','Star Movies','EZ Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('4400 The Movie','2019-08-12','2019-09-12','Cinema Star','4400 Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('4400 The Movie','2019-08-12','2019-10-12','ABC Theater','Awesome Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('Calculus Returns: A ML Story','2019-09-19','2019-10-10','ML Movies','AI Theater Company');
INSERT INTO `movieplay` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`) VALUES ('Calculus Returns: A ML Story','2019-09-19','2019-12-30','ML Movies','AI Theater Company');


#CUSTOMERVIEWMOVIE

INSERT INTO `customerviewmovie` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`,`creditcardnum`) VALUES ('How to Train Your Dragon','2010-03-21','2010-03-22','Main Movies','EZ Theater Company',1111111111111111);
INSERT INTO `customerviewmovie` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`,`creditcardnum`) VALUES ('How to Train Your Dragon','2010-03-21','2010-03-23','Main Movies','EZ Theater Company',1111111111111111);
INSERT INTO `customerviewmovie` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`,`creditcardnum`) VALUES ('How to Train Your Dragon','2010-03-21','2010-03-25','Star Movies','EZ Theater Company',1111111111111100);
INSERT INTO `customerviewmovie` (`movname`,`movreleasedate`,`movplaydate`,`thname`,`comname`,`creditcardnum`) VALUES ('How to Train Your Dragon','2010-03-21','2010-04-02','Cinema Star','4400 Theater Company',1111111111111111);


