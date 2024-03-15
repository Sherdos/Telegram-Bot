from database_conf import engine
from sqlalchemy.orm import Session
from models import Sentens
from sqlalchemy import select
import random

def get_session():
    with Session(engine) as session:
        return session


def get_phrath():
    sesion = get_session()
    stmt = select(Sentens)
    data = sesion.scalars(stmt)
    
    return random.choice(list(data))

    # for i in session.scalars(stmt):
    #     print(i)
    




