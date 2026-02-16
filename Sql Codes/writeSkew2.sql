begin;
set transaction isolation level repeatable read;
\set cid :client_id
\if :cid % 5 = 0
  	update writeSkewTest set value = value + 1
	where (select count(*) from writeSkew1 
			where available = true) not between 0.4*(select max(idnum)
											from writeSkew1)
									and 0.6*(select max(idnum)
											from writeSkew1);
\else 
	select writeskewFunc1();
\endif
commit;
