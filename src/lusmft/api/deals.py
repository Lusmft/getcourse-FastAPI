import rootdir

from typing import Dict

from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)

from models.deals import (
    SettingsData,
    UserData,
    SystemData,
    SessionData,
    DealData,
    )
    
from models.auth import User

from services.auth import (
    AuthService,
    get_current_user,
)

from services.deals import DealsService


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
    