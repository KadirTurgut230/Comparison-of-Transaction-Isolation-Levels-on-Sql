begin;
set transaction isolation level read committed;
  select myfunc1();
  select myfunc2();
commit;

--select sum(balance) from table1;
--select * from table1 order by table1;