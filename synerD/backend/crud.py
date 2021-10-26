from django.conf import settings
settings.configure(
    DATABASE_ENGINE = 'postgresql_psycopg2',
    DATABASE_NAME = 'db_name',
    DATABASE_USER = 'db_user',
    DATABASE_PASSWORD = 'db_pass',
    DATABASE_HOST = 'localhost',
    DATABASE_PORT = '5432',
    TIME_ZONE = 'America/New_York',
)
from synerD.models import *

if __name__ =='__main__':
    user = UserInfo(username='test')
    user.save()