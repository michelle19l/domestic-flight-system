drop view if exists search_tickets;
create view search_tickets
    as
    select airlinename,t1.flightno as flightno,t1.deptdate as deptdate,
            depttime,arvtime,seats_current,dept,arv
    from
    (select airlinename,flightno,deptdate,depttime,arvtime,seats_current,
            airportname as dept
    from timetable natural join flight natural join airline left outer join
            airport on flight.dept_airport=airport.airportno) as t1
    left outer join
    (
    select flightno,deptdate,airportname as arv
    from timetable natural join flight natural join airline left outer join
            airport on flight.arv_airport=airport.airportno
    ) as t2
    on t1.flightno=t2.flightno and t1.deptdate=t2.deptdate
