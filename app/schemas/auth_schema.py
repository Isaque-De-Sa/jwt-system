from pydantic import BaseModel

class Register(BaseModel):

    reg_user: str
    reg_email: str
    reg_pass: str


class Login(BaseModel):

    user: str
    pass2: str