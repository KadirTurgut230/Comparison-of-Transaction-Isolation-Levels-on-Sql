create table if not exists repRead1(
idnum integer primary key,
value integer
);

create index if not exists index3 on repRead1(idnum);


create table if not exists repReadTest(
error integer
);

--select * from repRead1;

create or replace function insert_to_RepRead1(member_size integer)
returns void as $$
Declare 
	X integer;
Begin
	delete from repRead1;
	delete from repReadTest;
	insert into repReadTest values(0);
	FOR i in 1..member_size LOOP
		select ceil(100*random()) into X;
		INSERT INTO repread1(idnum, value) VALUES(i, X);
	END lOOP;
End;
$$ LANGUAGE plpgsql ;

--select insert_to_RepRead1(20);




create or replace function repRead1Func()
returns void as $$
declare
 	data_size integer;
	X integer;
	value1 integer;
	value2 integer;
Begin
	select max(idnum) into data_size 
	from lost_Update1;

    select ceil(data_size*random()) into x; 
	
	select value into value1 
	from repRead1
	where idnum = x;
	
	select value into value2 from repRead1
	where idnum = X;

	if value1 <> value2 then
		update repReadTest set error = error +1;
	end if;
end;
$$ LANGUAGE plpgsql ;

--select repRead1Func();
