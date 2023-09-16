import base64

# Convert hex values to integers
e = 0x10001
p = 0xc4e1d5d6bdf328e68fba52afcd2789cbb6b3b1cd356934c41d150d16e033653a74624c33f12cf0d076b720fbcfe63b78535a6cc1f533db18954a3962336877420167134cbf84efa5cfe465920d09988def726525686cdce49290e8d65cd89652ad55ab7c0f26ebb6f98e21bdf9ce654414cc8e399aa30ced2f980ec157fbcdf7
q = 0xea958a4dabeef078a643cca1bc929b3998bcfd0c3e5b0ad17c582d5624d2b6638323df5b6671644cc924d82ca226242b3fafce921711fdb2a5611c0a3f12dcf126c426710c83c93f552b1099211bdd9780069c3b23a63b91d8fee705f2f3bbf0b5e0aa3a5576c815e4855a6dc7b22e59e7b3200092562c36e33d19136a8779b5
b64_ciphertext = "w26T6V4QFaZkqiFqKAisn1ySBFvk5Ahx4Zvb5/2hyfl5kRZPMoswOp2U+Lk0pZljR/++DvMqW1QdpvSdaKSMo2Z7b0bLSNlL0peHklH+x8/m8E8DPIJteSlMM+3YhkcrzTh1IY+FGw9IZtBF/od/xRLKSekFPVAuvBneSIqkEXU6q3b4JPRdKeMGbHEprL2vw6OPzb+tauI9UTpOgyEKOOuSNP9Giw8WCu/k9FFiXuGKJL/jDH89HV3w7FcwxwDgMkQVnJHZr3QC6JeaEJGIQAtHkxK1hjhQaspfrhIWMKp6+FfYZGozRM6noTGHaFBuy5OWQTjxcmSptfQPfHavhg=="

# Compute n and phi(n)
n = p * q
phi_n = (p-1) * (q-1)

# Modular inverse function
def modinv(a, m):
    m0 = m
    x0 = 0
    x1 = 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Compute the private key d
d = modinv(e, phi_n)

# Decrypt the ciphertext
ciphertext_int = int.from_bytes(base64.b64decode(b64_ciphertext), 'little')
plaintext_int = pow(ciphertext_int, d, n)
plaintext_bytes = plaintext_int.to_bytes((plaintext_int.bit_length() + 7) // 8, 'little')

print(plaintext_bytes.decode())
