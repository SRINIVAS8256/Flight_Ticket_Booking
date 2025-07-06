CREATE DATABASE FLIGHT_BOOKING;
USE FLIGHT_BOOKING;
                                     /*#USER*/
/*Login and signin*/
CREATE TABLE Login_Signin (
	 User_name  varchar(50),
     User_email varchar(50) unique,
     User_mob   varchar(10) unique,
     User_pass  varchar(15) 
);
/*select * from Login_Signin;*/
									/*#ADMIN*/
/* Flight table*/
CREATE TABLE Flight(
     Flight_number int primary key,
     Flight_name varchar(15),
     Flight_st_point varchar(15),
     Flight_end_point varchar(15),
     Flight_date date,
     Flight_time time
);

CREATE TABLE Filght_ceats(
	Flight_number int primary key,
    Flight_busines tinyint,
    Flight_first   tinyint,
    Flight_economy tinyint
);

CREATE TABLE Booking_conform(
    User_mob   varchar(10) unique,
    Flight_number int primary key,
    Total_ceats tinyint ,
    Booked_ceats int4
);