import os
import sys
from dataclasses import dataclass

import requests


@dataclass
class TokenData:
    """Data class to store token information."""

    access_token: str
    token_type: str
    expires_in: float | int


def __get_token_by_refresh_token() -> TokenData:
    """
    Retrieves a new access token using a refresh token.

    Returns:
        TokenData: Object containing information about the new token.
    """
    params = {
        "grant_type": "refresh_token",
        "refresh_token": os.environ.get("DROPBOX_API_REFRESH_TOKEN"),
        "client_id": os.environ.get("DROPBOX_CLIENT_ID_APP_KEY"),
        "client_secret": os.environ.get("DROPBOX_CLIENT_SECRET_APP_SECRET"),
    }

    response = requests.post(url=os.environ.get("DROPBOX_API_URL"), params=params)

    response.raise_for_status()

    return TokenData(**response.json())


def get_token_by_refresh_token():
    """
    Retrieves the access token using a refresh token, if the command is 'dbbackup'.

    Returns:
        str: Access token.
    """
    if not "dbbackup" in sys.argv:
        return

    token = __get_token_by_refresh_token()

    return token.access_token
