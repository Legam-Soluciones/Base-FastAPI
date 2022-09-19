from fastapi import FastAPI
from sqlmodel import Field, SQLModel, create_engine
from sqlalchemy import create_engine, MetaData, Table

app = FastAPI()

@app.get("/alumnos/{id_alumno}")
async def root(id_alumno):

    sql_url = 'mssql+pymssql://preset:Adm1np3set19@mattilda-prod.database.windows.net/mattilda-prod'
    print(id_alumno)
    engine = create_engine(sql_url)
    
    result = engine.execute(f'select * from t_alumno where IDAlumno = {id_alumno}')
    obj = {}
    for row in result:
        print(row)
        obj = {
            "name": row[2],
            "last_name": row[3]
        }
    result.close()

    return obj

#======================================================================================================

@app.get("/alumnos_by_name/{nombre}")
async def root(nombre):

    sql_url = 'mssql+pymssql://preset:Adm1np3set19@mattilda-prod.database.windows.net/mattilda-prod'
    print(nombre)
    engine = create_engine(sql_url)
    
    result = engine.execute(f'select * from t_alumno where Nombre = \'{nombre}\'') 
    obj = {}
    for row in result:
        print(row)
        obj = {
            "name": row[2],
            "last_name": row[3]
        }
    result.close()

    return obj
















#======================================================================================================

@app.get("/responsable/{id_responsable}")
async def root(id_responsable):

    sql_url = 'mssql+pymssql://preset:Adm1np3set19@mattilda-prod.database.windows.net/mattilda-prod'
    print(id_responsable)
    engine = create_engine(sql_url)
    
    result = engine.execute(f'select * from t_responsable where IDResponsable = {id_responsable}')
    obj = {}
    for row in result:
        print(row)
        obj = {
            "name": row[2],
            "last_name": row[3]
        }
    result.close()

    return obj

#======================================================================================================

@app.get("/colegios/{id_colegios}")
async def root(id_colegios):

    sql_url = 'mssql+pymssql://preset:Adm1np3set19@mattilda-prod.database.windows.net/mattilda-prod'
    print(id_colegios)
    engine = create_engine(sql_url)
    
    result = engine.execute(f'select * from cat_colegios where IDColegio = {id_colegios}')
    obj = {}
    for row in result:
        print(row)
        obj = {
            "name": row[2],
            "last_name": row[3]
        }
    result.close()

    return obj





    return {"message": "Hello"}

@app.get("/hello/{name}")
async def say_Hello(name:str ):
    return {"message": f"Hello {name}"}

