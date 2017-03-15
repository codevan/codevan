--#codevan 2017 - functional fibonacci function written in pl/sql
create or replace function  fibonacci (n number) return number  as 
-- linear recursion - can also be done with tail recursion
begin   
    if (n <= 1) then 
      return 0;    
    elsif (n = 2) then
      return 1;
    else 
      return ( fibonacci(n - 1) + fibonacci(n - 2) );
    end if;  
end fibonacci;
  /*
  select fibonacci(4) from dual; --should return 2
  select fibonacci(7) from dual; --should return 8
  input:   0,1,2,3,4,5,6,7
  returns: 0,0,1,1,2,3,5,8
  */
  /*
  set serveroutput on;
  begin 
   for i in 1 .. 10 loop
    dbms_output.put_line(fibonacci(i) );
   end loop;
  end; 
  */

