import hashlib
import base64

def sha256(data):
    m = hashlib.sha256()
    m.update(data)
    return m.digest()

def find_collision(target):
    # Convert the base64 encoded hash to bytes
    target_bytes = base64.b64decode(target)
    
    # Since it's just 2 bytes (16 bits), we have a maximum of 2^16 possibilities
    for i in range(0, 2**16):
        # Convert the integer i to bytes (this step is arbitrary, you can hash any form of data)
        data = i.to_bytes(2, byteorder='big')  
        hash_bytes = sha256(data)
        
        # Check only the first 2 bytes of the hash
        if hash_bytes[:2] == target_bytes[:2]:
            return base64.b64encode(data).decode('utf-8')

    return None

# Given target hash
target = "HUw="
collision = find_collision(target)
print("Collision (b64):", collision)
