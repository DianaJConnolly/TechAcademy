/*Populate Library Tables*/
use master
go
use dbLibrary
go
bulk insert PUBLISHER
from 'C:\Users\Student\Desktop\publisher.txt'
With(
	fieldterminator = '0x09',
	rowterminator = '0x0A'
	)
go
bulk insert BORROWER
from 'C:\Users\Student\Desktop\Borrower.txt'
With(
	fieldterminator = '0x09',
	rowterminator = '0x0A'
	)
go
bulk insert LIBRARY_BRANCH
from 'C:\Users\Student\Desktop\LibraryBranch.txt'
With(
	fieldterminator = '0x09',
	rowterminator = '0x0A'
	)
go
bulk insert BOOK
from 'C:\Users\Student\Desktop\Book.txt'
With(
	fieldterminator = '0x09',
	rowterminator = '0x0A'
	)
go
bulk insert BOOK_AUTHORS
from 'C:\Users\Student\Desktop\BookAuthor.txt'
With(
	fieldterminator = '0x09',
	rowterminator = '0x0A'
	)
go
bulk insert BOOK_COPIES
from 'C:\Users\Student\Desktop\BookCopies.txt'
With(
	fieldterminator = '0x09',
	rowterminator = '0x0A'
	)
go
bulk insert BOOK_LOANS
from 'C:\Users\Student\Desktop\BookLoans.txt'
With(
	fieldterminator = '0x09',
	rowterminator = '0x0A'
	)
go
