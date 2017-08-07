
from piggy_money_v2.db.dbmodel import Users, Accounts, Session, Transactions


def get_user_pass(username):
    dbsession = Session()
    user_pass_query = dbsession.query(Users.password).filter(Users.username==username)
    dbsession.close()
    return user_pass_query.all()

def get_user_accounts(username):
    dbsession = Session()
    user_acc_query = dbsession.query(Accounts.id, Accounts.balance).filter(Accounts.owner==username)
    dbsession.close()
    return user_acc_query.all()

if __name__=="__main__":
    print(get_user_pass('Bob'))
    print(get_user_accounts('Bob'))
