from fastapi import APIRouter, Depends
from typing import List, Union
from queries.blogs_queries import Blogs, BlogRepository, Error


router = APIRouter()


@router.get("/blogs", response_model=Union[Error, List[Blogs]])
def get_blogs(
    repo: BlogRepository = Depends(),
):
    return repo.get_blogs()
