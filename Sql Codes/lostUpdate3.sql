begin;
set transaction isolation level serializable;
\set cid :client_id
\if :cid % 2 = 0
  select myfunc1();
\else 
	select myfunc2();
\endif
commit;

--select sum(balance) from table1;
--select * from table1 order by table1;