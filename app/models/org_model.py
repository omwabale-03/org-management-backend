from pydantic import BaseModel

class OrgCreate(BaseModel):
    organization_name: str
    email: str
    password: str

class OrgGet(BaseModel):
    organization_name: str

class OrgUpdate(BaseModel):
    old_name: str
    new_name: str
    new_email: str
    new_password: str

class OrgDelete(BaseModel):
    organization_name: str
