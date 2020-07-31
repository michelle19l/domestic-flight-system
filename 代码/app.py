from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from classes import *
from sql_func import *

nav = Nav()
nav.register_element('top', Navbar(
    u'航班购票系统',
    View(u'主页', 'index'),
    Subgroup(u'航班修改',
             View(u'航班添加', 'addFlights'),
             Separator(),
             View(u'航班删除', 'deleteFlights')),
    View(u'班次修改', 'UpdateTimetable'),
    View(u'航班查询', 'SelectTickets'),
    Subgroup(u'填写个人信息',
             View(u'中国籍', 'Add_CN'),  # 第二对引号内为函数命
             Separator(),
             View(u'非中国籍', 'Add_FR')),
    View(u'购票', 'BuyTickets')
))

app = Flask(__name__)
app.secret_key = '1234567'
Bootstrap(app)
nav.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/addFlights/', methods=['Get', 'Post'])
def addFlights():
    form = addflights()
    if form.validate_on_submit():
        AirlineCode = form.data['AirlineCode']
        DeptAirport = form.data['DeptAirport']
        ArriveAirport = form.data['ArriveAirport']
        FlightNo = form.data['FlightNo']
        temp = add_flight(AirlineCode, DeptAirport, ArriveAirport, FlightNo)
        return temp
    return render_template('form.html', form=form)


@app.route('/deleteFlights/', methods=['Get', 'Post'])
def deleteFlights():
    form = deleteflights()
    if form.validate_on_submit():
        FlightNo = form.data['FlightNo']
        temp = delete_flight(FlightNo)
        return temp
    return render_template('form.html', form=form)


@app.route('/UpdateTimetable/', methods=['Get', 'Post'])
def UpdateTimetable():
    form = Timetable()
    if form.validate_on_submit():
        FlightNo = form.data['FlightNo']
        DeptDate = form.data['DeptDate']
        DeptTime = form.data['DeptTime']
        ArvTime = form.data['ArvTime']
        Seats_total = form.data['Seats_total']
        Seats_cur=Seats_total
        temp = add_timetable(FlightNo, DeptDate, DeptTime, ArvTime, Seats_total, Seats_cur)
        return temp
    return render_template('form.html', form=form)


@app.route('/BuyTickets/', methods=['Get','Post'])
def BuyTickets():
    form = buyticket()
    if form.validate_on_submit():
        FlightNo = form.data['FlightNo']
        DeptDate = form.data['DeptDate']
        ID_PassportNo = form.data['ID_PassportNo']
        temp = buy(FlightNo,DeptDate,ID_PassportNo)
        return temp
    return render_template('form.html', form=form)


@app.route('/SelectTickets/', methods=['Get', 'Post'])
def SelectTickets():
    form = SelectTicket()
    if form.validate_on_submit():
        DeptDate = form.data['DeptDate']
        DeptAirport = form.data['DeptAirport']
        ArvAirport = form.data['ArvAirport']
        temp = select_flights(DeptDate, DeptAirport, ArvAirport)
        return temp
    return render_template('form.html', form=form)


@app.route('/AddCN/', methods=['Get', 'Post'])
def Add_CN():
    form = CN()
    if form.validate_on_submit():
        EnName = form.data['EnName']
        CNName = form.data['CNName']
        Nationality = form.data['Nationality']
        Tel = form.data['Tel']
        ID = form.data['ID']
        Ethnic = form.data['Ethnic']
        return add_CN(EnName, CNName, Nationality, Tel, ID, Ethnic)
    return render_template('form.html', form=form)


@app.route('/AddFR/', methods=['Get', 'Post'])
def Add_FR():
    form = FR()
    if form.validate_on_submit():
        EnName = form.data['EnName']
        Nationality = form.data['Nationality']
        Tel = form.data['Tel']
        PassportNo = form.data['PassportNo']
        VisaNo = form.data['VisaNo']
        return add_FR(EnName, Nationality, Tel, PassportNo, VisaNo)
    return render_template('form.html', form=form)



if __name__ == '__main__':
    app.run()
