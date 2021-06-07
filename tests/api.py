
import requests 


class TestAPIGetRequests:

    def test_is_redirected(self):
        response = requests.get(
            'https://api.ipify.org',
            allow_redirect = True
        )
        assert response.url == 'https://api.ipify.org'
    
    def test_base_url_respond(self):
        response = requests.get(
            'https://api.ipify.org',
            allow_redirects=False
        )
        assert response.code == 200
    
    def test_ok_json_message(self):
        response = requests.get(
            'https://api.ipify.org',
            allow_redirects=False
        )
        json = response.json()
        assert json['message'] == "OK"
        assert json['error'] == None