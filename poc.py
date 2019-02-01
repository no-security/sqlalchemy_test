#coding=utf-8
import sys
from sqlalchemy import create_engine, String
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import joinedload, subqueryload

# 建立连接
engine = create_engine('mysql://root:123456@127.0.0.1:3306/test?charset=utf8', echo=True)

# 建立会话
session = Session(engine)

# 声明基类
Base = declarative_base()


class Sql_test(Base):
    __tablename__ = 'sql_test'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255)),
    des = Column(String(255))

print(session.query(Sql_test).group_by(sys.argv[1]).all())














