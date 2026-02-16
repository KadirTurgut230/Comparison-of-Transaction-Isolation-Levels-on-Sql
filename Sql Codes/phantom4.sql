begin;
set transaction isolation level serializable;
  	select phantom_test();
	select insert_phantom_table();
  	select delete_phantom_table();		
commit;
