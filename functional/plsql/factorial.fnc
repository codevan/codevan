--#codevan 2017 - functional factorial function written in pl/sql
create or replace function  factorial (n number) return number  as 
  function  go (n number, acc number) return number  as 
    -- this is the recursive helper function which replaces LOOP
  begin
    if (n <= 0) then 
      return acc;
    else 
      return go(n-1, n*acc);
    end if;  
  end go;
begin
  return go(n,1);  
end;
-- select factorial(3) from dual; --should return 6
-- select factorial(4) from dual; --should return 24



