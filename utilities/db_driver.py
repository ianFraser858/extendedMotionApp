from sqlalchemy import *
from local.local_settings import *


class DbDriver:
    def __init__(self):
        self.db_string = 'db2+ibm_db://{}:{}@{}:{}/{}'.format(username, password, hostname, port, db_alias)
        db2 = create_engine(self.db_string)
        self.metadata = MetaData()
        self.conn = db2.connect()

        def get_table_cols(self):
            set_schema('SYSIBM')

            table = Table(
                'SYSCOLUMNS', db2.metadata,
                Column('NAME', String),
                Column('TBNAME', String),
                Column('TBCREATOR', String),
                Column('COLTYPE', String))

            print('add code here')

        def set_schema(self, schema):
            return self.conn.execute('set schema {}'.format(schema))
