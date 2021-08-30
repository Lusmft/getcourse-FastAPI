from fastapi import FastAPI

from fastapi import APIRouter

from api import auth
from api import deals


router = APIRouter()
router.include_router(auth.router)
router.include_router(deals.router)


tags_metadata = [
    {
        'name': 'auth',
        'description': 'Авторизация и регистрация',
    },
    {
        'name': 'deals',
        'description': 'Импортирование/обновление сделки',
    }
]

app = FastAPI(
    title='getcourse-FastAPI',
    description='Сервис для импортирования/обновления сделок в getcourse.ru',
    version='1.0.0',
    openapi_tags=tags_metadata,
)

app.include_router(router)
