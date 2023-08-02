from jwt import JWT, jwk_from_dict, exceptions
from datetime import datetime, timedelta

jwt = JWT()

# Get the current local time
current_time = datetime.now()

# Set the expiration time to 5 minute from the current local time
expiration_time = current_time + timedelta(minutes=5)

# Convert the expiration time to a Unix timestamp
expiration_timestamp = int(expiration_time.timestamp())

payload = {'username': 'purvesh', 'exp': expiration_timestamp}

jwk_dict = {
    "kty": "oct",
    "k": "123456"
}

key = jwk_from_dict(jwk_dict)
token = jwt.encode(payload, key)

print("Token:", token)

# Decode and verify the token
try:
    decoded_token = jwt.decode(token, key)
    print("Decoded token:", decoded_token)
except exceptions.JWTDecodeError as e:
    print(f"error: {e}")
