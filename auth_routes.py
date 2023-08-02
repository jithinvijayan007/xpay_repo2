from fastapi import APIRouter,status
from fastapi.exceptions import HTTPException
from database import Session,engine
from schema import SignUpModel
from models import User, Profile
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash , check_password_hash
from fastapi.encoders import jsonable_encoder

auth_router = APIRouter(
    prefix='/auth'
)

session = Session(bind=engine)

@auth_router.get('/')
async def hello():
    return {"message":'Hello World!'}

@auth_router.post('/signup',
    status_code=status.HTTP_201_CREATED
)
async def signup(user:SignUpModel):
    """
        ## Create a user
        This requires the following
        ```
                fullname:str
                email:str
                phone:str
                profile_picture:str("s3_url_have_to_br_pass_here")
                password:str
                is_active:bool

        ```
    
    """


    email=session.query(User).filter(User.email==user.email).first()

    if email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with the email already exists"
        )

    phone=session.query(User).filter(User.phone==user.phone).first()

    if phone is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with the phone already exists"
        )
    
    new_user=User(
        fullname=user.fullname,
        email=user.email,
        phone=user.phone,
        password=generate_password_hash(user.password),
    )

    session.add(new_user)

    session.commit()

    profile = Profile(
        user_id = str(new_user.id),
        profile_picture = user.profile_picture
    )
    session.add(profile)

    session.commit()

    return {"maeesage": "user signup succesfull",
            "status":"success"}, 201


@auth_router.get('/users')
async def list_all_users():
    """
        ## List all users
        This lists all  users
        
    
    """

    users=session.query(User).all()
    data = [
    {
        "id": str(user.id),
        "fullname": user.fullname,
        "email": user.email,
        "phone": user.phone,
        "profile_picture": user.profile
    }
    for user in users
]
        


    return {"data":data,
            "status":"success"}, 200
