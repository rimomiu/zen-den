from fastapi import (
    # Depends,
    # Request,
    # Response,
    # HTTPException,
    # status,
    APIRouter,
)

# from queries.blogs_queries import BlogQueries


from models.blogs import CreateBlogs

# from utils.authentication import (
#     try_get_jwt_user_data,
#     hash_password,
#     generate_jwt,
#     verify_password,
# )

router = APIRouter()


@router.post("/blogs")
def create_blogs(blog: CreateBlogs):
    return blog
