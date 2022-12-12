""" Module represents a User. """

from sqlalchemy import (
    Column, String, Integer,
    DateTime, Date, Boolean,
    ForeignKey
)

from sqlalchemy import (
    Column, String, Integer, DateTime, Date, Boolean, DECIMAL, ForeignKey, Text
)
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship, backref

from application.database import db
from application.database.model import CommonModel, default_uuid


class User(CommonModel):
    __tablename__ = 'users'

    id = db.Column(Integer, autoincrement=True, primary_key=True)

    # Authentication Attributes.
    email = db.Column(String(255), nullable=False)
    name = db.Column(String(255), nullable=False)
    token_expires = db.Column(DateTime, nullable=True)
    perishable_token = db.Column(String(255), nullable=True, unique=True)

    # Personal Attributes.
    birthday = db.Column(Date, nullable=True)
    first_name = db.Column(String(35), nullable=True)
    last_name = db.Column(String(35), nullable=True)

    # Permission Based Attributes.
    is_active = db.Column(Boolean, default=False)

    # Methods
    def __repr__(self):
        """ Show user object info. """
        return '<User: {}>'.format(self.id)

    def full_name(self):
        """ Return users full name. """
        return '{} {}'.format(self.first_name, self.last_name)

    def formatted_birthday(self):
        """ Return birthday date in a understandable format. """
        return self.birthday.strftime('%m/%d/%Y')
    

class QuocGia(CommonModel):
    __tablename__ = 'quocgia'
    id = db.Column(Integer, primary_key=True)
    ma = db.Column(String(255), unique=True)
    ten = db.Column(String(255), nullable=False)
    mota = db.Column(String(255), nullable=True)
    tinhthanh = db.relationship("TinhThanh", order_by="TinhThanh.id", cascade="all, delete-orphan")
    
class TinhThanh(CommonModel):
    __tablename__ = 'tinhthanh'
    id = db.Column(Integer, primary_key=True)
    ma = db.Column(String(255), unique=True)
    ten = db.Column(String(255), nullable=False)
    quocgia_id = db.Column(Integer, ForeignKey('quocgia.id'), nullable=False)
    quocgia = db.relationship('QuocGia')
