import random
import string

def generate_random_deviceId():
    random_deviceId = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    random_deviceId += '-'
    random_deviceId += ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    random_deviceId += '-'
    random_deviceId += ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    random_deviceId += '-'
    random_deviceId += ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    random_deviceId += '-'
    random_deviceId += ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
    return random_deviceId

print(generate_random_deviceId())
