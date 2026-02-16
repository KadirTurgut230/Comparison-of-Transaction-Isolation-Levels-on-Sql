create table if not exists lost_update1(
    idnum integer primary key,
	balance integer
);

create table if not exists lost_update_Test(
    sum integer
);

create index if not exists index1 on lost_update1(idnum);

create or replace function initialize_lost_Update(member_size integer) 
returns void as $$
declare
	bal integer;
	summ integer;
Begin
	delete from lost_update1;
	delete from lost_update_Test;
	for i in 1..member_size loop
		bal := ceil(100*random());
		insert into lost_Update1 values(i, bal);
	end loop;
	select sum(balance) into summ from lost_update1;
	insert into lost_Update_Test values(summ);
	
end;
$$ LANGUAGE plpgsql ;

--select initialize_lost_Update(20);

--select * from lost_update1 order by idnum;
--select * from lost_update_Test;
--select sum(balance) from lost_update1;



CREATE OR REPLACE FUNCTION myfunc1() RETURNS void AS $$
DECLARE
	data_size integer;
    x INTEGER;
	y INTEGER;
BEGIN
	select max(idnum) into data_size 
	from lost_Update1;

    select ceil(data_size*random()) into x; 

	select balance into y from lost_update1
	where idnum = x;

	update lost_update1 set balance = y + 1
	where idnum = x;
END;
$$ LANGUAGE plpgsql;

--select myFunc1();

CREATE OR REPLACE FUNCTION myfunc2() RETURNS void AS $$
DECLARE
	data_size integer;
    x INTEGER;
	y INTEGER;
BEGIN
    select max(idnum) into data_size 
	from lost_Update1;

    select ceil(data_size*random()) into x;

	select balance into y from lost_update1 
	where idnum = x;

	update lost_update1 set balance = y - 1
	where idnum = x;
END;
$$ LANGUAGE plpgsql;

--select myFunc2();