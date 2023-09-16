import base64

# Your provided values
n = 0xaca3eda5534b5cfb0bfd4be1597fd6593e17a782e40966936427985ce0ece9c8406cacfd911813d23c049c74efd946000f34a9fc47558a424b565e9fcc15a2c04774c1660a9dc7cdeb634f743fc723a01b01d0e2531c9373e37fefc7ab1cb8631b062435bda926916b57e713481e2d0994ef9f3b288f9ad4bdfce61478d97fb5
d = 0xe2964552b80032094db325e49f9329c1f7bd141eb72d9f73d40023f9c33d2f99a4f4fe17d057c9ac2519e83f928d99527aa2a4787927cc4f3692259f963ccf5d647355d5f7e873a75974ffcaa97f54eeb33ad4ab4f32fac6f210663c1159da980d40458f67a0e68a0982e67c91e29d2a99428037e8455ab93ed816c451cfc1

# Secret ciphertext
secret_ciphertext_b64 = "+IbT9ZS/1s4VIAqdkkU+tzLZzMTivRLfTesew+e++6Vew3lHer1Vk6qYzb89YkbPeFFLTXAPwIHH+NIvTIOcen8bYPTDQT52O5uHONvZ18l/DfJ/KxfvR2wzwsFkWyZpRWspP5p/MWl5ruEM400cKoX40L8Gq43ZesJmJBY8KxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
secret_ciphertext_bytes = base64.b64decode(secret_ciphertext_b64)
secret_ciphertext_int = int.from_bytes(secret_ciphertext_bytes, 'big')

# Decryption using private key components (d and n)
flag_int = pow(secret_ciphertext_int, d, n)
flag_bytes = flag_int.to_bytes((flag_int.bit_length() + 7) // 8, 'big')

# Attempt to decode as ASCII
try:
    flag_str = flag_bytes.decode('utf-8').rstrip('\x00')
    print("ASCII decoded:", flag_str)
except UnicodeDecodeError:
    print("Unable to decode as ASCII.")
    print("Hexadecimal output:", flag_bytes.hex())
