begin;
set transaction isolation level serializable;
\set cid :client_id
\if :cid % 3 = 1
  	update repRead1 set value = value + 1
	WHERE idnum = (SELECT CEIL(MAX(idnum) * random()) FROM repRead1);
\elif :cid % 3 = 2
  	update repRead1 set value = value - 1
	WHERE idnum = (SELECT CEIL(MAX(idnum) * random()) FROM repRead1);
\else 
	select repRead1Func();
\endif
commit;

-- select * from repRead;