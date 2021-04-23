use hospital;
delimiter $$
drop trigger if exists insert_patient;
create trigger insert_patient
before insert on patient for each row
begin
	if (length(new.pname)<2 ) or (new.pname is null) or (not(new.pname regexp '^[A-Za-z]+$'))then 
	signal SQLSTATE '11111'
	set message_text='Invalid Name';
	end if;
	IF length(NEW.pphone)<10 or length(NEW.pphone)>10 or NEW.pphone is null
	then
		SIGNAL SQLSTATE '22222'
		SET MESSAGE_TEXT= 'Phone number should be 10 digit';
	END IF;
	if (length(new.pdisease)<3 ) or (new.pdisease is null) then 
	signal SQLSTATE '33333'
	set message_text='Invalid disease';
	end if;
	if ((select count(did) from doctor where did=new.pdoctor)<1) or (new.pdoctor is null) then 
	signal SQLSTATE '44444'
	set message_text='No doctor with this id';
	end if;
END;
drop trigger if exists insert_doctor;
create trigger insert_doctor
before insert on doctor for each row
begin
	if new.did is null then 
	signal SQLSTATE '66666'
	set message_text='Doctor ID should not be blank';
	end if;
	
	if (length(new.dname)<2 ) or (new.dname is null) or (not(new.dname regexp '^[A-Za-z]+$'))then 
	signal SQLSTATE '55555'
	set message_text='Invalid doctor Name';
	end if;
	
END;
drop trigger if exists insert_room;
create trigger insert_room
before insert on room for each row
begin
	if new.rno not in('101','102','103','104','105','106','107','108','109','110') or new.rno is null then 
	signal SQLSTATE '77777'
	set message_text='Invalid Room No.';
	end if;
	
	if new.startdate is null or (not(new.startdate regexp '^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$'))then 
	signal SQLSTATE '88888'
	set message_text='Invalid Date use YYYY-MM-DD format for the date';
	end if;
	
	if new.pid is null or ((select count(pid) from patient where pid=new.pid)<1)then 
	signal SQLSTATE '99999'
	set message_text='Invalid Patient add Patient entry First';
	end if;
	
END;
$$