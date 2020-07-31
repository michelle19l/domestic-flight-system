drop trigger if exists buy_add;
delimiter //
create trigger buy_add
before insert on ticket for each row
begin
    declare seat smallint(4);
    set seat=(select seats_current from timetable
                where flightno=new.flightno
                and deptdate=new.deptdate);
    if seat<1 then
        signal sqlstate 'HY000' set message_text='该班次机票已售罄';
    end if;
    if new.id_passportno not in (select id_passportno from passenger
                                where id_passportno=new.id_passportno )
     then
        signal sqlstate 'HY000' set message_text='请先填写个人信息';
    end if;
end;//
delimiter ;

