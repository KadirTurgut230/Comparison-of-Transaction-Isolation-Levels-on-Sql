create table if not exists phantom1(
	num integer
);

create table if not exists phantomTest(
	error integer
);

--insert into phantomTest values(0);

--delete from phantom1;

--select * from phantom1 order by num;
--select * from phantomTest;

create or replace function 
initilaize_phantom_table(member_num integer)
returns void as $$
Declare
	numberr integer;
Begin
	delete from phantom1;
	delete from phantomTest;
	insert into phantomTest values(0);
	FOR i IN 1..member_num LOOP
		select ceil(100*random()) into numberr;
		insert into phantom1 values(numberr);
	END LOOP;
end;
$$ LANGUAGE plpgsql ;

--select initilaize_phantom_table(20);

create or replace function insert_phantom_table()
returns void as $$
Declare
	numberr integer;
Begin
	select ceil(100*random()) into numberr;
	insert into phantom1 values(numberr);
end;
$$ LANGUAGE plpgsql;

--select insert_phantom_table();


create or replace function delete_phantom_table()
returns void as $$
Declare
Begin
	DELETE FROM phantom1 
    WHERE ctid = (
        SELECT ctid
        FROM phantom1 
        WHERE num = ceil(random() * 100)
        LIMIT 1
    );
end;
$$ LANGUAGE plpgsql;

--select delete_phantom_table();




create or replace function phantom_test()
returns void as $$
Declare
	x integer;
	y integer;
Begin
	select sum(num) into x from phantom1;
	select sum(num) into y from phantom1;

	IF x <> y then
		update phantomTest set error = error + 1;
	END IF;
	
end;
$$ LANGUAGE plpgsql ;

--select phantom_test();

