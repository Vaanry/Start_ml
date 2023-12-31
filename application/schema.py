import datetime
from pydantic import BaseModel

class UserGet(BaseModel):
    id: int
    gender: str
    age: int
    country: str
    city: str
    exp_group: int
    os: str
    source: str

    class Config:
        orm_mode = True

class PostGet(BaseModel):
    id: int
    text: str
    topic: str

    class Config:
        orm_mode = True

class FeedGet(BaseModel):
    id: int
    user_id: int
    post_id: int
    action: str
    time: datetime.datetime
    user: UserGet
    post: PostGet

    class Config:
        orm_mode = True
        
        
class Response(BaseModel):
    exp_group: str
    recommendations: List[PostGet]