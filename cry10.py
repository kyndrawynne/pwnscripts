import base64
import hashlib

def find_response(challenge):
    counter = 0
    while True:
        # Convert counter to bytes and append to challenge
        response = challenge + counter.to_bytes(4, 'little')
        
        # Compute hash
        hash_result = hashlib.sha256(response).digest()

        # Check if the first two bytes are null
        if hash_result[:2] == b'\x00\x00':
            return counter.to_bytes(4, 'little')

        counter += 1

challenge_encoded = "TSPpnZfHUdXRXm9uz09rBBXlhWurt29aZT5VZk4k82o="
challenge_bytes = base64.b64decode(challenge_encoded)

response_bytes = find_response(challenge_bytes)
response_encoded = base64.b64encode(response_bytes).decode()

print(f"Response (b64): {response_encoded}")

