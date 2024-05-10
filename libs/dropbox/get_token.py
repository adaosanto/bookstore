import requests
from django.conf import settings
from dataclasses import dataclass

@dataclass
class TokenData:
    access_token: str
    token_type: str
    expires_in: float|int

def get_token_by_refresh_token() -> TokenData:

    params = {
        "grant_type": "refresh_token",
        "refresh_token": settings.DROPBOX_API_REFRESH_TOKEN,
        "client_id": settings.DROPBOX_CLIENT_ID_APP_KEY,
        "client_secret": settings.DROPBOX_CLIENT_SECRET_APP_SECRET,
    }

    response = requests.post(
        url=settings.DROPBOX_API_URL,
        params=params
    )

    response.raise_for_status()

    return TokenData(
        **response.json()
    )