from pydantic import BaseModel

class ItemCreate(BaseModel):
    title: str
    description: str = None
    completed: bool = False

class ItemResponse(ItemCreate):
    id: int

    class Config:
        orm_mode = True
