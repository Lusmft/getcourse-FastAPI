import rootdir

from fastapi import (
    APIRouter,
    Depends,
    status,
)
from fastapi.security import OAuth2PasswordRequestForm

from models.auth import (
    Token,
    UserCreate,
    User,
)

from services.auth import (
    AuthService,
    get_current_user,
)


router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.post(
    '/sign-up/',
    response_model=Token,
    status_code=status.HTTP_201_CREATED,
)
async def sign_up(
    user_data: UserCreate,
    auth_service: AuthService = Depends(),
):
    '''Регистрация пользователя'''
    return auth_service.register_new_user(user_data)


@router.post(
    '/sign-in/',
    response_model=Token,
)
async def sign_in(
    auth_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(),
):
    '''Авторизация пользователя'''
    return auth_service.authenticate_user(
        auth_data.username,
        auth_data.password,
    )


@router.get(
    '/user/',
    response_model=User,
)
async def get_user(user: User = Depends(get_current_user)):
    '''Получение данных о пользователе !Необходима авторизация!'''
    return user
