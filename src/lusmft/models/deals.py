from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import (
    BaseModel, 
    EmailStr,
    )
    

class DealStatus(str, Enum):
    NEW = 'new'
    PAYED = 'payed'
    CANCELLED = 'cancelled'
    FALSE = 'false'
    IN_WORK = 'in_work'
    PAYMENT_WAITING = 'payment_waiting'
    PART_PAYED = 'part_payed'
    WAITING_FOR_RETURN = 'waiting_for_return'
    NOT_CONFIRMED = 'not_confirmed'
    PENDING = 'pending'
    
    
class PaymentStatus(str, Enum):
    EXPECTED = 'expected'
    ACCEPTED = 'accepted'
    RETURNED = 'returned'
    TOBALANCE = 'tobalance'
    FROMBALANCE = 'frombalance'
    RETURNED_TO_BALANCE = 'returned_to_balance'
    

class PaymentType(str, Enum):
    CO = '2CO'
    ALFA = "ALFA"
    BILL = 'BILL'
    CARD = 'CARD'
    CARD_TERMINAL = 'CARD_TERMINAL'
    CASH = 'CASH'
    CLOUD_PAYMENTS = 'cloud_payments'
    CLOUD_PAYMENTS_KZ = 'cloud_payments_kz'
    FONDY = 'fondy'
    HUTKI_GROSH = 'hutki_grosh'
    INTERKASSA = 'interkassa'
    INTERNAL = 'INTERNAL'
    JUSTCLICK = 'justclick'
    KVIT = 'kvit'
    OTHER = 'OTHER'
    PAYANYWAY = 'payanyway'
    PAYPAL = 'PAYPAL'
    PERFECT_MONEY = 'perfect_money'
    PERFECTMONEY = 'PERFECTMONEY'
    QIWI = 'QIWI'
    QIWI_KASSA = 'qiwi_kassa'
    QUICKTRANSFER = 'QUICKTRANSFER'
    RBK = 'RBK'
    RBKMONEY = 'rbkmoney'
    RBKMONEY_NEW = 'rbkmoney_new'
    ROBOKASSA = 'ROBOKASSA'
    SBER = 'SBER'
    SBERBANK = 'sberbank'
    TINKOFF = 'tinkoff'
    TINKOFFCREDIT = 'tinkoffcredit'
    VIRTUAL = 'VIRTUAL'
    WALLETONE = 'walletone'
    WAYFORPAY = 'wayforpay'
    WEBMONEY = 'WEBMONEY'
    YANDEX_KASSA = 'yandex_kassa'
    YANDEXMONEY = 'YANDEXMONEY'
    ZPAYMENT = 'ZPAYMENT'
    PRODAMUS = 'prodamus'
    EBANX = 'ebanx'
    SWEDBANK = 'swedbank'
    

class Currency(str, Enum):
    RUB = 'RUB'
    USD = 'USD'
    EUR = 'EUR'
    GBP = 'GBP'
    BYR = 'BYR'
    BYN = 'BYN'
    KZT = 'KZT'
    UAH = 'UAH'
    AUD = 'AUD'
    DKK = 'DKK'
    CHF = 'CHF'
    SEK = 'SEK'
    ZAR = 'ZAR'
    AMD = 'AMD'
    RON = 'RON'
    BRL = 'BRL'
    ILS = 'ILS'
    MYR = 'MYR'
    SGD = 'SGD'
    KGS = 'KGS'
    CAD = 'CAD'
    MXN = 'MXN'
    JPY = 'JPY'
    UZS = 'UZS'
    
class SettingsData(BaseModel):
    account_name: str
    key: str
    
class UserData(BaseModel):
    email: EmailStr
    phone: str
    first_name: str
    last_name: str
    city: str
    country: str
    group_name: Optional[list]
    add_fields: Optional[dict]

 
class SystemData(BaseModel):
    refresh_if_exists: Optional[bool]
    partner_email: Optional[EmailStr]
    multiple_offers: Optional[bool]
    return_payment_link: Optional[bool]
    return_deal_number: Optional[bool]


class SessionData(BaseModel):
    utm_source: Optional[str]
    utm_medium: Optional[str]
    utm_content: Optional[str]
    utm_campaign: Optional[str]
    utm_group: Optional[str]
    gcpc: str
    gcao: Optional[str]
    referer: Optional[str]
    
    
class DealData(BaseModel):
    deal_number: int
    offer_code: int
    product_title: str
    product_description: Optional[str]
    quantity: int
    deal_cost: int
    deal_status: Optional[DealStatus]
    deal_is_paid: Optional[bool]
    manager_email: Optional[EmailStr]
    deal_created_at: Optional[datetime]
    deal_finished_at: Optional[datetime]
    deal_comment: Optional[str]
    payment_type: Optional[PaymentType]
    payment_status: Optional[PaymentStatus]
    partner_email: Optional[EmailStr]
    addfields: Optional[dict]
    deal_currency: Optional[Currency]
