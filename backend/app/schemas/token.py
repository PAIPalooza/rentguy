from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    sub: str | None = None  # user ID or email
    email: EmailStr | None = None
    roles: list[str] = []

class Msg(BaseModel):
    message: str
