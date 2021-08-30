from typing import Dict

from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)

from app.models.deals import (
    SettingsData,
    UserData,
    SystemData,
    SessionData,
    DealData,
    )
    
from app.models.auth import User

from app.services.auth import (
    AuthService,
    get_current_user,
)

from app.services.deals import DealsService


router = APIRouter(
    prefix='/deals',
    tags=['deals'],
)


@router.post(
        '/import/',
        response_model=Dict)
async def get_deals(settings_data: SettingsData, user_data: UserData, system_data: SystemData, session_data: SessionData, deal_data: DealData, user: User = Depends(get_current_user), deal_service: DealsService = Depends()):
    '''Импортирует/обновляет сделку
    !Необходима авторизация!'''
    return deal_service.import_deal(settings_data.dict(), user_data.dict(), system_data.dict(), session_data.dict(), deal_data.dict())
    