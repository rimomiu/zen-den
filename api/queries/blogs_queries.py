from pydantic import BaseModel


class Blogs(BaseModel):
    title: str
    pic_url: str
    content: str
    author_id: int
