print('hello_p')

#import pandas as pd
#import sqlalchemy



from sqlalchemy import MetaData, Table
import _sqlite3
from sqlalchemy import create_engine
engine = create_engine('sqlite:///data_proj_1')
#metadata.create_all(engine)

#from sqlalchemy import (Table, Column, String, Integer, Boolean)
#employees = Table('employees', metadata,
#Column('id', Integer()),
#Column('name', String(255)),
#Column('active', Boolean()))

#engine.table_names()
print(engine.table_names())
from sqlalchemy import MetaData, Table
metadata = MetaData()
census = Table('tbl1', metadata, autoload=True,
autoload_with=engine)
print(repr(census))


