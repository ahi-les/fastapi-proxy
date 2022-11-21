from fastapi import APIRouter
from proxy.tables import Proxy
from core.db import SessionLocal
from models.operations import Operation
from  sqlalchemy.sql.expression import func

router = APIRouter(
    prefix='/proxy',
)

@router.get('/',response_model=Operation)
def get_random_proxy():
    sessionLocal = SessionLocal()
    operations = (
        sessionLocal
        .query(Proxy)
        .order_by(func.random())
        .first()
    )

    sessionLocal.close()
    return operations