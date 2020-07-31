from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class buyticket(FlaskForm):
    FlightNo = StringField('航班号:', validators=[DataRequired()])
    DeptDate = StringField('出发日期:', validators=[DataRequired()])
    ID_PassportNo = StringField('身份证号/PassportNo.:', validators=[DataRequired()])
    submit = SubmitField('submit', validators=[DataRequired()])


class deleteflights(FlaskForm):
    FlightNo = StringField('航班号:', validators=[DataRequired()])
    submit = SubmitField('submit', validators=[DataRequired()])

class addflights(FlaskForm):
    AirlineCode = StringField('航空公司编号:', validators=[DataRequired()])
    DeptAirport = StringField('出发机场编号:', validators=[DataRequired()])
    ArriveAirport = StringField('到达机场编号:', validators=[DataRequired()])
    FlightNo = StringField('航班号:', validators=[DataRequired()])
    submit = SubmitField('submit', validators=[DataRequired()])


class Timetable(FlaskForm):
    FlightNo = StringField('航班号:', validators=[DataRequired()])
    DeptDate = StringField('出发日期:', validators=[DataRequired()])
    DeptTime = StringField('起飞时间:', validators=[DataRequired()])
    ArvTime = StringField('到达时间:', validators=[DataRequired()])
    Seats_total = StringField('总座位数:', validators=[DataRequired()])
    submit = SubmitField('submit', validators=[DataRequired()])


class SelectTicket(FlaskForm):
    DeptDate=StringField('出发日期:', validators=[DataRequired()])
    DeptAirport = StringField('出发地:', validators=[DataRequired()])
    ArvAirport = StringField('目的地:', validators=[DataRequired()])
    submit = SubmitField('submit', validators=[DataRequired()])


class Passenger(FlaskForm):
    Nationality = StringField('Nationality:', validators=[DataRequired()])
    EnName = StringField('English Name:', validators=[DataRequired()])
    Tel = StringField('Tel:', validators=[DataRequired()])


class CN(FlaskForm):
    Nationality = StringField('Nationality:', validators=[DataRequired()])
    EnName = StringField('English Name:', validators=[DataRequired()])
    Tel = StringField('Tel:', validators=[DataRequired()])
    ID = StringField('ID:', validators=[DataRequired()])
    CNName = StringField('Chinese Name:', validators=[DataRequired()])
    Ethnic = StringField('Ethnic:', validators=[DataRequired()])
    submit = SubmitField('Submit')


class FR(FlaskForm):
    Nationality = StringField('Nationality:', validators=[DataRequired()])
    EnName = StringField('English Name:', validators=[DataRequired()])
    Tel = StringField('Tel:', validators=[DataRequired()])
    PassportNo = StringField('PassportNo.:', validators=[DataRequired()])
    VisaNo = StringField('VisaNo.:')
    submit = SubmitField('Submit')



