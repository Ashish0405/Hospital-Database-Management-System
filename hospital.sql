create database if not exists hospital;
use hospital;
create table if not exists doctor(
did int primary key,
dname varchar(30) not null
);  

create table if not exists patient(
pid int primary key,
pname varchar(30) not null,
pphone varchar(10) not null, 
pdisease varchar(30) not null,
pdoctor int,
foreign key (pdoctor) references doctor(did)
on delete CASCADE
);


create table if not exists room(
rno enum('101','102','103','104','105','106','107','108','109','110') primary key not null,
startdate DATE not null,
pid int,
foreign key (pid) references patient(pid)
on delete CASCADE
);

create table if not exists perrec like patient;
