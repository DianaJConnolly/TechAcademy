/*
create database dbLibrary
*/

use master
go
if exists(select * from sys.databases where [name] = 'dbLibrary')
drop database dbLibrary
go
create database dbLibrary
go
use dbLibrary
go 
create table PUBLISHER
(
	Name varchar(255) NOT NULL PRIMARY KEY, 
	Address varchar(255) NOT NULL, 
	Phone varchar(20) NOT NULL
);
create table BORROWER
(
	CardNo integer NOT NULL PRIMARY KEY,
	Name varchar(255) NOT NULL,
	Address varchar(255) NOT NULL, 
	Phone varchar(20) NOT NULL
);
create table LIBRARY_BRANCH
(
	BranchId integer NOT NULL PRIMARY KEY, 
	BranchName varchar(255) NOT NULL, 
	Address varchar(255) NOT NULL
);
create table BOOK
(
	BookId integer NOT NULL, 
	Title varchar(255) NOT NULL, 
	PublisherName varchar(255) NOT NULL,
	PRIMARY KEY (BookID),
	constraint pbfk FOREIGN KEY (PublisherName) REFERENCES PUBLISHER(Name) 
	on update cascade
	on delete cascade
);
create table BOOK_AUTHORS
(
	BookId integer NOT NULL, 
	AuthorName varchar(255),
	PRIMARY KEY (BookID, AuthorName),
	constraint BookIDfk FOREIGN KEY (BookID) REFERENCES Book(BookID)  
	on update cascade
	on delete cascade
);
create table BOOK_COPIES
(
	BookId integer NOT NULL, 
	BranchId integer NOT NULL, 
	No_Of_Copies integer NOT NULL,
	PRIMARY KEY (BookID, BranchId),
	constraint BookIDBCfk FOREIGN KEY (BookID) REFERENCES Book(BookID),
	constraint BranchIDBCfk FOREIGN KEY (BranchID) REFERENCES LIBRARY_BRANCH(BranchID)  
	on update cascade
	on delete cascade
);
create table BOOK_LOANS
(
	BookId integer NOT NULL, 
	BranchId integer NOT NULL,
	CardNo integer NOT NULL,
	DateOut date NOT NULL,
	DueDate date NOT NULL,
	PRIMARY KEY(BookId, BranchId, CardNo),
	constraint BookIDBLfk FOREIGN KEY (BookID) REFERENCES Book(BookID),
	constraint BranchIDBLfk FOREIGN KEY (BranchID) REFERENCES LIBRARY_BRANCH(BranchID),
	constraint CardNoBLfk FOREIGN KEY (CardNo) REFERENCES BORROWER(CardNo) 
	on update cascade
	on delete cascade
);