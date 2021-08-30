import requests, json

from typing import Dict

from fastapi import (
    HTTPException,
    status,
)

from app.models.deals import (
    SettingsData,
    UserData,
    SystemData,
    SessionData,
    DealData,
    )
    
from base64 import b64encode


class DealsService:
    def import_deal(self, settings_data: SettingsData, user_data: UserData, system_data: SystemData, session_data: SessionData, deal_data: DealData) -> Dict:
        account_name = settings_data['account_name']
        key = settings_data['key']
        url = f'https://{account_name}.getcourse.ru/pl/api/deals'
        
        deal_data = self.parse_deal_data(deal_data)
        
        params = {'user': user_data, 'system': system_data, 'session': session_data, 'deal': deal_data}
        
        request = requests.post(url, data={'key': key, 'action': 'add', 'params': b64encode(json.dumps(params).encode("utf-8"))})
        if request.status_code==404:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
       
        return json.loads(str(request.content,'utf-8'))
        
    def parse_deal_data(self, deal_data: DealData) -> Dict:
        if deal_data['deal_created_at'] != None:
            deal_data['deal_created_at'] = deal_data['deal_created_at'].strftime('%Y-%m-%d %H:%M:%S')
        if deal_data['deal_finished_at'] != None:
            deal_data['deal_finished_at'] = deal_data['deal_finished_at'].strftime('%Y-%m-%d %H:%M:%S')
        if deal_data['deal_status'] != None:
            deal_data['deal_status'] = deal_data['deal_status'].value
        if deal_data['payment_status'] != None:
            deal_data['payment_status'] = deal_data['payment_status'].value
        if deal_data['payment_type'] != None:
            deal_data['payment_type'] = deal_data['payment_type'].value
        if deal_data['deal_currency'] != None:
            deal_data['deal_currency'] = deal_data['deal_currency'].value
        return deal_data
