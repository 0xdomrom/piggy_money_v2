import sqlalchemy

from sqlalchemy import create_engine, Column, String,\
                        Integer, ForeignKey

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///piggy.db",echo=True)
Base = declarative_base()



class Users(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    def repr(self):
        return None


class Accounts(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    owner = Column(ForeignKey('users.username'))
    balance = Column(Integer, nullable=False)


class Transactions(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    from_acc = Column(ForeignKey('accounts.id'))
    to_acc = Column(ForeignKey('accounts.id'))
    amount = Column(Integer, nullable=False)

# create tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
# create session
Session = sessionmaker(bind=engine)
dbsession = Session()


user_data = [
    {"username":'Bob',"password":'Bob'},
    {"username":'Alice',"password":'Alice'}
]
account_data = [
    {"owner":'Bob','balance':1000},
    {"owner":'Bob','balance':2000},
    {"owner":'Bob','balance':-3000},
    {"owner":'Alice','balance':-1000},
    {"owner":'Alice','balance':-2000},
    {"owner":'Alice','balance':3000},
]
try:
    for user in user_data:
        row = Users(**user)
        dbsession.add(row)
    for account in account_data:
        row = Accounts(**account)
        dbsession.add(row)
    dbsession.commit()
except SQLAlchemyError as e:
    print(e)



