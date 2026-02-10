-- 1. Enable Checkpointing (CRITICAL for Iceberg commits)
set 'execution.checkpointing.interval'
= '3s'
;

show databases
;

-- 2. Create Table
create table messages (
    id int,
    chat_id int,
    chat_title string,
    sender_id string,
    sender_username string,
    text string,
    `timestamp` timestamp(0),
    primary key (id) not enforced
) with (
    'connector' = 'mysql-cdc',
    'hostname' = 'plutus_db',
    'port' = '3306',
    'username' = 'plutus',
    'password' = 'plutus',
    'database-name' = 'plutus',
    'table-name' = 'messages'
    -- ,
    -- 'server-time-zone' = 'utc'
);

-- 3. Select Data from MySQL
select *
from messages
;

--- -----------------------
-- Insert Data into Iceberg
--- -----------------------
-- 1. Create the Catalog
create catalog iceberg with (
    'type' = 'iceberg',
    'catalog-type' = 'hadoop',
    'warehouse' = 's3a://data-bucket/warehouse'
);

-- 2. Create Namespace(Database) in MinIO
create database if not exists iceberg.dl;

-- 3. Create the Iceberg Sink Table
create table if not exists iceberg.dl.messages (
    id int,
    chat_id int,
    chat_title string,
    sender_id string,
    sender_username string,
    text string,
    `timestamp` timestamp(0),
    primary key (id) not enforced
);

-- 4. Submit the Streaming Job
insert into iceberg.dl.messages
select * from messages;

-- 5. Select Table
select * from iceberg.dl.messages;