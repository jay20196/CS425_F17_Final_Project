create table address(
	ID		numeric(5,0),
	street	varchar(30) NOT NULL,
	city	varchar(30) NOT NULL,
	state	char(2) NOT NULL,
	zip		numeric(5,0) NOT NULL,
	primary key (ID, street, city, state, zip),
	foreign key (ID) references gUser
);	

create table customer(
	name		varchar(30),
	email		varchar(30),
	customerID	numeric(5,0),
	balance		numeric(6,2) NOT NULL,
	orAirport		varchar(30),
	mileC		numeric(0,7),
	primary key(customerID),
	foreign key(customerID) references payment(paymentAddress)
);

create table payment(
	customerID 		numeric(5,0),
	cardNumber		char(16),
	paymentAddress	varchar(70) NOT NULL,
	activity		varchar(8) 	NOT NULL,
	primary key (cardNumber),
	foreign key (customerID) references customer
);

create table books(
	classT	varchar(15),
	cCreditID	numeric(5,0),
	primary key(cCreditID),
	foreign key (cCreditID) references payment




create table flight(
	flightID 	numeric(5,0),
	flightNum	numeric(7,0),
	fDate 	Date
	dTime	Time(0,7),
	aTime	Time(0,7),
	capacity 	numeric(0,4) NOT NULL,
	//(the capacity on max economy and first class) help here i dont know what to put
	primary key(flightID),
	foreign key(flightID) references airline,
);
	
create table airline(
	airlineID	numeric(6,0),
	aName	varchar(30) NOT NULL,
	oCountry		varchar(30) NOT NULL,
	primary key(airlineID),
	foreign key(airlineID) references airport,
);

create table airport(
	airportID 	numeric(5,0),
	aName	varchar(15),
	sName 	varchar(15),
	cName 	varchar(15),
	primary key(airportID),
	foreign key(airportID) references airline,
);

create table price(
	priceID 	numeric(5,0) NOT NULL,
	fclass	varchar(15),
	eclass	varchar(15),
	primary key(priceID),
	foreign key(priceID) references flight,
	check (status IN ('1','2','3'))//suppose to check what is eclass and fclass <--------HELP
);

