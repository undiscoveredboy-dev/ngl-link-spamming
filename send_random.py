'''
created by: ridwaanhall
date      : 16/04/2024
instagram : ridwaanhall

note: don't delete this watermark
'''

import os
import sys
import random
import string
import time
import logging
from dotenv import load_dotenv
import requests
from fake_useragent import UserAgent

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s - %(levelname)s] %(message)s')


class MessageGenerator:
    def __init__(self):
        self.generic_messages = [
            "Hey there! Just wanted to drop a quick message to say hi and see how you're doing. Hope you're having a great day! 😊",
            "Hi friend! Sending some positive vibes your way. Hope you're doing well!",
            "Hey buddy! Remember, you're awesome and capable of achieving anything you set your mind to! 💪",
            "Hello! Just checking in to see how you're doing. Let me know if there's anything I can do to support you!",
            "Hi! Wishing you a fantastic day filled with joy and laughter. Keep shining bright! ✨",
            "Hey! Hope your day is as amazing as you are! 😄",
            "Hi there! Just wanted to remind you that you're appreciated and valued. Keep being awesome!",
            "Hey friend! Just dropping by to say hello and spread some positivity your way. Have a wonderful day!",
            "Hello! Sending you lots of love and good vibes. You've got this!",
            "Hi! Remember, every challenge you face is an opportunity to grow stronger. Keep pushing forward!",
            "Hey there! Just wanted to send a quick virtual hug your way. You're not alone, and I'm here for you!",
            "Hi friend! Hope your day is filled with laughter, love, and all the good things in life. You deserve it!"
        ]
        
        self.messages_hacker = [
            "Initiating secure connection. Your digital presence is attracting attention. Stay vigilant. - ShadowCipher",
            "Warning: Unusual activity detected in your online behavior. Exercise caution. - DarkNetOp",
            "Cipher protocol activated. Your online actions have drawn scrutiny. Maintain discretion. - GhostHacker",
            "Alert: Anomaly detected in network traffic. You may be under surveillance. - StealthByte",
            "Security breach alert: Your digital footprint is being monitored. Take evasive action. - PhantomByte",
            "Caution: Digital surveillance detected. Your activities are being watched closely. - CyberPhantom",
            "Intrusion warning: Your online presence is under scrutiny. Stay under the radar. - CryptoGhost",
            "Encryption compromised. Your digital identity may be at risk. Take precautions. - ShadowCipher",
            "Attention: Suspicious network activity detected. Exercise heightened security measures. - DarkNetOp",
            "Security protocol breached. Your digital security may have been compromised. - GhostHacker",
            "Warning: Abnormal data flow detected in your network. Stay alert. - StealthByte",
            "Code red: Unauthorized access detected. Your online security is under threat. - PhantomByte",
            "Initiating secure transmission. Your digital activities have attracted attention. Stay covert. - CyberPhantom",
            "Caution: Anomalies detected in network traffic. Proceed with caution. - CryptoGhost",
            "Alert: Cipher protocol engaged. Your online presence may be compromised. - ShadowCipher",
            "Security breach detected. Your digital identity is vulnerable. Take action. - DarkNetOp",
            "Warning: Digital surveillance in progress. Maintain operational security. - GhostHacker",
            "Attention: Unusual patterns detected in your online behavior. Stay under the radar. - StealthByte",
            "Intrusion alert: Your online activities are being monitored. Stay low-key. - PhantomByte",
            "Encryption compromised. Your digital security may be compromised. Take evasive action. - CyberPhantom",
            "Alert: Suspicious network activity detected. Exercise caution in your online interactions. - CryptoGhost",
            "Security protocol breached. Your digital footprint is attracting unwanted attention. - ShadowCipher",
            "Code red: Unauthorized access detected. Take measures to protect your online security. - DarkNetOp",
            "Initiating secure communication. Your digital presence is under scrutiny. Maintain discretion. - GhostHacker",
            "Caution: Abnormal data flow detected. Your online activities may be compromised. - StealthByte",
            "Alert: Cipher protocol activated. Your digital security is at risk. Take precautions. - PhantomByte",
            "Security breach detected. Your digital privacy may be compromised. Take evasive action. - CyberPhantom",
            "Warning: Digital surveillance detected. Exercise caution in your online interactions. - CryptoGhost",
            "Attention: Unusual activity detected in your network. Stay alert. - ShadowCipher",
            "Intrusion warning: Your digital footprint has been noticed. Stay under the radar. - DarkNetOp",
            "Encryption compromised. Your online security may be compromised. Take action. - GhostHacker",
            "Alert: Suspicious network activity detected. Proceed with caution in your online activities. - StealthByte",
            "Security protocol breached. Your digital identity is vulnerable. Take evasive action. - PhantomByte",
            "Code red: Unauthorized access detected. Exercise caution in your digital interactions. - CyberPhantom",
            "Initiating secure transmission. Your digital presence is under surveillance. Stay covert. - CryptoGhost",
            "Caution: Anomalies detected in network traffic. Maintain operational security. - ShadowCipher",
            "Alert: Cipher protocol engaged. Your digital privacy may be compromised. - DarkNetOp",
            "Security breach detected. Your online activities are being monitored. Take action. - GhostHacker",
            "Warning: Digital surveillance in progress. Stay low-key in your online interactions. - StealthByte",
            "Attention: Unusual patterns detected in your online behavior. Exercise caution. - PhantomByte",
            "Intrusion alert: Your digital security may be compromised. Stay vigilant. - CyberPhantom"
        ]

    def generate_message(self):
        if random.random() < 1:
            return random.choice(self.messages_hacker)
        else:
            return random.choice(self.generic_messages)

class GameSlugGenerator:
    def __init__(self):
        self.game_slugs = [
            "",  
            "confessions",  
            "3words",  
            "tbh",  
            "shipme",  
            "yourcrush",  
            "cancelled",  
            "dealbreaker"  
        ]
        
    def generate_game_slug(self):
        return random.choice(self.game_slugs)


class RequestSender:
    '''
    This class sends requests to the specified URL.
    '''
    def __init__(self, url):
        '''
        Initializes the RequestSender with the specified URL.
        '''
        if not url:
            logging.error("URL must be provided")
            sys.exit(1)
        self.url = url
        self.user_agent = UserAgent()

    def send_request(self, username, question, device_id, game_slug, referrer=''):
        '''
        Sends a POST request to the specified URL with the provided parameters.
        '''
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
            response.raise_for_status()  # This will handle HTTP errors which are 400 and above
        except requests.exceptions.HTTPError as e:
            logging.error(f"HTTP Error: {e}")
            return None
        except requests.exceptions.RequestException as e:
            logging.error(f"Request Failed: {e}")
            return None
        return response

    def send_request_with_retry(self, username, question, device_id, game_slug, referrer='', max_retries=3):
        '''
        Sends a POST request to the specified URL with retry the provided parameters.
        '''
        retries = 0
        while retries < max_retries:
            response = self.send_request(username, question, device_id, game_slug, referrer)
            if response is None:
                logging.info("Request failed, retrying...")
                retries += 1
                time.sleep(2)
                continue
            
            if response.status_code == 404:
                logging.error("HTTP Error 404: Not Found. Stopping the program.")
                sys.exit(1)
            
            if response.status_code == 429:
                retry_after = int(response.headers.get('Retry-After', 10))
                logging.info(f"Rate limited. Retrying after {retry_after} seconds...")
                time.sleep(retry_after)
                retries += 1
                continue

            return response

        logging.error("Max retries reached. Failed to send request.")
        return None

    def _generate_headers(self, username):
        '''
        Generates headers for the request.
        '''
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

class DeviceIDGenerator:
    '''
    Generates device ID for the request.
    '''
    @staticmethod
    def generate_device_id():
        return '-'.join([''.join(random.choices(string.ascii_lowercase + string.digits, k=part_length))
                         for part_length in [8, 4, 4, 4, 12]])

if __name__ == "__main__":
    load_dotenv()
    url = os.getenv("URL")
    if not url:
        logging.error("No URL provided in environment. Exiting.")
        sys.exit(1)
    pesan = '''
    For better experience, please use a valid username.
    '''
    print(pesan)
    request_sender = RequestSender(url)
    username = input("Enter target username: ").strip()
    if not username:
        logging.error("Username is required. Exiting.")
        sys.exit(1)
    
    spam_choice = input("Do you want to spam? (yes/no): ").lower().strip()
    if spam_choice not in ["yes", "no", "y", "n", ""]:
        logging.error("Invalid choice for spam. Exiting.")
        sys.exit(1)

    device_generator = DeviceIDGenerator()
    message_generator = MessageGenerator()
    game_slug_generator = GameSlugGenerator()
    if spam_choice in ["yes", "y", ""]:
        spam_count = input("How many times do you want to spam? (Default is 9999): ")
        spam_count = int(spam_count) if spam_count.isdigit() else 9999

        # Determine the number of digits needed for the spam count
        count_format = f'{{:0{len(str(spam_count))}d}}'

        for i in range(spam_count):
            device_id = device_generator.generate_device_id()
            message_input = message_generator.generate_message()
            game_slug = game_slug_generator.generate_game_slug()
            
            response = request_sender.send_request_with_retry(username, message_input, device_id, game_slug)
            if response:
                try:
                    response_data = response.json()
                    question_id = response_data.get("questionId", "Unknown ID")
                    user_region = response_data.get("userRegion", "Unknown Region")
                    logging.info(f"({count_format.format(i+1)} of {count_format.format(spam_count)}) {response.status_code} {response.reason} {user_region} {username.upper()} -> {game_slug.upper()} '{message_input.upper()}'")
                except ValueError:
                    logging.error("Failed to decode JSON from response.")
            else:
                logging.error("Failed to send message.")
    else:
        device_id = device_generator.generate_device_id()
        message_input = message_generator.generate_message()
        game_slug = game_slug_generator.generate_game_slug()
        
        response = request_sender.send_request_with_retry(username, message_input, device_id, game_slug)
        if response:
            try:
                response_data = response.json()
                question_id = response_data.get("questionId", "Unknown ID")
                user_region = response_data.get("userRegion", "Unknown Region")
                logging.info(f"{response.status_code} {response.reason} {user_region} {username.upper()} {game_slug.upper()} -> '{message_input.upper()}'")
            except ValueError:
                logging.error("Failed to decode JSON from response.")
        else:
            logging.error("Failed to send message.")
