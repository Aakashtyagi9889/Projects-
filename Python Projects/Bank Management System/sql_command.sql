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




