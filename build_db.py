import os
from sqlalchemy import create_engine, schema

from data_model import Base

UID = os.environ["POSTGRES_USER"]
PWD = os.environ["POSTGRES_PASSWORD"]
DBNAME = os.environ["POSTGRES_DB"]

engine = create_engine(f"postgresql+psycopg2://{UID}:{PWD}@opencdms-database:5432/{DBNAME}")

Base.metadata.bind = engine

schemas = {v.schema for k, v in Base.metadata.tables.items()}
# for _schema in schemas:
#     # if not engine.dialect.has_schema(engine, _schema):
#     engine.execute(schema.CreateSchema(_schema))

Base.metadata.create_all(engine)
