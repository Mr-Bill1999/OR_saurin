from pydantic import BaseModel

class URLCreate(BaseModel):
    url: str

class URLStats(BaseModel):
    id: int
    short_id: str
    full_url: str

    class Config:
        orm_mode = True

