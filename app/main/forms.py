#-*- coding:utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import Required

class TicketForm(Form):
    date = DateField('出发日期', validators=[Required()])
    from_station = StringField('出发站点：', validators=[Required()])
    to_station = StringField('目的站点：', validators=[Required()])
