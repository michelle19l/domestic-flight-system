drop procedure if exists buyT ;
create procedure buyT (FlightNo_ char(5), DeptDate_ integer,ID_PassportNo_ varchar(30))
    begin
        declare seat char(5);
        set seat=(select seats_current from timetable
            where flightno=FlightNo_ and deptdate=DeptDate_);
        insert into ticket(flightno,deptdate,seat,id_passportno)
            values(FlightNo_,DeptDate_,seat,ID_PassportNo_);
        set seat=seat-1;
        update timetable
        set seats_current=seat
            where flightno=FlightNo_ and deptdate=DeptDate_;
    end;


drop procedure if exists information_updating_fr;
create procedure information_updating_fr(enname_ varchar(50),nationality_ varchar(20),tel_ bigint(11),
id_passportno_ varchar(50),visano_ varchar(100))
    begin
        if nationality_='中国' then
            signal sqlstate 'HY000' set message_text='国籍填写错误，中国籍人士请到Chinese板块填写';
        end if;
        if exists (select * from passenger where id_passportno=id_passportno_) then
            update passenger set tel=tel_ where id_passportno=id_passportno_;
            update passenger set nationality=nationality_ where id_passportno=id_passportno_;
            update passenger set enname=enname_ where id_passportno=id_passportno_;

        else insert into passenger(id_passportno,tel,nationality,enname)
                values (id_passportno_,tel_,nationality_,enname_);
        end if;
        if exists (select * from foreigner where id_passportno=id_passportno_) then
                update foreigner set visano=visano_ where id_passportno=id_passportno_;
            else insert into foreigner(id_passportno,visano)
                values(id_passportno_,visano_);
        end if;
    end;

drop procedure if exists delete_flight;
create procedure delete_flight(flightno_ char(7))
    begin
        if exists(select * from ticket where flightno=flightno_) then
            signal sqlstate 'HY000' set message_text='请先退回机票';
            else delete from flight where flightno=flightno_;
        end if;
    end;



drop procedure if exists information_updating_cn;
create procedure information_updating_cn(enname_ varchar(50),cnname_ varchar(20),nationality_ varchar(20),
tel_ bigint(11),id_passportno_ varchar(50),ethnic_ char(5))
    begin
        if nationality_<>'中国' then
            signal sqlstate 'HY000' set message_text='国籍填写错误，非中国籍人士请到foreigner板块填写';
        end if;
        if exists (select * from passenger where id_passportno=id_passportno_) then
            update passenger set tel=tel_ where id_passportno=id_passportno_;
            update passenger set nationality=nationality_ where id_passportno=id_passportno_;
            update passenger set enname=enname_ where id_passportno=id_passportno_;
        else insert into passenger(id_passportno,tel,nationality,enname)
                values (id_passportno_,tel_,nationality_,enname_);
        end if;
        if exists (select * from chinese where id_passportno=id_passportno_) then
                update chinese set cnname=cnname_ where id_passportno=id_passportno_;
                update chinese set ethnic=ethnic_ where id_passportno=id_passportno_;
            else insert into chinese(id_passportno,cnname,ethnic)
                values(id_passportno_,cnname_,ethnic_);
        end if;
    end;