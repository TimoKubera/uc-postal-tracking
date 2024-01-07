from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenRequestForm(BaseModel):
    username: str
    password: str

class User(BaseModel):
    username: str

    class Config:
        orm_mode = True

# Additional schemas can be added here
