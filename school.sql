create database if not exists School;
use School;
create table if not exists staff (id int primary key,teachername varchar(30),classes set('1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'));
desc staff;
create table if not exists student (studentname varchar(30),rno int primary key,class enum('1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'));
desc student;
create table if not exists info(class set('1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'),subject varchar(20),teacher varchar(30));
desc info;
create table if not exists fees(studentname varchar(30),class enum('1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'),fee set('paid','not paid'));
desc info;
create table if not exists salary(teacher varchar(30), sal float(10,2));
desc salary;
create table if not exists room (roomno enum('101','102','103','104','105'),startime TIME,endtime TIME,studentname varchar(30),class enum('1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'));
desc room;
 