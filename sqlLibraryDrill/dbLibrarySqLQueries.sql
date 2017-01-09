--SQL Drill Exercises
use master
go
use dbLibrary
go
--1. How many copies of the book titled The Lost Tribe 
--are owned by the library branch whose name is"Sharpstown"?
select bc.No_Of_Copies, lb.BranchName from BOOK_COPIES bc
left join BOOK b ON bc.BookId = b.Bookid
left join LIBRARY_BRANCH lb ON lb.BranchId = bc.BranchId 
Where b.Title = 'The Lost Tribe' and lb.BranchName = 'Sharpstown';

--2. How many copies of the book titled The Lost Tribe are owned by each library branch?
select bc.No_Of_Copies, lb.BranchName from BOOK_COPIES bc
left join BOOK b ON bc.BookId = b.Bookid
left join LIBRARY_BRANCH lb ON lb.BranchId = bc.BranchId 
Where b.Title = 'The Lost Tribe';

--3. Retrieve the names of all borrowers who do not have any books checked out.
-- expect return of "Tom Hanks"
select b.name from BORROWER b
left join BOOK_LOANS bl 
on b.CardNo =  bl.CardNo 
where bl.CardNo is null

--4. For each book that is loaned out from the "Sharpstown" branch and whose DueDate is today,
--retrieve the book title, the borrower's name, and the borrower's address
select b.Title, br.Name as "Borrower's Name", br.Address as "Borrower's Address" from BOOK_LOANS bl
inner join Borrower br on bl.CardNo = br.CardNo 
right join LIBRARY_BRANCH lb on lb.BranchId = bl.BranchId
right join BOOK b on bl.BookId = b.BookId
where DueDate = convert(varchar(10), getdate(), 111) and lb.BranchName = 'Sharpstown'

--5. For each library branch, retrieve the branch name and the total number of books loaned out from that branch.
select lb.BranchName, count(bl.BranchId) as totalNumberOfBooksOut from LIBRARY_BRANCH lb 
inner join BOOK_LOANS bl ON lb.BranchId = bl.BranchId
group by lb.BranchName;

--6. Retrieve the names, addresses, and number of books checked out for all borrowers who have more than five books checked out.
select br.Name, br.Address, count(bl.CardNo) from BORROWER as br
inner join BOOK_LOANS bl on bl.CardNo = br.CardNo
group by br.Name, br.Address
having count(bl.CardNo) > 5
order by br.Name ASC

--Update BOOK_AUTHORS set AuthorName = 'Stephen King' where AuthorName like 'Steven King%'
--7. For each book authored (or co-authored) by "Stephen King", retrieve the title and the number of
--copies owned by the library branch whose name is "Central"
select b.Title, ba.AuthorName, bc.No_Of_Copies, lb.BranchName from BOOK b 
inner join BOOK_COPIES bc on b.BookId = bc.BookId 
inner join LIBRARY_BRANCH lb on bc.BranchId = lb.BranchId 
inner join BOOK_AUTHORS ba on b.BookId = ba.BookId
where  lb.BranchName = 'Central' and AuthorName = 'Stephen King'

--8. create a stored procedure that will execute one or more of those queries, based on user choice.
See StoredProc.sql
