begin;
set transaction isolation level repeatable read;
\if :client_id % 5 = 0
  	select phantom_test();
\elif :client_id % 5 <= 2
  	select delete_phantom_table();		  
\else 
	select insert_phantom_table();
\endif
commit;
