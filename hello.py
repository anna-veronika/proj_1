print('hello_p')


import sqlalchemy as db
from sqlalchemy import MetaData
from sqlalchemy import insert
from sqlalchemy import (Table, Column, String, Integer)
from sqlalchemy.sql import select

engine = db.create_engine('sqlite:///data.db')
connection = engine.connect()

metadata = MetaData()


seq_data = Table('seq_data', metadata,
Column('seq_id', Integer()),
Column('seq', String(255)),
Column('gen_name', String(255)))
metadata.create_all(engine)

print(engine.table_names())
print(seq_data.columns.keys())

stmt = insert(seq_data)
values_list = [
    {'seq_id': 2, 'seq': 'ATCCGTTA', 'gen_name': 'sil_colf'},
    {'seq_id': 3, 'seq': 'GTAATGCT', 'gen_name': 'soolg_a'},
    {'seq_id': 1, 'seq': 'GTAATGTGCT', 'gen_name': 'soolg_b'},
    {'seq_id': 4, 'seq': 'GTAATGCT', 'gen_name': 'gengl'}
    ]
result_proxy = connection.execute(stmt, values_list)
print(result_proxy.rowcount)

stmt = select([seq_data])
results = connection.execute(stmt).fetchall()
print(results)

stmt = select([seq_data]).where(seq_data.columns.seq_id == '1')
# Print the result of executing the query.
print(connection.execute(stmt).first())

