from pydantic import BaseModel
from typing import List, Optional

class Page(BaseModel):
    id: str
    name: str
    url: str
    profile_pic: Optional[str]
    email: Optional[str]
    website: Optional[str]
    category: Optional[str]
    followers: int
    likes: int
    creation_date: str

class Post(BaseModel):
    id: str
    page_id: str
    content: str
    likes: int
    comments: List[str]

class Comment(BaseModel):
    id: str
    post_id: str
    user: str
    text: str
    timestamp: str
