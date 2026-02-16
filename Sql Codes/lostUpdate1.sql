begin;
set transaction isolation level read committed;
\set cid :client_id
\if :cid % 2 = 0
  	select myfunc1();
\else 
	select myfunc2();
\endif
commit;

--rollback;
--select sum(balance) from table1 ;
--select * from table1 order by idnum;

