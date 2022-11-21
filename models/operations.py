from typing import Optional

from pydantic import BaseModel

class Operation(BaseModel):
    id: int
    ip: str
    port: int
    login: str
    pass_: str
    active: str
    port_http: int
    label: Optional[str]

    class Config:
        orm_mode = True