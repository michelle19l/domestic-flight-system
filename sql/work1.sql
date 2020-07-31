DROP DATABASE IF EXISTS Domestic_Flight;
CREATE DATABASE IF NOT EXISTS Domestic_Flight
DEFAULT CHARACTER SET utf8mb4	
DEFAULT COLLATE utf8mb4_unicode_ci;

Use Domestic_Flight;

CREATE TABLE IF NOT EXISTS airline(
code	char(3)	PRIMARY KEY,
airlinename	varchar(1024) 	not null
);


CREATE TABLE IF NOT EXISTS airport(
airportno	char(4)	PRIMARY KEY,
airportname varchar(100)	not null
);

CREATE TABLE IF NOT EXISTS flight(
flightno	char(7)	PRIMARY KEY,
dept_airport	char(4)	not null,
arv_airport	char(4)	not null,
code		char(3)	not null,
FOREIGN KEY (dept_airport) REFERENCES airport (airportno)
	ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (arv_airport) REFERENCES airport (airportno)
	ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (code) REFERENCES airline (code)
	ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS timetable(
flightno	char(7),
deptdate	int(8),
depttime	smallint(4)	not null,
arvtime smallint(4)	not null,
seats_total	smallint(4)	not null,
seats_current	smallint(4)	not null,
FOREIGN KEY (flightno) REFERENCES flight (flightno)
	ON DELETE CASCADE ON UPDATE CASCADE,
PRIMARY KEY(deptdate,flightno)
);

CREATE TABLE IF NOT EXISTS passenger(
id_passportno varchar(50) PRIMARY KEY,
nationality	varchar(20),
tel	bigint(11)	,
enname	varchar(50)
);

CREATE TABLE IF NOT EXISTS chinese(
id_passportno varchar(50) PRIMARY KEY,
cnname	varchar(20),
ethnic	char(5),
FOREIGN KEY (id_passportno) REFERENCES passenger (id_passportno)
	ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS foreigner(
id_passportno varchar(50) PRIMARY KEY,
visano	varchar(100),
FOREIGN KEY (id_passportno) REFERENCES passenger (id_passportno)
	ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS ticket(
flightno	char(7),
deptdate	int(8),
seat	smallint(4)	not null,
id_passportno	varchar(50)	not null,
PRIMARY KEY (flightno,deptdate,seat)
);

ALTER TABLE `ticket`
	ADD FOREIGN KEY (deptdate) REFERENCES timetable (deptdate)
		ON DELETE CASCADE ON UPDATE CASCADE,
	ADD FOREIGN KEY (flightno) REFERENCES timetable (flightno)
		ON DELETE CASCADE ON UPDATE CASCADE,
	ADD FOREIGN KEY (id_passportno) REFERENCES passenger (id_passportno)
		ON DELETE NO ACTION ON UPDATE CASCADE;
