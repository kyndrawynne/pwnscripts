from Crypto.PublicKey import RSA

# Generate RSA key pair
key = RSA.generate(1024)

challenge_hex = "0x8a3015d1147378cbf7f001076206670f425a73976cdb6772ab3f69aa80f4328b2223b0ed843450521ffdc8152dfc9ed453a5c400d6514f1c9690c482134040dc"
challenge_int = int(challenge_hex, 16)

response_int = pow(challenge_int, key.d, key.n)
print(f"response: {hex(response_int)}")
