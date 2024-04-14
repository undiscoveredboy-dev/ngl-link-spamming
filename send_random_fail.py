import os
import random
import string
import time
import logging
import argparse
from dotenv import load_dotenv
import requests
from fake_useragent import UserAgent

class RequestSender:
    def __init__(self, url):
        self.url = url
        self.user_agent = UserAgent()
        self.session = requests.Session()
        self.session.headers = {'User-Agent': self.user_agent.random}

    def send_request(self, username, question, deviceId, gameSlug='', referrer=''):
        headers = self._generate_headers(username)
        data = {
            'username': username,
            'question': question,
            'deviceId': deviceId,
            'gameSlug': gameSlug,
            'referrer': referrer
        }
        try:
            response = requests.post(self.url, headers=headers, data=data)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as errh:
            self.logger.error(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            self.logger.error(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            self.logger.error(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            self.logger.error(f"OOps: Something Else {err}")

    def send_request_with_retry(self, username, question, deviceId, gameSlug='', referrer='', max_retries=3):
        retries = 0
        while retries < max_retries:
            response = self.send_request(username, question, deviceId, gameSlug, referrer)
            if response and response.status_code == 429:
                retry_after = int(response.headers.get('Retry-After', 10))
                self.logger.info(f"Rate limited. Retrying after {retry_after} seconds")
                time.sleep(retry_after)
                retries += 1
            elif response and response.status_code == 200:
                return response
            else:
                break
        self.logger.error("Max retries reached. Failed to send request.")
        return None

    def _generate_headers(self, username):
        return {
            'User-Agent': self.user_agent.random,
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Dnt': '1',
            'Referer': f'https://ngl.link/{username}'
        }

class DeviceIDGenerator:
    @staticmethod
    def generate_deviceId():
        parts = [8, 4, 4, 4, 12]
        return '-'.join(''.join(random.choices(string.ascii_lowercase + string.digits, k=part)) for part in parts)

class MessageGenerator:
    def __init__(self, messages=None):
        self.messages = messages if messages else [
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
        return random.choice(self.messages)

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def parse_arguments():
    parser = argparse.ArgumentParser(description="Send automated messages using specified configurations.")
    parser.add_argument("-u", "--username", required=True, help="Target username")
    parser.add_argument("-m", "--message", help="Specific message to send. Randomized if not specified.")
    parser.add_argument("-c", "--count", type=int, default=1, help="Number of messages to send")
    parser.add_argument("-s", "--slug", help="Game slug to use. Randomized if not specified.")
    return parser.parse_args()

if __name__ == "__main__":
    load_dotenv()
    setup_logging()
    args = parse_arguments()

    url = os.getenv("URL")
    request_sender = RequestSender(url)
    message_generator = MessageGenerator()

    for _ in range(args.count):
        message = args.message or message_generator.generate_message()
        gameSlug = args.slug or ""
        deviceId = DeviceIDGenerator.generate_deviceId()
        response = request_sender.send_request_with_retry(args.username, message, deviceId, gameSlug)
        if response:
            logging.info(f'Successfully sent: {response.status_code} - {response.text}')
        else:
            logging.error('Failed to send the message')
