import sqlalchemy
from django.conf import settings


def dbe():
    return sqlalchemy.create_engine(settings.DB_CONNECTION_URL)

def dbsess():
    Session = sqlalchemy.orm.sessionmaker(bind=dbe())
    return Session()
