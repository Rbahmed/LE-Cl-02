CREATE TABLE passengers (id SERIAL PRIMARY KEY, origin VARCHAR NOT NULL, destination VARCHAR NOT NULL, duration INTEGER NOT NULL);

INSERT INTO flights(origin,destination,duration) VALUES ('New Yeark','London',456);
INSERT INTO flights(origin,destination,duration) VALUES ('Dothan','Eufaula',847);
INSERT INTO flights(origin,destination,duration) VALUES ('Florence','London',356);
INSERT INTO flights(origin,destination,duration) VALUES ('Fort Payne','Huntsville',748);
INSERT INTO flights(origin,destination,duration) VALUES ('Gadsden','Ozark',567);
INSERT INTO flights(origin,destination,duration) VALUES ('Greenville','Scottsboro',965);
INSERT INTO flights(origin,destination,duration) VALUES ('Guntersville','Arizona',543);



INSERT INTO passengers(passenger_name,flight_id) VALUES ('A',3);
INSERT INTO passengers(passenger_name,flight_id) VALUES ('B',5);
INSERT INTO passengers(passenger_name,flight_id) VALUES ('C',7);
INSERT INTO passengers(passenger_name,flight_id) VALUES ('D',2);
INSERT INTO passengers(passenger_name,flight_id) VALUES ('E',4);
INSERT INTO passengers(passenger_name,flight_id) VALUES ('F',6);
INSERT INTO passengers(passenger_name,flight_id) VALUES ('G',8);
