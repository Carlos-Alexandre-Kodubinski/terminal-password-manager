create database pwd_manager
default character set utf8
default collate utf8_general_ci ;

create table accounts (
    id tinyint not null auto_increment,
    name_site varchar(20) not null,
    email varchar(30) not null,
    name_user varchar(20) not null,
    pwd varchar(15) not null, 
    primary key (id) 
) default charset = utf8;

