import unittest
import unittest.mock
from django.conf import settings
from libs.dropbox.get_token import get_token_by_refresh_token

def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status):
            self.json_data = json_data
            self.status = status

        def json(self):
            return self.json_data
        
        def raise_for_status(self): ...
        
    if kwargs['url'] == settings.DROPBOX_API_URL:
        json_data = {
            "access_token": "sl.xpto..",
            "token_type": "bearer",
            "expires_in": 14400,
        }
        status = 200

    else:
        json_data = {"detail": "Not mocked"}
        status = 400

    return MockResponse(json_data, status)

class TestDropBox:
    @unittest.mock.patch('libs.dropbox.get_token.requests.post', side_effect=mocked_requests_get)
    def test_get_token(self, mock_get):
        import sys
        sys.argv.append('dbbackup')
        response = get_token_by_refresh_token()

        assert 'sl.' in response
