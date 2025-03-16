import os
import sys
import random
import time
import logging
from dotenv import load_dotenv
import requests
from fake_useragent import UserAgent
from generator import MessageGenerator, GameSlugGenerator, DeviceIDGenerator, UserRegionGenerator

# Predefined variables
username = "dps_juicy_tea_south"  # Set your target username here
spam_choice = "yes"  # Set "yes" to enable spam mode, "no" for single message
spam_count = 1000000000000  # Set number of spam messages if spam_choice is "yes"

logging.basicConfig(level=logging.INFO, format='[%(asctime)s - %(levelname)s] %(message)s')

class RequestSender:
    def __init__(self, url):
        if not url:
            logging.error("URL must be provided")
            sys.exit(1)
        self.url = url
        self.user_agent = UserAgent()

    def send_request(self, username, question, device_id, game_slug, referrer=''):
        headers = self._generate_headers(username)
        data = {
            'username': username,
            'question': question,
            'deviceId': device_id,
            'gameSlug': game_slug,
            'referrer': referrer
        }
        try:
            response = requests.post(self.url, headers=headers, data=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logging.error(f"Request Failed: {e}")
            return None
        return response

    def send_request_with_retry(self, username, question, device_id, game_slug, referrer='', max_retries=3):
        retries = 0
        while retries < max_retries:
            response = self.send_request(username, question, device_id, game_slug, referrer)
            if response is None:
                logging.info("Request failed, retrying...")
                retries += 1
                time.sleep(2)
                continue
            if response.status_code in [404, 429]:
                retry_after = int(response.headers.get('Retry-After', 10)) if response.status_code == 429 else 0
                logging.info(f"Retrying after {retry_after} seconds...")
                time.sleep(retry_after)
                retries += 1
                continue
            return response
        logging.error("Max retries reached. Failed to send request.")
        return None

    def _generate_headers(self, username):
        return {
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Dnt': '1',
            'Referer': f'https://ngl.link/{username}',
            'Sec-Ch-Ua': random.choice(['"Microsoft Edge";v="123"', '"Not:A-Brand";v="8"', '"Chromium";v="123"']),
            'Sec-Ch-Ua-Mobile': random.choice(['?0', '?1']),
            'Sec-Ch-Ua-Platform': random.choice(['"Windows"', '"Linux"', '"Macintosh"', '"Android"', '"iOS"']),
            'User-Agent': self.user_agent.random
        }

if __name__ == "__main__":
    load_dotenv()
    url = os.getenv("URL")
    if not url:
        logging.error("No URL provided in environment. Exiting.")
        sys.exit(1)
    
    request_sender = RequestSender(url)
    device_generator = DeviceIDGenerator()
    message_generator = MessageGenerator()
    game_slug_generator = GameSlugGenerator()
    
    if spam_choice.lower() in ["yes", "y"]:
        count_format = f'{{:0{len(str(spam_count))}d}}'
        for i in range(spam_count):
            device_id = device_generator.generate_device_id()
            message_input = message_generator.generate_message()
            game_slug = game_slug_generator.generate_game_slug()
            response = request_sender.send_request_with_retry(username, message_input, device_id, game_slug)
            if response:
                logging.info(f"({count_format.format(i+1)} of {count_format.format(spam_count)}) {response.status_code} {response.reason} {username.upper()} -> '{game_slug.upper()}'")
            else:
                logging.error("Failed to send message.")
    else:
        device_id = device_generator.generate_device_id()
        message_input = message_generator.generate_message()
        game_slug = game_slug_generator.generate_game_slug()
        response = request_sender.send_request_with_retry(username, message_input, device_id, game_slug)
        if response:
            logging.info(f"{response.status_code} {response.reason} {username.upper()} {game_slug.upper()} -> '{message_input.upper()}'")
        else:
            logging.error("Failed to send message.")
