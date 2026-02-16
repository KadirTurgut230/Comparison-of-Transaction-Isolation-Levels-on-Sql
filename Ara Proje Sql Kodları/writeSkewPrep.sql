create table if not exists writeSkew1(
    idnum integer primary key,
	available boolean
);

create table if not exists writeSkewTest(
    value integer
);

create index if not exists index2 on writeSkew1(idnum);

CREATE INDEX if not exists index2_2 ON writeSkew1(available);


create or replace function insertWriteSkew(member_size integer)
returns void as $$
Begin
	delete from writeSkew1;
	delete from writeSkewTest;
	insert into writeSkewTest values(0);
	FOR i in 1..member_size LOOP
		INSERT INTO writeSkew1(idnum) VALUES(i);
	END lOOP;
End;
$$ LANGUAGE plpgsql ;

--select insertWriteSkew(20);


create or replace function resetValuesWriteSkew()
returns void as $$
Declare
	countt integer;
Begin
	delete from writeSkewTest;
	insert into writeSkewTest values(0);
	select count(*) into countt
	from writeSkew1;
	update writeSkew1 set available = true
	where idnum <= countt/2;
	update writeSkew1 set available = false
	where idnum > countt/2;
	end;
$$ LANGUAGE plpgsql;

--select resetValuesWriteSkew();

--select * from writeSkew1 order by idnum;
--select * from writeSkewTest;


create or replace function WriteSkewFunc1()
returns void as $$
declare
	countt integer;
	X integer;
	Y boolean;
Begin
	select max (idnum) into countt
	from writeSkew1;
	select ceil(countt * random()) into x 
	from writeSkew1;

	select available into y from writeSkew1
	where idnum = x;
	update writeSkew1 set available = NOT y
	where idnum = x and
	(select count(*)
	from writeskew1
	where available = y) > countt*0.4 ;
	
end;
$$ LANGUAGE plpgsql ;

--select WriteSkewFunc1();




