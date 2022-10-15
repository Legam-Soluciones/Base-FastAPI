#===========================================================================================================
#===========================================================================================================

2022/10/13 CAMPUS / CAMPUS

#===========================================================================================================
#===========================================================================================================

from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.campus import CampusRead, CampusbynameRead, CampusCreate

from db.sessions import engine

router = APIRouter()

@router.get(
    "/campus/",
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
    for row in result: 
        print(row)
    return campus

@router.get(
    "/campus_by_name/",
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
    for row in result: 
        print(row)
    return campus_by_name

@router.post(
    "/create_campus/",
    name="create_campus",
    status_code=http_status.HTTP_201_CREATED
)
async def post_campus(
    campus_create: CampusCreate
):
    sql = f"""
            INSERT INTO cat_campus(
                Nombre, 
                Calle, 
                IDColonia, 
                Colonia, 
                IDMunicipio, 
                IDEstado, 
                ZIP, 
                IDColegio, 
                IDEstatus, 
                Fecha_registro
            ) 
            values
            (
                \'{campus_create.campus_name}\', 
                \'{campus_create.street}\', 
                \'{campus_create.suburb_id}\', 
                \'{campus_create.suburb}\', 
                \'{campus_create.municipality_id}\', 
                \'{campus_create.state_id}\', 
                \'{campus_create.zip}\',
                \'{campus_create.college_id}\', 
                \'{campus_create.status_id}\', 
                \'{campus_create.registration_date}\'
            )
            """
    result = engine.execute(sql)
    return result


#===========================================================================================================
#===========================================================================================================

2022/10/013 CHARGES / PAGOS
#===========================================================================================================
#===========================================================================================================


from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.charges import ChargeRead, ChargebynameRead, ChargeCreate

from db.sessions import engine

router = APIRouter()

@router.get(
    "/charges/",
    response_model=List[ChargeRead],
    status_code=http_status.HTTP_200_OK,
)
async def get_charges_by_id(
    student_id: int,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from t_cargos where IDAlumno = {student_id} order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    charges = [
        ChargeRead(
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
    for row in result: 
        print(row)
    return charges

@router.get(
    "/charges_by_concept/",
    response_model=List[ChargebynameRead],
    status_code=http_status.HTTP_200_OK
)
async def get_charges_by_concept(
    concept: str,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from t_cargos where Concepto = \'{concept}\' order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    charges_by_name = [
        ChargebynameRead(
            student_id= row[0],
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
    for row in result: 
        print(row)
    return charges_by_name    

@router.post(
    "/create_charges/",
    name="create_charge",
    status_code=http_status.HTTP_201_CREATED
)
async def create_charge(
    charge_create: ChargeCreate
):
    sql = f"""
            insert into t_cargos (
                IDAlumno, 
                IDTransaccion, 
                Periodo, 
                IDConcepto, 
                Concepto, 
                Monto, 
                Saldo, 
                IDUsuario, 
                Fecha_Vencimiento, 
                Fecha_registro, 
                IDTransaccion_old
            ) 
            values(
                \'{charge_create.student_id}\', 
                \'{charge_create.transaction_id}\', 
                \'{charge_create.period}\', 
                \'{charge_create.concept_id}\', 
                \'{charge_create.concept}\', 
                \'{charge_create.amount}\', 
                \'{charge_create.balance}\', 
                \'{charge_create.user_id}\', 
                \'{charge_create.expiration_date}\', 
                \'{charge_create.registration_date}\', 
                \'{charge_create.transaction_id_old}\'
            )
            """
    result = engine.execute(sql)
    return result
    
    
#===========================================================================================================
#===========================================================================================================
200/10/12 CONCEPTS / Conceptos
#===========================================================================================================
#===========================================================================================================


   from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.concepts import ConceptRead, ConceptbynameRead, ConceptCreate

from db.sessions import engine

router = APIRouter()

@router.get(
    "/concepts/",
    response_model=List[ConceptRead],
    status_code=http_status.HTTP_200_OK
)
async def get_concepts_by_id(
    concepts_id: str,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from cat_conceptos where IDConcepto = \'{concepts_id}\' order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    concepts = [ 
        ConceptRead( 
            concepts=row[1],
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
     "/concepts_by_concept/",
    response_model=List[ConceptbynameRead],
    status_code=http_status.HTTP_200_OK
)
async def get_concepts_by_concept(
    concepts: str,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from cat_conceptos where Concepto = \'{concepts}\' order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    concepts_by_concept = [
        ConceptbynameRead(
            concepts_id=row[0],
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
    return concepts_by_concept

@router.post(
    "/create_concepts/",
    name="create_concepts",
    status_code=http_status.HTTP_201_CREATED
)
async def create_concepts(
    concept_create: ConceptCreate
):
    sql = f""" 
            insert into cat_conceptos(
                IDConcepto, 
                Concepto, 
                Categoria, 
                ClaveProdServ, 
                ClaveUnidad, 
                IDColegio, 
                IDPeriodo, 
                IDPrograma, 
                IDNivel, 
                Fecha_registro
            ) 
            values(
                \'{concept_create.concepts_id}\', 
                \'{concept_create.concept}\', 
                \'{concept_create.category}\', 
                \'{concept_create.provserv_key}\', 
                \'{concept_create.unit_key}\', 
                \'{concept_create.college_id}\', 
                \'{concept_create.period_id}\', 
                \'{concept_create.program_id}\', 
                \'{concept_create.level_id}\', 
                \'{concept_create.registration_date}\'
            )
            """
    result = engine.execute(sql)
    return result

#ERROR 422 Unprocessable Entity
    
#===========================================================================================================
#===========================================================================================================   
 2022/10/13 discounts / descuentos
#===========================================================================================================
#===========================================================================================================
 
 
from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.discounts import DiscountRead, DiscounttypeRead, DiscountCreate

from db.sessions import engine

router = APIRouter()

@router.get(
    "/discounts/",
    response_model=List[DiscountRead],
    status_code=http_status.HTTP_200_OK
)
async def get_discount_by_id(
    discounts_id: int,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from t_descuentos where IDConfig_D = {discounts_id} order by Fecha_Aplicacion desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)

    discounts = [
        DiscountRead(
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
    for row in result: 
        print(row)
    return discounts

@router.get(
    "/discounts_type/",
    response_model=List[DiscounttypeRead],
    status_code=http_status.HTTP_200_OK
)
async def get_discount_by_type_discounts(
    discounts_type_id: int,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from t_descuentos where IDTipoDesc = {discounts_type_id} order by Fecha_Aplicacion desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)

    discounts_type = [
        DiscounttypeRead(
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
    for row in result: 
        print(row)
    return discounts_type

@router.post(
    "/create_discounts/",
    name="create_discounts",
    status_code=http_status.HTTP_201_CREATED
)
async def create_discounts(
    discounts_create: DiscountCreate
):
    sql = f"""
            insert into t_descuentos(
                IDConcepto, 
                IDTipoDesc, 
                Dias_regla, 
                Tipo_monto, 
                Porcentaje, 
                Monto, 
                IDConcepto_Aplica, 
                IDEstatus, 
                IDUsuario, 
                Fecha_actividad
            )
            values(
                \'{discounts_create.concept_id}\', 
                \'{discounts_create.desctype_id}\', 
                \'{discounts_create.days_period}\', 
                \'{discounts_create.type_amount}\', 
                \'{discounts_create.percentage}\', 
                \'{discounts_create.amount}\', 
                \'{discounts_create.concept_id_applies}\', 
                \'{discounts_create.status_id}\', 
                \'{discounts_create.user_id}\', 
                \'{discounts_create.activity_date}\'
            )
            """
    result = engine.execute(sql)
    return result
    
    
 #===========================================================================================================
 #===========================================================================================================
 2022/10/14  payments / pagos
 #===========================================================================================================
 #===========================================================================================================

from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.payments import PaymentRead, PaymentbytransaccionRead, PaymentCreate

from db.sessions import engine

router = APIRouter()

@router.get(    
    "/payments/",
    response_model=List[PaymentRead],
    status_code=http_status.HTTP_200_OK 
)
async def get_payments_by_id_alumno(    
    student_id: int,
    offset: int = 0,
    limit: int = 20  
):
    sql = f'select * from t_pagos where IDAlumno = {student_id} order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    payments = [
        PaymentRead(
            transaction_id=row[1],
            transaction_charge_id=row[2],
            concepts_id=row[3],
            concepts=row[4],
            payment_amount=row[5],
            amount_applied=row[6],
            status_id=row[7],
            uid_cfdi=row[8],
            payment_id=row[9],
            user_id=row[10],
            pay_day=row[11],
            registration_date=row[12],
            transaction_id_old=row[13],
            transaction_id_charge_old=row[14]
        )
        for row in result
    ]
    for row in result: 
        print(row)
    return payments

@router.get(
    "/paymentsbytransaccion/",
    response_model=List[PaymentbytransaccionRead],
    status_code=http_status.HTTP_200_OK
)
async def get_payments_by_id_transaccion(
    id_transaccion: int,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from t_pagos where IDTransaccion = {id_transaccion}order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    paymentbytransaccion = [
        PaymentbytransaccionRead(
            student_id=row[0],
            transaction_id=row[1],
            transaction_charge_id=row[2],
            concepts_id=row[3],
            concepts=row[4],
            payment_amount=row[5],
            amount_applied=row[6],
            status_id=row[7],
            uid_cfdi=row[8],
            payment_id=row[9],
            user_id=row[10],
            pay_day=row[11],
            registration_date=row[12],
            transaction_id_old=row[13],
            transaction_id_charge_old=row[14]
        )
        for row in result
    ]
    for row in result: 
        print(row)
    return paymentbytransaccion

@router.post(
    "/create_payments/",
    name="create_payments",
    status_code=http_status.HTTP_201_CREATED
)  
async def create_discounts(
    payments_create: PaymentCreate
):  
    sql = f"""
            insert into t_pagos(
                IDAlumno, 
                IDTransaccion, 
                IDTransaccion_Cargo, 
                IDConcepto, 
                Concepto,
                Monto_Pago, 
                Monto_Aplicado, 
                IDEstatus, 
                UID_CFDI, 
                IDPago, 
                IDUsuario, 
                Fecha_Pago, 
                Fecha_registro, 
                IDTransaccion_old, 
                IDTransaccion_Cargo_old
            ) 
            values(
                \'{payments_create.student_id}\',
                \'{payments_create.transaction_id}\',
                \'{payments_create.transaction_charge_id}\',
                \'{payments_create.concepts_id}\',
                \'{payments_create.concepts}\',
                \'{payments_create.payment_amount}\',
                \'{payments_create.amount_applied}\',
                \'{payments_create.status_id}\',
                \'{payments_create.uid_cfdi}\',
                \'{payments_create.payment_id}\',
                \'{payments_create.user_id}\',
                \'{payments_create.pay_day}\',
                \'{payments_create.registration_date}\',
                \'{payments_create.transaction_id_old}\',
            )
            """
    result = engine.execute(sql)
    return result

#422 Unprocessable Entity

#===========================================================================================================
#===========================================================================================================
2022/10/14 RESPONSABLE / responsibles
#===========================================================================================================
#===========================================================================================================


from datetime import date

from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.responsibles import ResponsibleRead, ResponsiblebynameRead, ResponsibleCreate

from db.sessions import engine

router = APIRouter()

@router.get(
    "/responsibles/",
    response_model=List[ResponsibleRead],
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
        ResponsibleRead(
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
     "/responsibles_by_name/",
    response_model=List[ResponsiblebynameRead],
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
        ResponsiblebynameRead(
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
    "/create_responsibles/",
    name="create_responsibles",
    status_code=http_status.HTTP_201_CREATED
)
async def post_responsibles(
    responsibles_create: ResponsibleCreate
):
    sql = f"""
            insert into t_responsable(
                IDResponsable, 
                UIDColegio, 
                Nombre, 
                A_Paterno, 
                A_Materno, 
                CURP, 
                Email, 
                Telefono, 
                Contacto_Pref, 
                IDAlumno, 
                IDEstatus, 
                Fecha_registro, 
                Fecha_actividad
            ) 
            value(
                \'{responsibles_create.responsibles_id}\', 
                \'{responsibles_create.college_uid}\', 
                \'{responsibles_create.responsibles_name}\', 
                \'{responsibles_create.father_name}\', 
                \'{responsibles_create.mother_name}\', 
                \'{responsibles_create.curp}\', 
                \'{responsibles_create.email}\', 
                \'{responsibles_create.phone}\', 
                \'{responsibles_create.contact_pref}\', 
                \'{responsibles_create.alumno_id}\', 
                \'{responsibles_create.status_id}\', 
                \'{responsibles_create.registration_date}\', 
                \'{responsibles_create.activity_date}\'
            )
            """
    result = engine.execute(sql)
    return result
#===========================================================================================================
#===========================================================================================================
2022/10/12 BECAS / schoolarships
#===========================================================================================================
#===========================================================================================================
   
    
from datetime import datetime
from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.schoolarships import SchoolarshipsRead, SchoolarshipCreate

from db.sessions import engine

router = APIRouter()

@router.get(
    "/schoolarships/",
    response_model=List[SchoolarshipsRead],
    status_code=http_status.HTTP_200_OK
)
async def get_Schoolarships_by_id(
    schoolarships_id_b: int,
    offset: int = 0,
    limit: int = 20
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
    "/create_schoolarships/",
    name="create_schoolarships",
    status_code=http_status.HTTP_201_CREATED
)
async def post_schoolarships( 
    schoolarships_create: SchoolarshipCreate
):
    sql = f"""
            insert into t_becas(
                IDConcepto, 
                Tipo_monto, 
                Porcentaje, 
                Monto , 
                IDConcepto_Aplica, 
                IDEstatus, 
                IDUsuario,
                Fecha_actividad
            ) 
            values(
                \'{schoolarships_create.concept_id}\', 
                \'{schoolarships_create.type_amount}\',
                \'{schoolarships_create.percentage}\',
                \'{schoolarships_create.amount}\', 
                \'{schoolarships_create.concept_applies_id}\',
                \'{schoolarships_create.status_id}\', 
                \'{schoolarships_create.user_id}\',
                \'{schoolarships_create.activity_date}\'
            )
            """
    result = engine.execute(sql)
    return result
    
    
#===========================================================================================================
#===========================================================================================================
2022/10/12 SCHOOLS / colegios
#===========================================================================================================
#===========================================================================================================

from datetime import date, datetime

from typing import List, Optional

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.schools import SchoolRead, SchoolbynameRead, SchoolCreate

from db.sessions import engine

router = APIRouter()

@router.get(
    "/schools/",
    response_model=List[SchoolRead],
    status_code=http_status.HTTP_200_OK
)
async def get_schools_by_id(
    college_id: int,
    offset: int = 0,
    limit: int = 20
):
    sql = f'select * from cat_colegios where IDColegio = {college_id} order by Fecha_registro desc offset {offset} rows fetch first {limit} rows only'
    result = engine.execute(sql)
    schools = [
        SchoolRead(
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
    for row in result: 
        print(row)
    return schools

@router.get(
    "/schools_by_name/",
    response_model=List[SchoolbynameRead],
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
        SchoolbynameRead(
            college_id=row[0],
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
    for row in result: 
        print(row)
    return schools_by_name

@router.post(
    "/create_schools/",
    name="create_schools",
    status_code=http_status.HTTP_201_CREATED
)
async def create_schools(
    school_create: SchoolCreate
):
    sql = f"""
            insert into cat_colegios(
                IDColegio, 
                Nombre, 
                Calle, 
                IDColonia, 
                Colonia, 
                IDMunicipio, 
                IDEstado, 
                ZIP, 
                IDEstatus, 
                Fecha_registro, 
                C_tarjetas, 
                C_oxxo
            ) 
            values(
                \'{school_create.college_id}\', 
                \'{school_create.college_name}\', 
                \'{school_create.street}\', 
                \'{school_create.suburb_id}\', 
                \'{school_create.suburb}\', 
                \'{school_create.municipality_id}\', 
                \'{school_create.state_id}\', 
                \'{school_create.zip}\', 
                \'{school_create.status_id}\', 
                \'{school_create.registration_date}\', 
                \'{school_create.c_cards}\', 
                \'{school_create.c_oxxo}\'
            )
            """
    result = engine.execute(sql)
    return result
    
    
#===========================================================================================================
#===========================================================================================================
2022/10/12 STUDENTS / alumnos
#===========================================================================================================
#===========================================================================================================

UPDATE 2022/10/10


from datetime import date

from typing import List

from fastapi import APIRouter
from fastapi import status as http_status

from api.v100.schemas.students import StudentRead, StudentbynameRead, StudentCreate

from db.sessions import engine

router = APIRouter()

@router.get(
    "/students/",
    response_model=List[StudentRead],
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
        StudentRead(   
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
    for row in result: 
        print(row)
    return students

@router.get(
     "/students_by_name/",
    response_model=List[StudentbynameRead],
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
        StudentbynameRead(
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
    for row in result: 
        print(row)
    return students_by_name

@router.post(
    "/create_students/",
    name="create_students",
    status_code=http_status.HTTP_201_CREATED
)
async def post_students(
    student_create: StudentCreate
    ):
    sql = f"""
                insert into t_alumno(
                    IDAlumno, 
                    No_Control, 
                    Nombre, 
                    A_Paterno, 
                    A_Materno, 
                    CURP, 
                    Nivel, 
                    ClaveIncorporacion, 
                    IDColegio, 
                    Grado, 
                    Grupo, 
                    IDEstatus, 
                    Fecha_registro
                )
                values(
                    \'{student_create.student_id}\', 
                    \'{student_create.num_control}\', 
                    \'{student_create.student_name}\', 
                    \'{student_create.father_name}\', 
                    \'{student_create.mother_name}\', 
                    \'{student_create.curp}\', 
                    \'{student_create.level}\', 
                    \'{student_create.incorporation_key}\', 
                    \'{student_create.college_id}\', 
                    \'{student_create.degree}\', 
                    \'{student_create.cluster}\', 
                    \'{student_create.status_id}\', 
                    \'{student_create.registration_date}\'
                )
                """
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
    
    