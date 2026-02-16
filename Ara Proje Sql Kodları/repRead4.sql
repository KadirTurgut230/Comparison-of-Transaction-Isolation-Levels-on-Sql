begin;
set transaction isolation level serializable;
  	update repRead1 set value = value + 1
	WHERE idnum = (SELECT CEIL(MAX(idnum) * random()) FROM repRead1);
  	update repRead1 set value = value - 1
	WHERE idnum = (SELECT CEIL(MAX(idnum) * random()) FROM repRead1);
	select repRead1Func();
commit;