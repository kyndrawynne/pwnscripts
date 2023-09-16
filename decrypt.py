key = open('key.bin', 'rb').read()
secret = open('secret.bin', 'rb').read()

result = bytes(a ^ b for a, b in zip(key, secret))

print(result.decode('utf-8'))
