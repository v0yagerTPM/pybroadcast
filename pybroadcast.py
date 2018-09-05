import requests
import json

class pybroadcast:
    def __init__(self, username, password):
        self.URL = 'https://www.slybroadcast.com/gateway/vmb.json.php'
        self.USERNAME = username
        self.PASSWORD = password

    def verify_user(self):
        payload = \
            {
                'c_uid': self.USERNAME,
                'c_password': self.PASSWORD,
                'c_option': 'user_verify'
            }
        return requests.post(self.URL, data=payload)

    def get_audio_file(self):
        payload = \
            {
                'c_uid': self.USERNAME,
                'c_password': self.PASSWORD,
                'c_method': 'get_audio_list'
            }
        return json.loads(requests.post(self.URL, data=payload).content)

    def create_campaign(self, caller_id, phone, date, audio_file, mobile_only):
        payload = \
            {
                'c_uid': self.USERNAME,
                'c_password': self.PASSWORD,
                'c_method': 'new_campaign',
                'c_callerID': caller_id,
                'c_phone': phone,
                'c_date': date,
                'c_record_audio': audio_file,
                'mobile_only': mobile_only
            }
        return json.loads(requests.post(self.URL, data=payload).content)