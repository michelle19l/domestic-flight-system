import pymysql
import traceback
from flask import render_template


def add_flight(AirlineCode, DeptAirport, ArvAirport, FlightNo):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="mysql",
        database="Domestic_Flight",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = "insert into flight(flightno,dept_airport,arv_airport,code) VALUES (%s, %s, %s,%s );"
    str_ = ''
    try:
        # 执行SQL语句
        cursor.execute(sql, [FlightNo, DeptAirport, ArvAirport, AirlineCode])
        # 提交事务
        conn.commit()

        str_ = 'Success'
    except Exception as e:
        # 有异常，回滚事务
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        conn.rollback()
        str_ = str(e)

    cursor.close()
    conn.close()
    return str_


def add_timetable(FlightNo, DeptDate, DeptTime, ArvTime, Seats_total,Seats_cur):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="mysql",
        database="Domestic_Flight",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = "insert into timetable(FlightNo,DeptDate,DeptTime,ArvTime,Seats_total,Seats_current) VALUES (%s,%s, %s, %s,%s,%s );"
    str_ = ''
    try:
        # 执行SQL语句
        cursor.execute(sql, [FlightNo, DeptDate, DeptTime, ArvTime, Seats_total, Seats_cur])
        # 提交事务
        conn.commit()
        print("Success")
        str_ = 'Success'
    except Exception as e:
        # 有异常，回滚事务
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        conn.rollback()
        str_ = str(e)

    cursor.close()
    conn.close()
    return str_


def select_flights(DeptDate, DeptAirport, ArvAirport):  # 查timetable
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="mysql",
        database="Domestic_Flight",
        charset="utf8mb4"
    )
    cursor = conn.cursor()

    sql = "select *\
            from search_tickets\
            where deptdate=%s and dept=%s and arv=%s;"
    try:

        cursor.execute(sql, [DeptDate, DeptAirport, ArvAirport])
        rs = cursor.fetchall()
        return render_template('selectform.html', rs=rs)  # 返回表格
    except Exception as e:
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        conn.rollback()
        str_ = str(e)
        return str_


def add_CN(EnName, CNName, Nationality, Tel, ID, Ethnic):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="mysql",
        database="Domestic_Flight",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = "call information_updating_cn(%s,%s,%s,%s,%s,%s);"
    str_ = ''
    try:
        cursor.execute(sql, [EnName, CNName, Nationality, Tel, ID, Ethnic])
        conn.commit()
        str_ = 'Success'
    except Exception as e:
        # 有异常，回滚事务
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        conn.rollback()
        str_ = str(e)
    cursor.close()
    conn.close()
    return str_


def add_FR(EnName, Nationality, Tel, PassportNo, VisaNo):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="mysql",
        database="Domestic_Flight",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = "call information_updating_fr(%s,%s,%s,%s,%s);"
    str_ = ''
    try:
        # 执行SQL语句
        cursor.execute(sql, [EnName, Nationality, Tel, PassportNo, VisaNo])
        # 提交事务
        conn.commit()
        str_ = 'Success'
    except Exception as e:
        # 有异常，回滚事务
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        conn.rollback()
        str_ = str(e)

    cursor.close()
    conn.close()
    return str_



def delete_flight(FlightNo):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="mysql",
        database="Domestic_Flight",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = "call delete_flight(%s);"
    try:
        cursor.execute(sql, FlightNo)
        # 运行成功，提交事务
        conn.commit()
        str_ = 'Success'

    except Exception as e:
        # 有异常，回滚事务
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        conn.rollback()
        str_ = str(e)

    cursor.close()
    conn.close()
    return str_


def buy(FlightNo,DeptDate,ID_PassportNo):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="mysql",
        database="Domestic_Flight",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = "call buyT(%s,%s,%s);"
    try:
        cursor.execute(sql, [FlightNo,DeptDate,ID_PassportNo])
        conn.commit()
        str_ = 'Success'

    except Exception as e:
        # 有异常，回滚事务
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        conn.rollback()
        str_ = str(e)
    cursor.close()
    conn.close()
    return str_