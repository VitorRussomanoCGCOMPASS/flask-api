from sqlalchemy.engine import URL, create_engine


connect_url = URL.create(
    'mssql+pyodbc',
    username='Vitor.ibanez@cgcompass.com',
    password='Changepass*23',
    host='tcp:cg-lz-core-db-sql001.public.568a9b46c7aa.database.windows.net,3342',
    database='DB_Brasil',
    query=dict(driver='ODBC Driver 17 for SQL Server',authentication= 'ActiveDirectoryPassword'))


engine = create_engine(connect_url) 


TempProcessingIMA.__table__.create(engine)