create database pharmacy_db;
use pharmacy_db;

create table medicines(
medicine_id int auto_increment primary key, 
name varchar(100), 
price decimal(10,2), 
availability int default 1,
offer int default 0,
discounted_price decimal(10,2));

create table suppliers(
	supplier_id int auto_increment primary key,
    name varchar(100),
    contact_info varchar(255)
);

create table alternatives(
	alt_id int auto_increment primary key,
    org_medicine_id int,
    alt_medicine_id int,
    foreign key (org_medicine_id) references medicines(medicine_id),
    foreign key (alt_medicine_id) references medicines(medicine_id)
);

desc medicines;

delimiter //
create trigger calculate_discounted_price
before insert on medicines
for each row
begin
 if new.offer>0 then
	set new.discounted_price = new.price - (new.price * new.offer / 100);
 else
	set new.discounted_price = new.price;
 end if;
end; //
delimiter ;

insert into medicines (name, price, availability, offer) values
('Aspirin',20.50,1,10),
('Ibuprofen',15.75,1,0),
('Paracetamol',5.00,0,20);

insert into suppliers (name, contact_info) values
('Supplier A','1234 Street, City'),
('Supplier B','5678 Avenue, City'),
('Supplier C','7642 Shard, City');

insert into alternatives (org_medicine_id,alt_medicine_id) values
(1,2);

ALTER TABLE medicines
ADD quantity INT DEFAULT 0;

update medicines
set quantity = 120
where name = 'Aspirin';

update medicines
set quantity = 250
where name = 'Ibuprofen';

update medicines
set quantity = 150
where name = 'Paracetamol';

select * from medicines;


