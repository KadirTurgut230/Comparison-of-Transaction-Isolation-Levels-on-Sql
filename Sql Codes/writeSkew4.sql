begin;
set transaction isolation level read committed;
	select writeskewFunc1();
	select writeskewFunc1();
	select writeskewFunc1();
	select writeskewFunc1();
  	update writeSkewTest set value = value + 1
	where (select count(*) from writeSkew1 
			where available = true) not between 0.4*(select max(idnum)
											from writeSkew1)
									and 0.6*(select max(idnum)
											from writeSkew1);
commit;