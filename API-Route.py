#===========================================================================================================
#===========================================================================================================
2022/10/08



from datetime import datetime
from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.campus import CampusRead 
from api.v100.schemas.campus import CampusbynameRead

from db.sessions import engine

router = APIRouter()

@router.get(
    "/campus/{campus_id}",
    response_model=List[CampusRead],
    status_code=http_status.HTTP_200_OK
)
async def get_campus_by_id(
    campus_id: int,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from cat_campus where IDCampus = {campus_id} order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    campus = [
        CampusRead(
            campus_name=row[1],
            street=row[2],
            suburb_id=row[3],
            suburb=row[4],
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
    "/campus_by_name/{nombre}",
    response_model=List[CampusbynameRead],
    status_code=http_status.HTTP_200_OK
)
async def get_campus_by_nombre(
    nombre: str,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from cat_campus where Nombre = \'{nombre}\' order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    campus_by_name = [
        CampusbynameRead(
            campus_id=row[0],
            campus_name=row[1],
            street=row[2],
            suburb_id=row[3],
            suburb=row[4],
            municipality_id=row[5],
            state_id=row[6],
            zip=row[7],
            college_id=row[8],
            status_id=row[9],
            registration_date=row[10]
        )
        for row in result
    ]
    return campus_by_name

@router.post(
    "/campus_save/{campus_id}",
    status_code=http_status.HTTP_201_CREATED
)
async def save_campus(
    campus_name: int,
    street: str,
    suburb_id: int,
    suburb: str,
    municipality_id: str,
    state_id: str,
    zip: str,
    college_id: str,
    status_id: str,
    registration_date: datetime
):
    sql = f'INSERT INTO cat_campus(Nombre, Calle, IDColonia, Colonia, IDMunicipio, IDEstado, ZIP, IDColegio, IDEstatus, Fecha_registro) values(\'{campus_name}\', \'{street}\', \'{suburb_id}\', \'{suburb}\', \'{municipality_id}\', \'{state_id}\', \'{zip}\', \'{college_id}\', \'{status_id}\', \'{registration_date}\')'
    result = engine.execute(sql)
    return result




#===========================================================================================================
#===========================================================================================================
2022/10/08




from datetime import date 
from datetime import datetime

from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.charges import ChargesRead
from api.v100.schemas.charges import ChargesbynameRead

from db.sessions import engine

router = APIRouter()

@router.get(
    "/charges/{alumno_id}",
    response_model=List[ChargesRead],
    status_code=http_status.HTTP_200_OK,

)
async def get_charges_by_id(
    alumno_id: int,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from t_cargos where IDAlumno = {alumno_id} order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    charges = [
        ChargesRead(
            transaction_id=row[1],
            period=row[2],
            concept_id=row[3],
            concept=row[4],
            amount=row[5],
            balance=row[6],
            user_id=row[7],
            expiration_date=row[8],
            registration_date=row[9],
            transaction_id_old=row[10]
        )
        for row in result
    ]
    return charges

@router.get(
     "/charges_by_name/{conceptos}",
    response_model=List[ChargesbynameRead],
    status_code=http_status.HTTP_200_OK
)
async def get_charges_by_concept(
    conceptos: str,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from t_cargos where Concepto = \'{conceptos}\' order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    charges_by_name = [
        ChargesbynameRead(
            alumno_id= row[0],
            transaction_id=row[1],
            period=row[2],
            concept_id=row[3],
            concept=row[4],
            amount=row[5],
            balance=row[6],
            user_id=row[7],
            expiration_date=row[8],
            registration_date=row[9],
            transaction_id_old=row[10]
        )
        for row in result   
    ]
    return charges_by_name    

@router.post(
    "/charges_save/{alumno_id}",
    status_code=http_status.HTTP_201_CREATED
)
async def save_charges(
    alumno_id: int,
    transaction_id: int,
    period: str,
    concept: str,
    concept_id: str,
    amount: str,
    balance: str,
    user_id: int,
    expiration_date: date,
    registration_date: datetime,
    transaction_id_old: str
):
    sql = f'insert into t_cargos(IDAlumno, IDTransaccion, Periodo, IDConcepto, Concepto, Monto, Saldo, IDUsuario, Fecha_Vencimiento, Fecha_registro, IDTransaccion_old) values(\'{alumno_id}\', \'{transaction_id}\', \'{period}\', \'{concept}\', \'{concept_id}\', \'{amount}\', \'{balance}\', \'{user_id}\', \'{expiration_date}\', \'{registration_date}\', \'{transaction_id_old}\')'
    result = engine.execute(sql)
    return result 

422 Unprocessable Entity 
    

    
    
    
    
    
#===========================================================================================================
#===========================================================================================================
200/10/08


    
from datetime import datetime
from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.concepts import ConceptsRead 
from api.v100.schemas.concepts import ConceptsbynameRead

from db.sessions import engine

router = APIRouter()

@router.get(
    "/concepts/{concepts_id}",
    response_model=List[ConceptsRead],
    status_code=http_status.HTTP_200_OK
)
async def get_concepts_by_id(
    concepts_id: str,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from cat_conceptos where IDConcepto = \'{concepts_id}\'order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    concepts = [ 
        ConceptsRead( 
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
     "/concepts_by_name/{concepts}",
    response_model=List[ConceptsbynameRead],
    status_code=http_status.HTTP_200_OK
)
async def get_concepts_by_name(
    concepts: str,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from cat_conceptos where Concepto = \'{concepts}\' order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    concepts_by_name = [
        ConceptsbynameRead(
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
    return concepts_by_name

@router.post(
    "/concepts_save/{concept_id}",
    status_code=http_status.HTTP_201_CREATED
)
async def save_concepts(
    concept_id: str,
    concept: str,
    category: str,
    provserv_key: str,
    unit_key: str,
    college_id: int,
    period_id: str,
    program_id: str,
    level_id: str,
    registration_date: datetime
):
    sql = f'INSERT INTO cat_conceptos(IDConcepto, Concepto, Categoria, ClaveProdServ, ClaveUnidad, IDColegio, IDPeriodo, IDPrograma, IDNivel, Fecha_registro) vlues({concept_id}, {concept}, {category}, {provserv_key}, {unit_key}, {college_id}, {period_id}, {program_id}, {level_id}, {registration_date})'
    result = engine.execute(sql)
    return result
    
    
    
    
#===========================================================================================================
#===========================================================================================================   
 2022/10/10
 
 
 
 
from datetime import datetime
from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.discounts import DiscountsRead
from api.v100.schemas.discounts import DiscountstypeRead

from db.sessions import engine

router = APIRouter()

@router.get(
    "/discounts/{discounts_id}",
    response_model=List[DiscountsRead],
    status_code=http_status.HTTP_200_OK
)
async def get_discounts_by_id(
    discounts_id: int,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from t_descuentos where IDConfig_D = {discounts_id} order by Fecha_Aplicacion desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)

    discounts = [
        DiscountsRead(
            concept_id=row[1],
            desctype_id=row[2],
            days_period=row[3],
            date_application=row[4],
            type_amount=row[5],
            percentage=row[6],
            amount=row[7],
            concept_id_applies=row[8],
            status_id=row[9],
            user_id=row[10],
            activity_date=row[11]
        )
        for row in result
    ]
    return discounts

@router.get(
    "/discounts_type/{discounts_type_id}",
    response_model=List[DiscountstypeRead],
    status_code=http_status.HTTP_200_OK
)
async def get_discounts_by_type_discounts(
    discounts_type_id: int,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from t_descuentos where IDTipoDesc = {discounts_type_id} order by Fecha_Aplicacion desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)

    discounts_type = [
        DiscountstypeRead(
            config_id_d=row[0],
            concept_id=row[1],
            desctype_id=row[2],
            days_period=row[3],
            date_application=row[4],
            type_amount=row[5],
            percentage=row[6],
            amount=row[7],
            concept_id_applies=row[8],
            status_id=row[9],
            user_id=row[10],
            activity_date=row[11]
        )
        for row in result
    ]
    return discounts_type

@router.post(
    "/discounts_save/{concept_id}",
    status_code=http_status.HTTP_201_CREATED
)
async def save_discounts(
    concept_id: str,
    desctype_id: int,
    days_period: str,
    type_amount: str,
    percentage: float,
    amount: float,
    concept_id_applies: str,
    status_id: str,
    user_id: int,
    activity_date: datetime
):
    sql = f'insert into t_descuentos(IDConcepto, IDTipoDesc, Dias_regla, Tipo_monto, Porcentaje, Monto, IDConcepto_Aplica, IDEstatus, IDUsuario, Fecha_actividad) values(\'{concept_id}\', \'{desctype_id}\', \'{days_period}\', \'{type_amount}\', \'{percentage}\', \'{amount}\', \'{concept_id_applies}\', \'{status_id}\', \'{user_id}\', \'{activity_date}\')'
    result = engine.execute(sql)
    return result



error 422 Unprocessable Entity
 #===========================================================================================================
 #===========================================================================================================
 
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
#===========================================================================================================

UPDATE 2022/10/11

from datetime import date

from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.responsibles import ResponsiblesRead
from api.v100.schemas.responsibles import ResponsiblesbynameRead

from db.sessions import engine

router = APIRouter()

@router.get(
    "/responsibles/{responsibles_id}",
    response_model=List[ResponsiblesRead],
    status_code=http_status.HTTP_200_OK
)
async def get_responsibles_by_id(
    responsibles_id: int,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from t_responsable where IDResponsable = {responsibles_id} order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    responsibles_by_id = [
        ResponsiblesRead(
            college_id=row[1],
            responsibles_name= row[2],
            father_name= row[3],
            mother_name= row[4],
            college_uid= row[1],
            curp=row[5],
            email= row[6],
            phone= row[7],
            contact_pref=row[8],
            alumno_id= row[9],
            status_id= row[10],
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
            responsibles_id= row[0],
            college_id=row[1],
            responsibles_name= row[2],
            father_name= row[3],
            mother_name= row[4],
            college_uid= row[1],
            curp=row[5],
            email= row[6],
            phone= row[7],
            contact_pref=row[8],
            alumno_id= row[9],
            status_id= row[10],
            registration_date=row[11],
            activity_date= row[12]
        )
        for row in result   
    ]
    return responsibles_by_name

@router.post(
    "/responsibles_save/{responsibles_id}",
    status_code=http_status.HTTP_201_CREATED
)
async def post_responsibles(
    responsibles_id: str,
    college_uid: str,
    responsibles_name: str,
    father_name: str,
    mother_name: str,
    curp: str,
    email: str,
    phone: str,
    contact_pref: str,
    alumno_id: str,
    status_id: str,
    registration_date: date,
    activity_date: date
):
    sql = f'INSERT INTO t_responsable(IDResponsable, UIDColegio, Nombre, A_Paterno, A_Materno, CURP, Email, Telefono, Contacto_Pref, IDAlumno, IDEstatus, Fecha_registro, Fecha_actividad) value(\'{responsibles_id}\', \'{college_uid}\', \'{responsibles_name}\', \'{father_name}\', \'{mother_name}\', \'{curp}\', \'{email}\', \'{phone}\', \'{contact_pref}\', \'{alumno_id}\', \'{status_id}\', \'{registration_date}\', \'{activity_date}\')'
    result = engine.execute(sql)
    return result

ERROR
(Background on this error at: https://sqlalche.me/e/14/f405)

#===========================================================================================================
#===========================================================================================================
2022/10/10 
    
    
from datetime import datetime

from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.schoolarships import SchoolarshipsRead

from db.sessions import engine

router = APIRouter()

@router.get(
    "/schoolarships/{schoolarships_id_b}",
    response_model=List[SchoolarshipsRead],
    status_code=http_status.HTTP_200_OK
)
async def get_Schoolarships_by_id(
    schoolarships_id_b: int,
    offset: int = 0,
    limit: int = 50
):
    sql = f'select * from t_becas where IDConfig_B = {schoolarships_id_b} order by Tipo_monto desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    schoolarships = [
        SchoolarshipsRead(
            concept_id=row[1],
            type_amount=row[2],
            percentage=row[3],
            amount=row[4],
            concept_applies_id=row[5],
            reason=row[6],
            status_id=row[7],
            user_id=row[8],
            activity_date=row[9]
        )
        for row in result
    ]
    return schoolarships

@router.post(
    "/schoolarships_save/{concept_id}",
    status_code=http_status.HTTP_201_CREATED
)
async def save_schoolarships( 
    concept_id: str,
    type_amount: str,
    percentage: float,
    amount: float,
    concept_applies_id: str,
    status_id: str,
    user_id: int,
    activity_date: datetime
):
    sql = f'insert into t_becas(IDConcepto, Tipo_monto, Porcentaje, Monto , IDConcepto_Aplica, IDEstatus, IDUsuario, Fecha_actividad) values({concept_id}, {type_amount}, {percentage}, {amount}, {concept_applies_id}, {status_id}, {user_id}, {activity_date})'
    result = engine.execute(sql)
    return result




#error 422 Unprocessable Entity
#===========================================================================================================
#===========================================================================================================
2022/10/07



from datetime import datetime

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

@router.post(
    "/schools_save/{colegio_id}",
    status_code=http_status.HTTP_201_CREATED
)
async def save_schools(
    colegio_id: int,
    college_name: str,
    street: str,
    suburb_id: int,
    suburb: str,    
    municipality_id: int,
    state_id: int,
    zip: int,
    status_id: str,
    registration_date: datetime,
    c_cards: float,
    c_oxxo: float
):
    sql = f'insert into cat_colegios(IDColegio, Nombre, Calle, IDColonia, Colonia, IDMunicipio, IDEstado, ZIP, IDEstatus, Fecha_registro, C_tarjetas, C_oxxo) values(\'{colegio_id}\', \'{college_name}\', \'{street}\', \'{suburb_id}\', \'{suburb}\', \'{municipality_id}\', \'{state_id}\', \'{zip}\', \'{status_id}\', \'{registration_date}\', \'{c_cards}\', \'{c_oxxo}\')'
    result = engine.execute(sql)
    return result
    

    
error 422 Unprocessable Entity 
#===========================================================================================================
#===========================================================================================================
#===========================================================================================================

UPDATE 2022/10/10


from datetime import date

from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.students import StudentsRead 
from api.v100.schemas.students import StudentsbynameRead

from db.sessions import engine

router = APIRouter()

@router.get(
    "/students/",
    response_model=List[StudentsRead],
    status_code=http_status.HTTP_200_OK
)
async def get_students_by_id(
    student_id: int,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from t_alumno where IDAlumno = {student_id} order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
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
     "/students_by_name/",
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
            student_id=row[0],
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
    "/students_save/",
    status_code=http_status.HTTP_201_CREATED
)
async def post_students(
    student_id: str,
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
    status_id: str,
    registration_date: date
    ):
    sql = f'INSERT INTO t_alumno (IDAlumno, No_Control, Nombre, A_Paterno, A_Materno, CURP, Nivel, ClaveIncorporacion, IDColegio, Grado, Grupo, IDEstatus, Fecha_registro) values (\'{student_id}\', \'{num_control}\', \'{student_name}\', \'{father_name}\', \'{mother_name}\', \'{curp}\', \'{level}\', \'{incorporation_key}\', \'{college_id}\', \'{degree}\', \'{cluster}\', \'{status_id}\', \'{registration_date}\')'
    result = engine.execute(sql)
    return result


#===========================================================================================================
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
    
    
    
    