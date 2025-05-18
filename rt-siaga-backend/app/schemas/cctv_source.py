from pydantic import BaseModel

class CCTVSourceBase(BaseModel):
    name: str
    url: str

class CCTVSourceCreate(CCTVSourceBase):
    pass

class CCTVSourceResponse(CCTVSourceBase):
    id: int

    class Config:
        orm_mode = True