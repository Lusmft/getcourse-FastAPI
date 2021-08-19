import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tables import Base
from database import get_session
from app import app


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.sqlite3"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_session] = override_get_db

client = TestClient(app)


def test_sign_up():
    response = client.post(
        "/auth/sign-up/",
        json={"email": "deadpool@example.com", "username": "userr", "password": "chimichangas4life"},
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["token_type"] == "bearer"


def test_sign_up_if_user_exists():
    response = client.post(
        "/auth/sign-up/",
        json={"email": "deadpool@example.com", "username": "userr", "password": "chimichangas4life"},
    )
    assert response.status_code == 401, response.text
    data = response.json()
    assert data["detail"] == "Username is already exists"


def test_sign_in():
    response = client.post(
        "/auth/sign-in/", 
        data={"username": "userr", "password": "chimichangas4life", 'grant_type': '', 'scope': '', 'client_id': '', 'client_secret': ''},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["token_type"] == "bearer"
    assert 'access_token' in data
    access_token = data['access_token']
    return access_token
    
    
def test_failed_sign_in():
    response = client.post(
        "/auth/sign-in/", 
        data={"username": "username", "password": "password"},
    )
    assert response.status_code == 401, response.text
    data = response.json()
    assert data["detail"] == "Incorrect username or password"
    
 
def test_get_user():
    access_token = test_sign_in()
    response = client.get(
        "/auth/user/", 
        headers={'Authorization': 'Bearer ' + access_token},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['email'] == 'deadpool@example.com'
    assert data['username'] == 'userr'
    assert data['id'] == 1
    
    
def test_get_user_without_token():
    response = client.get(
        "/auth/user/", 
    )
    assert response.status_code == 401, response.text
    data = response.json()
    assert data['detail'] == 'Not authenticated'
    

def test_import_deals():
    access_token = test_sign_in()
    response = client.post(
        '/deals/import/',
        headers={'Authorization': 'Bearer ' + access_token},
        json={
            "settings_data": {
                "account_name": "lusmft",
                "key": "Ipzfg4zygJG1N4VJcw2TcgNuFo1UEZGo4Y9ox0UxAetQK68wPPVfpCx99oPpXMTjLCdg5eyyr4J6Bj8zsCEgehaJCFU3lppwSrP9ds9M9wAUIY9Ov4ueWGQZUSTwygF5"
            },
            "user_data": {
                "email": "user@example.com",
                "phone": "string",
                "first_name": "string",
                "last_name": "string",
                "city": "string",
                "country": "string",
                "group_name": [
                  "string"
                ],
                "add_fields": {}
              },
              "system_data": {
                "refresh_if_exists": True,
                "partner_email": "user@example.com",
                "multiple_offers": True,
                "return_payment_link": True,
                "return_deal_number": True
              },
              "session_data": {
                "utm_source": "string",
                "utm_medium": "string",
                "utm_content": "string",
                "utm_campaign": "string",
                "utm_group": "string",
                "gcpc": "string",
                "gcao": "string",
                "referer": "string"
              },
              "deal_data": {
                "deal_number": 1,
                "offer_code": 521090,
                "product_title": "Новый",
                "product_description": "string",
                "quantity": 1,
                "deal_cost": 1000,
                "deal_status": "new",
                "deal_is_paid": True,
                "manager_email": "user@example.com",
                "deal_created_at": "2021-08-19T21:07:53.792Z",
                "deal_finished_at": "2021-08-19T21:07:53.792Z",
                "deal_comment": "string",
                "payment_type": "2CO",
                "payment_status": "expected",
                "partner_email": "user@example.com",
                "addfields": {},
                "deal_currency": "RUB"
            }
        }
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['success'] == True
    assert data['action'] == 'add'
    assert data['result']['success'] == True, data['result']['error_message']
    
    
def test_remove_db():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.sqlite3')
    os.remove(path)
