select Database();
use bankmanagementsystem;

create database if not exists BankManagementSystem;
CREATE TABLE account_holder(
acc_no INT Primary key AUTO_INCREMENT,
aname Varchar(100) NOT NULL,
aemail Varchar(100) NOT NULL,
amob Varchar(100) NOT NULL,
agender Varchar(100) NOT NULL,
aadd Varchar(100) NOT NULL,
atype Varchar(100) NOT NULL,
abalance DECIMAL (15,2),
active_status INT DEFAULT 1
);

Select * from account_holder;

Update  account_holder 
set acc_no = 32318128;


Create Table transactions(
tid INT PRIMARY KEY AUTO_INCREMENT,
acc_no INT , 
a_name Varchar(100),
a_type varchar(100),
c_bal Decimal(10,2),
d_bal Decimal(10,2),
a_balance Decimal(12,2),
time_ timestamp default current_timestamp
)

DELIMITER //
CREATE TRIGGER ins_acc
AFTER INSERT ON account_holder
FOR EACH ROW
BEGIN
	INSERT INTO transactions(acc_no , a_name , a_type , c_bal , d_bal , a_balance)
    VALUE(NEW.accno , NEW.aname , NEW.atype , 0 , 0 , NEW.abalance);
END // DELIMITER;

select * from transactions;
