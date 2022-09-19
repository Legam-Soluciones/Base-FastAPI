from unittest import result
from sqlmodel import Field, SQLModel, create_engine
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper
from sqlalchemy.sql import select

class MyTable(object):
    pass

sql_url = 'mssql+pymssql://preset:Admlnp3set19@mattilda-prod.database.windows.net/mattilda-prod'

engine = create_engine(sql_url, echo=True)

metadata = MetaData(engine)
my_table_instance = Table('MyTable', metadata, autoload=True)
mapper(MyTable, my_table_instance)

conn = engine.connect()
s = select([MyTable.ColumnName]).where(MyTable.ID == 802)
res = conn.execute(s)
row = res.fetchone()
res = None if row is None else row['ColumnName']
    
print(res)





