# Terminal
####
# $ sqlite3 ydb.db
# sqlite >.tables
# sqlite >.exit
# $ ls
####


#import pandas as pd
#import sqlalchemy



from sqlalchemy import MetaData, Table
import _sqlite3
#from sqlalchemy import create_engine
#engine = create_engine('sqlite:///data_proj_1')


#metadata = db.MetaData()
#census = db.Table('employees', metadata, autoload=True, autoload_with=engine)
#query = db.select([census])
#ResultProxy = connection.execute(query)


from sqlalchemy import MetaData, Table
metadata = MetaData()
census = Table('tbl1', metadata, autoload=True, autoload_with=engine)
print(repr(census))


from sqlalchemy import (Table, Column, String, Integer, Boolean)
employees = Table('employees', metadata,
Column('id', Integer()),
Column('name', String(255)),
Column('active', Boolean()))
metadata.create_all(engine)

from sqlalchemy import (Table, Column, String, Integer, Boolean)
seq_data = Table('seq_data', metadata,
Column('seq_id', Integer()),
Column('seq', String(255)),
Column('gen_name', String(255)))
metadata.create_all(engine)


print(engine.table_names())

from sqlalchemy import insert
stmt = insert(employees).values(id=1, name='Jason', active=True)
result_proxy = connection.execute(stmt)
print(result_proxy.rowcount)

print(employees.columns.keys())
print(employees.columns.values())
print(seq_data.columns.keys())

stmt = insert(employees)
values_list = [
    {'id': 2, 'name': 'Rebecca', 'active': True},
    {'id': 3, 'name': 'Bob', 'active': False}
    ]
result_proxy = connection.execute(stmt, values_list)
print(result_proxy.rowcount)

#stmt = 'SELECT * FROM people'
from sqlalchemy.sql import select
stmt = select([employees])
results = connection.execute(stmt).fetchall()
print(results)

