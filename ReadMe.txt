1) open el CMD en modo Administrador 

2) estando ahi verificar la version de python
			C:\Windows\system32>python --version
			
2) intalar el poetry
			C:\Windows\system32>pip install poetry
			
3)crear una carpeta en el escritorio desde el CMD
			C:\Windows\system32>cd D:\legam\desktop
			C:\Windows\system32>d:
			D:\legam\desktop
			D:\legam\Desktop>mkdir base_api
			D:\legam\Desktop>cd base_api
			D:\legam\Desktop\base_api>dir
			
4)correr el poetry el el folder Base_APi
			D:\legam\Desktop\base_api>poetry init
			y dar [yes] a las preguntas
			
5)agregar las librerias
			D:\legam\Desktop\base_api>poetry add fastapi uvicorn sqlalchemy pymssql pyparsing fastapi-pagination[all]
			
6) realizar un update
			D:\legam\Desktop\base_api>poetry update
			
7)al terminar el update iniciamos el Visual Studio Code	
			D:\legam\Desktop\base_api>code .
			
8)en caso de error de sesiones favor correr desde la terminal de la consola de Visual Code
			PS D:\legam\Desktop\base_api> poetry add pymssql
			
9)cuando ya se tiene el desarrollo y se probara se corre el server unicor
			PS D:\legam\Desktop\base_api> poetry run uvicorn main:app --reload --port 9999
			
10)
			pip install tortoise-orm
			pip install python-multipart fastapi uvicorn pydantic
********************************************************************************************************************			

"ConnectionStrings": {
        "DefaultConnection": "Data Source=ANUBIS-INTEL64E;Initial Catalog=PELICULAS-APIv2;Integrated Security=True"
    },
	
	WepApiPeliculas2022v2
	
	¿Qué librerías tiene Python?
¿Cuáles son las mejores librerías de Python?

Matplotlib. Esta es una de las librerías de Python más usadas, pues su procesamiento y generador de gráficos son de amplia calidad.
Seaborn.
Bokeh.
NumPy.
SciPy.
Pandas.
Numba.
Scikit-Learn.
sqlalchemy.
FastAPI.

poetry add sqlmodel

pip install peewee    
pip install poetry
pip install "fastapi[all]"
pip install "uvicorn[standard]"
pip freeze
freeze 

requirements.txt

pip install virtualenv

python -m vent ent

d:/legam/Desktop/WebApiEstudiantes.Python/Banner-API/ent/Scripts/Activate.ps1

uvicorn scr/main:app --reload

python -m uvicorn main:app --reload -- 9999

Example

	{
        "id": 4,
        "nombre": "Terminator",
        "rutaImagen": "Test",
        "descripcion": "Test Descripcion",
        "duracion": "125",
        "clasificacion": 1,
        "categoriaId": 1,
        "categoria": null
{
    "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
    "title": "One or more validation errors occurred.",
    "status": 400,
    "traceId": "|34b91873-47a5cb2980250ef6.",
    "errors": {
        "Nombre": [
            "El campo nombre es obligatorio."
        ],
        "Duracion": [
            "El campo nombre es obligatorio"
        ],
        "Descripcion": [
            "El campo nombre es obligatorio"
        ]
    }
}

==================================================================================================
**************************************************************************************************
session.py
**************************************************************************************************

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

**************************************************************************************************

==================================================================================================

**************************************************************************************************
main.py
**************************************************************************************************
from fastapi import FastAPI
from sqlmodel import Field, SQLModel, create_engine
from sqlalchemy import create_engine, MetaData, Table

app = FastAPI()

#======================================================================================================

@app.get("/students/{id_alumno}")
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
            "pather_name": row[3],
            "mother_name": row[4],
            "curp": row[5],
            "level": row[7],
            "incorp": row[8],
            "college": row[9],
            "status": row[12],
            "registration_date": row[14]
        }
    result.close()

    return obj

#======================================================================================================

@app.get("/students_by_name/{nombre}")
async def root(nombre):

    sql_url = 'mssql+pymssql://preset:Adm1np3set19@mattilda-prod.database.windows.net/mattilda-prod'
    print(nombre)
    engine = create_engine(sql_url)
    
    result = engine.execute(f'select * from t_alumno where Nombre = \'{nombre}\'') 
    student_list = []
    for row in result:

        print(row)
        obj = {
            "idalumno": row[0],
            "name": row[2],
            "pather_name": row[3],
            "mother_name": row[4],
            "curp": row[5],
            "level": row[7],
            "incorp": row[8],
            "college": row[9],
            "status": row[12],
            "fecha_reg": row[14]
        }
        student_list.append(obj)
    result.close()

    return student_list

#======================================================================================================

@app.get("/responsible/{id_responsable}")
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
            "pather_name": row[3],
            "mother_name": row[4],
            "UIDCollege": row[1],
            "email": row[6],
            "phone": row[7],
            "idalumno": row[9],
            "status": row[10],
            "records": row[11],
            "activity": row[12]
        }
    result.close()

    return obj

#======================================================================================================

@app.get("/responsible_by_name/{nombre}")
async def root(nombre):

    sql_url = 'mssql+pymssql://preset:Adm1np3set19@mattilda-prod.database.windows.net/mattilda-prod'
    print(nombre)
    engine = create_engine(sql_url)
    
    result = engine.execute(f'select * from t_responsable where Nombre = \'{nombre}\'') 
    responsible_list = []
    for row in result:
        print(row)
        obj = {
            "idresponsable": row[0],
            "name": row[2],
            "pather_name": row[3],
            "mother_name": row[4],
            "UIDCollege": row[1],
            "email": row[6],
            "phone": row[7],
            "idalumno": row[9],
            "status": row[10],
            "records": row[11],
            "activity": row[12]
        }
        responsible_list.append(obj)
    result.close()

    return responsible_list

#======================================================================================================

@app.get("/college/{id_colegios}")
async def root(id_colegios):

    sql_url = 'mssql+pymssql://preset:Adm1np3set19@mattilda-prod.database.windows.net/mattilda-prod'
    print(id_colegios)
    engine = create_engine(sql_url)
    
    result = engine.execute(f'select * from cat_colegios where IDColegio = {id_colegios}')
    obj = {}
    for row in result:
        print(row)
        obj = {
            "name": row[1],
            "street": row[2],
            "suburb": row[4],
            "idsuburb": row[3],
            "municipality": row[5],
            "state": row[6],
            "zip": row[7],
            "record": [8],
            "fecha_reg": row[9]
        }
    result.close()

    return obj

#======================================================================================================

@app.get("/college_by_name/{nombre}")
async def root(nombre):

    sql_url = 'mssql+pymssql://preset:Adm1np3set19@mattilda-prod.database.windows.net/mattilda-prod'
    print(nombre)
    engine = create_engine(sql_url)
    
    result = engine.execute(f'select * from cat_colegios where Nombre = \'{nombre}\'') 
    college_list = []
    for row in result:
        print(row)
        obj = {
            "idcolegio": row[0],
            "name": row[1],
            "street": row[2],
            "suburb": row[4],
            "idsuburb": row[3],
            "municipality": row[5],
            "state": row[6],
            "zip": row[7],
            "record": [8],
            "fecha_reg": row[9]
        }
        college_list.append(obj)
    result.close()

    return college_list

#======================================================================================================

@app.get("/concepts/{id_conceptos}")  #*************************** 
async def root(id_conceptos):

    sql_url = 'mssql+pymssql://preset:Adm1np3set19@mattilda-prod.database.windows.net/mattilda-prod'
    print(id_conceptos)
    engine = create_engine(sql_url)
    
    result = engine.execute(f'select * from cat_conceptos where IDConcepto = {id_conceptos}')
    obj = {}
    for row in result:
        print(row)
        obj = {
            "concept": row[1],
            "category": row[2],
           }
    result.close()

    return obj

#======================================================================================================

@app.get("/campus/{id_campus}")
async def root(id_campus):

    sql_url = 'mssql+pymssql://preset:Adm1np3set19@mattilda-prod.database.windows.net/mattilda-prod'
    print(id_campus)
    engine = create_engine(sql_url)
    
    result = engine.execute(f'select * from cat_campus where IDCampus = {id_campus}')
    obj = {}
    for row in result:
        print(row)
        obj = {
            "name": row[1],
            "street": row[2],
            "Suburb": row[4],
            "idSuburb": row[3],
            "municipality": row[5],
            "state": row[6],
            "zip": row[7],
            "idcollege": row[8],
            "status": row[9],
            "fecha_reg": row[10]
           }
    result.close()

    return obj

#======================================================================================================

@app.get("/campus_by_name/{nombre}")
async def root(nombre):

    sql_url = 'mssql+pymssql://preset:Adm1np3set19@mattilda-prod.database.windows.net/mattilda-prod'
    print(nombre)
    engine = create_engine(sql_url)
    
    result = engine.execute(f'select * from cat_campus where Nombre = \'{nombre}\'') 
    campus_list = []
    for row in result:
        print(row)
        obj = {
            "idcampus": row[0],
            "name": row[1],
            "street": row[2],
            "Suburb": row[4],
            "idSuburb": row[3],
            "municipality": row[5],
            "state": row[6],
            "zip": row[7],
            "idcollege": row[8],
            "status": row[9],
            "fecha_reg": row[10]
        }
        campus_list.append(obj)
    result.close()

    return campus_list

#======================================================================================================

@app.get("/charges/{id_alumno}")
async def root(id_alumno):

    sql_url = 'mssql+pymssql://preset:Adm1np3set19@mattilda-prod.database.windows.net/mattilda-prod'
    print(id_alumno)
    engine = create_engine(sql_url)
    
    result = engine.execute(f'select * from t_cargos where IDAlumno = {id_alumno}')
    obj = {}
    for row in result:
        print(row)
        obj = {
            "transaction": row[1],
            "period": row[2],
            "idconcept": row[3],
            "concept": row[4],
            "amount": row[5],
            "balance": row[6],
            "userid": row[7],
            "expiration_date": row[8],
            "registration_date": row[9],
            "transactionID_old": row[10]
           }
    result.close()

    return obj

#======================================================================================================

@app.get("/campus_by_name/{nombre}")
async def root(nombre):

    sql_url = 'mssql+pymssql://preset:Adm1np3set19@mattilda-prod.database.windows.net/mattilda-prod'
    print(nombre)
    engine = create_engine(sql_url)
    
    result = engine.execute(f'select * from cat_campus where Nombre = \'{nombre}\'') 
    campus_list = []
    for row in result:
        print(row)
        obj = {
            "idcampus": row[0],
            "name": row[1],
            "street": row[2],
            "Suburb": row[4],
            "idSuburb": row[3],
            "municipality": row[5],
            "state": row[6],
            "zip": row[7],
            "idcollege": row[8],
            "status": row[9],
            "fecha_reg": row[10]
        }
        campus_list.append(obj)
    result.close()

    return campus_list

#======================================================================================================

@app.get("/charges_by_concept/{conceptos}")
async def root(conceptos):

    sql_url = 'mssql+pymssql://preset:Adm1np3set19@mattilda-prod.database.windows.net/mattilda-prod'
    print(conceptos)
    engine = create_engine(sql_url)
    
    result = engine.execute(f'select * from t_cargos where Concepto = \'{conceptos}\'')
    charges_list = []
    for row in result:
        print(row)
        obj = {
            "idalumno": row[0],
            "transaction": row[1],
            "period": row[2],
            "concept": row[4],
            "idconcept": row[3],         
            "amount": row[5],
            "balance": row[6],
            "userid": row[7],
            "expiration_date": row[8],
            "registration_date": row[9],
            "transactionID_old": row[10]
           }
        charges_list.append(obj)
    result.close()

    return charges_list

#======================================================================================================

@app.get("/discounts/{id_descuento}")
async def root(id_descuento):

    sql_url = 'mssql+pymssql://preset:Adm1np3set19@mattilda-prod.database.windows.net/mattilda-prod'
    print(id_descuento)
    engine = create_engine(sql_url)
    
    result = engine.execute(f'select * from t_descuentos where IDConfig_D = {id_descuento}')
    obj = {}
    for row in result:
        print(row)
        obj = {
            "idconcept": row[1],
            "desctypeid": row[2],
            "days_period": row[3],
            "date_application": row[4],
            "type_amount": row[5],
            "percentage": row[6],
            "amount": row[7],
            "idconcept_applies": row[8],
            "idstatus": row[9],
            "userid": row[10],
            "activity_date": row[11]
           }
    result.close()

    return obj

#======================================================================================================

@app.get("/scholarships/{id_becas}")
async def root(id_becas):

    sql_url = 'mssql+pymssql://preset:Adm1np3set19@mattilda-prod.database.windows.net/mattilda-prod'
    print(id_becas)
    engine = create_engine(sql_url)
    
    result = engine.execute(f'select * from t_becas where IDConfig_B = {id_becas}')
    obj = {}
    for row in result:
        print(row)
        obj = {
            "idconcept": row[1],
            "type_amount": row[2],
            "percentage": row[3],
            "amount": row[4],
            "idconcept_applies": row[5],
            "reason": row[6],
            "idstatus": row[7],
            "userid": row[8],
            "activity_date": row[9]
           }
    result.close()

    return obj

#======================================================================================================






#======================================================================================================

    return {"message": "Hello"}

@app.get("/hello/{name}")
async def say_Hello(name:str ):
    return {"message": f"Hello {name}"}

#======================================================================================================


**************************************************************************************************
==================================================================================================
**************************************************************************************************



Es decir, vas a construir un Api Restful en C# 
para conectar con el ERP Banner de una escuela, 
considerando con los siguientes Endpoints:
Conceptos ???
Alumnos   !!!
Colegios  !!!
Campus    !!!
Cargos    !!
Descuentos!!
Becas     !!
Plan de estudios !!


7019 8020 Amazing Toys 


Buenos días a todos Equipo  :)  ya estamos en el ombligo de la semana, el Miercoles.
La frase de hoy es del autor Copérnico:

"23. No estoy tan enamorado de mis propias opiniones que ignore lo que los demás puedan pensar acerca de ellas."

Que todos pasen un lindo y productivo día, :)  ademas de muchas bendiciones para todos.





















