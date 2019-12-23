from sqlalchemy import *
from local.local_settings import *


class DbDriver:
    def __init__(self):
        self.db_string = 'db2+ibm_db://{}:{}@{}:{}/{}'.format(username, password, hostname, port, db_alias)
        db2 = create_engine(self.db_string)
        self.metadata = MetaData()
        self.conn = db2.connect()

    def get_table_cols(self, schema, table):
        dict_of_cols = {}

        created_table = Table(
            'SYSCOLUMNS', self.metadata,
            Column('NAME', String),
            Column('TBNAME', String),
            Column('TBCREATOR', String),
            Column('COLTYPE', String),
            extend_existing =True,
            schema='SYSIBM')

        s = created_table.select().where(created_table.c.TBCREATOR == schema).where(created_table.c.TBNAME == table)

        result = self.conn.execute(s)

        for entry in result:
            dict_of_cols[entry[0]] = Column(entry[0])

        return dict_of_cols

    def get_all_from_table(self, schema, table):
        all_cols = self.get_table_cols(schema, table)

        created_table = Table(
            table,
            self.metadata,
            extend_existing=True,
            schema=schema)

        for entry in all_cols:
            created_table.append_column(all_cols[entry])

        query = created_table.select()
        result = self.conn.execute(query)

        return result

    def create_table(self, schema, table):
        return Table(
            table,
            self.metadata,
            extend_existing=True,
            schema=schema)

    def set_schema(self, schema):
        return self.conn.execute('set schema {}'.format(schema))
