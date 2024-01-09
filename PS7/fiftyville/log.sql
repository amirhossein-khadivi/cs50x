-- Keep a log of any SQL queries you execute as you solve the mystery.
select name, transcript from interviews where year = 2021 and month = 7 and day = 28;

select name, atm_transactions.amount from people
       join atm_transactions on bank_accounts.account_number = atm_transactions.account_number
       join bank_accounts on people.id = bank_accounts.person_id
       where atm_transactions.transaction_type = 'withdraw'
       and atm_transactions.atm_location = 'Leggett Street'
       and atm_transactions.year = 2021
       and atm_transactions.month = 7
       and atm_transactions.day = 28;

select abbreviation, full_name, city from airports where city = 'Fiftyville';

select flights.id, full_name, city, flights.hour, flights.minute from airports
       join flights on airports.id = flights.destination_airport_id
       where flights.day = 29
       and flights.month = 7
       and flights.year = 2021
       and flights.origin_airport_id = (select id from airports where city = 'Fiftyville')
       order by flights.hour, flights.minute;



select passengers.flight_id, name, passengers.seat, passengers.passport_number from people
       join flights on passengers.flight_id = flights.id
       join passengers on people .passport_number = passengers.passport_number
       where flights.year = 2021
       and flights.month = 7
       and flights.day = 29
       and flights.hour = 8
       and flights.minute = 20
       order by passengers.passport_number;

select name, bakery_security_logs.hour, bakery_security_logs.minute from people
       join bakery_security_logs on people.license_plate = bakery_security_logs.license_plate
       where bakery_security_logs.activity = 'exit'
       and bakery_security_logs.minute <= 25
       and bakery_security_logs.minute >= 15
       and bakery_security_logs.year = 2021
       and bakery_security_logs.month = 7
       and bakery_security_logs.day = 28
       order by bakery_security_logs.minute;



create table a as
              select name, phone_calls.duration from people
                     join phone_calls on people.phone_number = phone_calls.receiver
                     where phone_calls.duration <= 60
                     and phone_calls.year = 2021
                     and phone_calls.month = 7
                     and phone_calls.day = 28
                     order by phone_calls.duration;
select * from a;


create table b as
              select name, phone_calls.duration from people
                     join phone_calls on people.phone_number = phone_calls.caller
                     where phone_calls.duration <= 60
                     and phone_calls.year = 2021
                     and phone_calls.month = 7
                     and phone_calls.day = 28
                     order by phone_calls.duration;


select a.name, b.name, a.duration from a inner join b on a.duration = b.duration;