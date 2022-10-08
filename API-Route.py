from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.campus import CampusRead, CampusbynameRead

from db.sessions import engine

router = APIRouter()

@router.get(
    "/campus/{id_campus}",
    response_model=List[CampusRead],
    status_code=http_status.HTTP_200_OK
)
async def get_campus_by_id(
    id_campus: int
):
    sql = f'select * from cat_campus where IDCampus = {id_campus}'
    result = engine.execute(sql)

    campus = [
        CampusRead(
            campus_name=row[1],
            street=row[2],
            suburb=row[4],
            suburb_id=row[3],
            municipality_id=row[5],
            state_id=row[6],
            zip=row[7],
            college_id=row[8],
            status_id=row[9],
            registration_date=row[10]
        )
        for row in result
    ]
    return campus

@router.get(
    "/campusbyname/{nombre}",
    response_model=List[CampusbynameRead],
    status_code=http_status.HTTP_200_OK
)
async def get_campus_by_nombre(
    nombre: str
):
    sql = f'select * from cat_campus where Nombre = \'{nombre}\''
    result = engine.execute(sql)

    campusbyname = [
        CampusbynameRead(
            campus_id=row[0],
            campus_name=row[1],
            street=row[2],
            suburb=row[4],
            suburb_id=row[3],
            municipality_id=row[5],
            state_id=row[6],
            zip=row[7],
            college_id=row[8],
            status_id=row[9],
            registration_date=row[10]
        )
        for row in result
    ]
    return campusbyname



#====================================================================
from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.charges import ChargesRead, ChargesbynameRead

from db.sessions import engine

router = APIRouter()

@router.get(
    "/charges/{id_alumno}",
    response_model=List[ChargesRead],
    status_code=http_status.HTTP_200_OK
)
async def get_charges_by_id(
    id_alumno: int
):
    sql = f'select * from t_cargos where IDAlumno = {id_alumno}'
    result = engine.execute(sql)

    charges = [
        ChargesRead(
            period=row[2],
            concept=row[4],
            amount=row[5],
            balance=row[6],
            userid=row[7],
            registration_date=row[9],
        )
        for row in result
    ]
    return charges

@router.get(
     "/chargesbyname/{conceptos}",
    response_model=List[ChargesbynameRead],
    status_code=http_status.HTTP_200_OK
)
async def get_charges_by_name(
    conceptos: str
):
    sql = f'select * from t_cargos where Concepto = \'{conceptos}\''
    result = engine.execute(sql)

    chargesbyname = [
        ChargesbynameRead(
            idalumno= row[0],
            period=row[2],
            concept=row[4],
            amount=row[5],
            balance=row[6],
            userid=row[7],
            registration_date=row[9],
        )
        for row in result   
    ]
    return chargesbyname    
    
#====================================================================
    
from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.concepts import ConceptRead, ConceptbynameRead

from db.sessions import engine

router = APIRouter()

@router.get(
    "/concepts/{id_conceptos}",
    response_model=List[ConceptRead],
    status_code=http_status.HTTP_200_OK
)
async def get_concepts_by_id(
    id_conceptos: str
):
    sql = f'select * from cat_conceptos where IDConcepto = \'{id_conceptos}\''
    result = engine.execute(sql)

    concepts = [ 
        ConceptRead( 
            concept=row[1],
            category=row[2], 
            provserv_key=row[3], 
            unit_key=row[4],
            college_id=row[5],     
            period_id=row[6],     
            program_id=row[7],
            level_id=row[8],
            registration_date=row[9]
        )
        for row in result
    ]
    for row in result: 
        print(row)

    return concepts

@router.get(
     "/conceptbyname/{concepto}",
    response_model=List[ConceptbynameRead],
    status_code=http_status.HTTP_200_OK
)
async def get_concept_by_name(
    concepto: str
):
    sql = f'select * from cat_conceptos where Concepto = \'{concepto}\''
    result = engine.execute(sql)
    conceptbyname = [
        ConceptbynameRead(
            concept_id=row[0],
            concept=row[1],
            category=row[2], 
            provserv_key=row[3], 
            unit_key=row[4],
            college_id=row[5],     
            period_id=row[6],     
            program_id=row[7],
            level_id=row[8],
            registration_date=row[9]
        )
        for row in result   
    ]
    return conceptbyname
    
#====================================================================   
 
from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.discounts import DiscountsRead

from db.sessions import engine

router = APIRouter()

@router.get(
    "/discounts/{id_descuento}",
    response_model=List[DiscountsRead],
    status_code=http_status.HTTP_200_OK
)
async def get_discounts_by_id(
    id_descuento: int
):
    sql = f'select * from t_descuentos where IDConfig_D = {id_descuento}'
    result = engine.execute(sql)

    discounts = [
        DiscountsRead(
            idconcept=row[1],
            desctypeid=row[2],
            days_period=row[3],
            date_application=row[4],
            type_amount=row[5],
            percentage=row[6],
            amount=row[7],
            idconcept_applies=row[8],
            idstatus=row[9],
            userid=row[10],
            activity_date=row[11]
        )
        for row in result
    ]
    return discounts

 #====================================================================
 
from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.payments import PaymentsRead, PaymentsbytransaccionRead

from db.sessions import engine

router = APIRouter()

@router.get(
    "/payments/{id_alumno}",
    response_model=List[PaymentsRead],
    status_code=http_status.HTTP_200_OK
)
async def get_payments_by_id_alumno(
    id_alumno: int
):
    sql = f'select * from t_pagos where IDAlumno = {id_alumno}'
    result = engine.execute(sql)

    payments = [
        PaymentsRead(
            transact_id=row[1],
            transaction_charge_id=row[2],
            concepts_id=row[3],
            concepts=row[4],
            payment_amount=row[5],
            amount_applied=row[6],
            status_id=row[7],
            payment_id=row[9],
            user_id=row[10],
            pay_day=row[11],
            registration_date=row[12]
        )
        for row in result
    ]
    return payments

@router.get(
    "/paymentsbytransaccion/{id_transaccion}",
    response_model=List[PaymentsbytransaccionRead],
    status_code=http_status.HTTP_200_OK
)
async def get_payments_by_id_transaccion(
    id_transaccion: int
):
    sql = f'select * from t_pagos where IDTransaccion = {id_transaccion}'
    result = engine.execute(sql)

    paymentsbytransaccion = [
        PaymentsbytransaccionRead(
            alumno_id=row[0],
            transact_id=row[1],
            transaction_charge_id=row[2],
            concepts_id=row[3],
            concepts=row[4],
            payment_amount=row[5],
            amount_applied=row[6],
            status_id=row[7],
            payment_id=row[9],
            user_id=row[10],
            pay_day=row[11],
            registration_date=row[12]
        )
        for row in result
    ]
    return paymentsbytransaccion


#===========================================================================================================
#===========================================================================================================
2022/10/07



from datetime import datetime

from typing import List, Union

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.responsibles import ResponsiblesRead
from api.v100.schemas.responsibles import ResponsiblesbynameRead

from db.sessions import engine

router = APIRouter()

@router.get(
    "/responsibles/{responsable_id}",
    response_model=List[ResponsiblesRead],
    status_code=http_status.HTTP_200_OK
)
async def get_responsibles_by_id(
    responsable_id: int,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from t_responsable where IDResponsable = {responsable_id} order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    responsibles_by_id = [
        ResponsiblesRead(
            college_id=row[1],
            responsable_name= row[2],
            father_name= row[3],
            mother_name= row[4],
            college_uid= row[1],
            curp=row[5],
            email= row[6],
            phone= row[7],
            contact_pref=row[8],
            alumno_id= row[9],
            status= row[10],
            registration_date=row[11],
            activity_date= row[12]
        )
        for row in result
    ]
    return responsibles_by_id

@router.get(
     "/responsibles_by_name/{nombre}",
    response_model=List[ResponsiblesbynameRead],
    status_code=http_status.HTTP_200_OK
)
async def get_responsibles_by_name(
    nombre: str,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from t_responsable where Nombre = \'{nombre}\' order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    responsibles_by_name = [
        ResponsiblesbynameRead(
            responsable_id= row[0],
            college_id=row[1],
            responsable_name= row[2],
            father_name= row[3],
            mother_name= row[4],
            college_uid= row[1],
            curp=row[5],
            email= row[6],
            phone= row[7],
            contact_pref=row[8],
            alumno_id= row[9],
            status= row[10],
            registration_date=row[11],
            activity_date= row[12]
        )
        for row in result   
    ]
    return responsibles_by_name





#===========================================================================================================
#===========================================================================================================
    
    
    
from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.schoolarships import SchoolarshipsRead

from db.sessions import engine

router = APIRouter()

@router.get(
    "/schoolarships/{id_becas}",
    response_model=List[SchoolarshipsRead],
    status_code=http_status.HTTP_200_OK
)
async def get_discounts_by_id(
    id_becas: int
):
    sql = f'select * from t_becas where IDConfig_B = {id_becas}'
    result = engine.execute(sql)

    schoolarships = [
        SchoolarshipsRead(
            idconcept=row[1],
            type_amount=row[2],
            percentage=row[3],
            amount=row[4],
            idconcept_applies=row[5],
            reason=row[6],
            idstatus=row[7],
            userid=row[8],
            activity_date=row[9]
        )
        for row in result
    ]
    return schoolarships
    
#===========================================================================================================
#===========================================================================================================
2022/10/07




from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.schools import SchoolsRead
from api.v100.schemas.schools import SchoolsbynameRead

from db.sessions import engine

router = APIRouter()

@router.get(
    "/schools/{id_colegios}",
    response_model=List[SchoolsRead],
    status_code=http_status.HTTP_200_OK
)
async def get_schools_by_id(
    id_colegios: int,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from cat_colegios where IDColegio = {id_colegios} order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    schools = [
        SchoolsRead(
            college_name=row[1],
            street=row[2],
            suburb=row[4],
            suburb_id=row[3],
            municipality_id=row[5],
            state_id=row[6],
            zip=row[7],
            status_id=row[8],
            registration_date=row[9],
            c_cards=row[10],
            c_oxxo=row[11]
        )
        for row in result
    ]
    return schools

@router.get(
    "/schools_by_name/{nombre}",
    response_model=List[SchoolsbynameRead],
    status_code=http_status.HTTP_200_OK
)
async def get_schools_by_nombre(
    nombre: str,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from cat_colegios where Nombre = \'{nombre}\' order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    schools_by_name = [
        SchoolsbynameRead(
            colegio_id=row[0],
            college_name=row[1],
            street=row[2],
            suburb=row[4],
            suburb_id=row[3],
            municipality_id=row[5],
            state_id=row[6],
            zip=row[7],
            status_id=row[8],
            registration_date=row[9],
            c_cards=row[10],
            c_oxxo=row[11]
        )
        for row in result
    ]
    return schools_by_name
    
    
    
#===========================================================================================================
#===========================================================================================================
2022/10/07



from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.students import StudentsRead, StudentsbynameRead

from db.sessions import engine

router = APIRouter()

@router.get(
    "/students/{id_alumno}",
    response_model=List[StudentsRead],
    status_code=http_status.HTTP_200_OK
)
async def get_students_by_id(
    id_alumno: int,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from t_alumno where IDAlumno = {id_alumno} order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    students = [
        StudentsRead(   
            num_control=row[1],
            student_name=row[2],
            father_name=row[3],
            mother_name=row[4],            
            curp=row[5],
            level_id=row[6],
            level=row[7],
            incorporation_key=row[8],
            college_id=row[9],
            campus_id=row[10],
            grade=row[11],
            cluster=row[12],
            status_id=row[13],
            registration_date=row[14]
        )
        for row in result
    ]
    return students

@router.get(
     "/students_by_name/{nombre}",
    response_model=List[StudentsbynameRead],
    status_code=http_status.HTTP_200_OK
)
async def get_students_by_name(
    nombre: str,
    Offset: int = 0,
    Limit: int = 20
):
    sql = f'select * from t_alumno where Nombre = \'{nombre}\' order by Fecha_registro desc offset {Offset} rows fetch first {Limit} rows only'
    result = engine.execute(sql)
    students_by_name = [
        StudentsbynameRead(
            alumno_id= row[0],
            num_control=row[1],
            student_name=row[2],
            father_name=row[3],
            mother_name=row[4],
            curp=row[5],
            level_id=row[6],
            level=row[7],
            incorporation_key=row[8],
            college_id=row[9],
            campus_id=row[10],
            grade=row[11],
            cluster=row[12],
            status_id=row[13],
            registration_date=row[14]
        )
        for row in result   
    ]
    return students_by_name

@router.post(
    "/students_save/{alumno_id}",
    status_code=http_status.HTTP_201_CREATED
)
async def save_students(
    alumno_id: str,
    num_control: str,
    student_name: str,
    father_name: str,
    mother_name: str,
    curp: str,
    level: str,
    incorporation_key: str,
    college_id: str,
    degree: str,
    cluster: str,
    status_id: str
    ):
    sql = f'INSERT INTO t_alumno (IDAlumno, No_Control, Nombre, A_Paterno, A_Materno, CURP, Nivel, ClaveIncorporacion, IDColegio, Grado, Grupo, IDEstatus) values (\'{alumno_id}\', \'{num_control}\', \'{student_name}\', \'{father_name}\', \'{mother_name}\', \'{curp}\', \'{level}\', \'{incorporation_key}\', \'{college_id}\', \'{degree}\', \'{cluster}\', \'{status_id}\')'
    result = engine.execute(sql)
    return result



#===========================================================================================================
#===========================================================================================================


    
    alumno_id: str,
    num_control: str,
    student_name: str,
    father_name: str,
    mother_name: str,
    curp: str,
    level: str,
    incorporation_key: str,
    college_id: str,
    degree: str,
    cluster: str,
    status_id: str
    
    
    {alumno_id}, {num_control}, {student_name}, {father_name}, {mother_name}, {curp}, {level}, {incorporation_key}, {college_id}, {degree}, {cluster}, {status_id} "
    {alumno_id}, {num_control}, {student_name}, {father_name}, {mother_name}, {curp}, {level}, {incorporation_key}, {college_id}, {degree}, {cluster}, {status_id} "
    
   
    
    f'INSERT INTO t_responsable
    (
    1)IDResponsable, 
    2)UIDColegio, 
    3)Nombre, 
    4)A_Paterno, 
    5)A_Materno, 
    6)CURP, 
    7)Email, 
    8)Telefono, 
    9)Contacto_Pref, 
    10)IDAlumno, 
    11)IDEstatus, 
    12)Fecha_registro, 
    13)Fecha_actividad
    )
    values
    (
    1\'{responsable_id}\',
    2\'{college_uid}\',
    3\'{responsable_name}\',
    4\'{father_name}\',
    5\'{mother_name}\',
    6\'{curp}\', 
    7\'{email}\',
    8\'{phone}\', 
    9\'{contact_pref}\',
    10\'{alumno_id}\', 
    11\'{status}\', 
    12\'{registration_date}\',
    13'{activity_date}\'
    )
    
    
    
    