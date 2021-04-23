use hospital;
delimiter $$
create procedure doctor()
begin
	select *  from doctor;
end $$ 
delimiter ;

delimiter $$
create procedure patient()
begin
	select pid,pname,pphone,pdisease,dname from patient,doctor where pdoctor=did;
end $$ 
delimiter ;

delimiter $$
create procedure room()
begin
	select patient.pid,pname,pphone,pdisease,rno,startdate from patient,room where patient.pid=room.pid;
end $$ 
delimiter ;

delimiter $$
create procedure days(IN sdate date ,IN ddate date)
begin
	select DATEDIFF(ddate,sdate);
end $$ 
delimiter ;