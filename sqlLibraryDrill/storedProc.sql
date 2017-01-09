use AdventureWorks2012
go
create procedure dbo.uspGetEmailAddress @lastName varchar(50), @stateName varchar(50)
as
select p.BusinessEntityID, bea.BusinessEntityID, p.LastName, sp.Name, ea.EmailAddress,
	   a.AddressID, sp.StateProvinceID
from Person.Person as p 
inner join Person.BusinessEntityAddress as bea on p.BusinessEntityID = bea.BusinessEntityID
inner join Person.Address a on a.AddressID = bea.AddressID
inner join Person.StateProvince sp on a.StateProvinceID = sp.StateProvinceID
inner join Person.EmailAddress ea on ea.BusinessEntityID = bea.BusinessEntityID
where p.LastName = @lastName and sp.Name = @stateName
go

exec dbo.uspGetEmailAddress @lastName = 'Smith', @stateName = 'California'