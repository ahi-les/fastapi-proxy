from sqlalchemy import Column, String, Integer
from core.db import Base


class Proxy(Base):
    __tablename__ = "proxies"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    ip = Column(String)
    port = Column(Integer)
    login = Column(String)
    pass_ = Column(String)
    active = Column(String)
    port_http = Column(Integer)
    label = Column(String, nullable=True)
