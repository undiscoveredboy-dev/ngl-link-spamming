import os
from dotenv import load_dotenv
import requests
from fake_useragent import UserAgent
import random
import string
import time


class RequestSender:
    def __init__(self, url):
        self.url = url

    def send_request(self, username, question, deviceId, gameSlug='', referrer=''):
        ua = UserAgent()
        headers = self._generate_headers(username)
        data = {
            'username': username,
            'question': question,
            'deviceId': deviceId,
            'gameSlug': gameSlug,
            'referrer': referrer
        }
        response = requests.post(self.url, headers=headers, data=data)
        return response

    def send_request_with_retry(self, username, question, deviceId, gameSlug='', referrer='', max_retries=3):
        retries = 0
        while retries < max_retries:
            response = self.send_request(username, question, deviceId, gameSlug, referrer)
            if response.status_code == 429:  # Too Many Requests
                retry_after = int(response.headers.get('Retry-After', 10))  # Default to waiting 10 seconds
                print(f"\rRate limited. Retrying after {retry_after} seconds...", end='', flush=True)
                time.sleep(retry_after)
                retries += 1
            elif response.status_code == 200:  # Success
                return response
            else:
                print(f"Unexpected error: {response.status_code} - {response.reason}")
                return response
        print("Max retries reached. Failed to send request.")
        return None

    def _generate_headers(self, username):
        sec_ch_ua = [
            '"Microsoft Edge";v="123"',
            '"Not:A-Brand";v="8"',
            '"Chromium";v="123"'
        ]
        sec_ch_ua_mobile = ['?0', '?1']
        sec_ch_ua_platform = ['"Windows"', '"Linux"', '"Macintosh"', '"Android"', '"iOS"']

        return {
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Dnt': '1',
            'Referer': f'https://ngl.link/{username}',
            'Sec-Ch-Ua': random.choice(sec_ch_ua),
            'Sec-Ch-Ua-Mobile': random.choice(sec_ch_ua_mobile),
            'Sec-Ch-Ua-Platform': random.choice(sec_ch_ua_platform),
            'User-Agent': UserAgent().random
        }

class deviceIDGenerator:
    def generate_deviceId(self):
        return '-'.join([''.join(random.choices(string.ascii_lowercase + string.digits, k=part_length))
                         for part_length in [8, 4, 4, 4, 12]])

if __name__ == "__main__":
    load_dotenv()
    url = os.getenv("URL")
    request_sender = RequestSender(url)
    username = input("Enter target username: ")
    spam_choice = input("Do you want to spam? (yes/no): ").lower().strip()
    message_input = input("Enter your message or leave blank to use a default message: ") or "Default message"

    if spam_choice in ["yes", "y", ""]:
        spam_count = input("How many times do you want to spam? (Default is 10000): ").strip()
        spam_count = int(spam_count) if spam_count.isdigit() else 10000

        for i in range(spam_count):
            message = message_input
            deviceId = deviceIDGenerator().generate_deviceId()
            referrer = ""
            response = request_sender.send_request_with_retry(username, message, deviceId)
            print(f'\n{i+1} of {spam_count}')
            print(f'{response.status_code} {response.reason} = {response.text}')
            print(f'message: {message}')
    else:
        message = message_input
        deviceId = os.getenv("DEVICE_ID")
        referrer = ""
        response = request_sender.send_request_with_retry(username, message, deviceId)
        print(f'{response.status_code} {response.reason} = {response.text}')
