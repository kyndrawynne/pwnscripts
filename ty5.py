from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def generate_valid_rsa_key():
    while True:
        p = rsa.generate_prime(256, backend=default_backend())
        q = rsa.generate_prime(256, backend=default_backend())
        n = p * q

        if 2**512 < n < 2**1024:
            e = 65537
            d = mod_inverse(e, (p-1)*(q-1))
            private_numbers = rsa.RSAPrivateNumbers(p=p, q=q, d=d, dmp1=d%(p-1), dmq1=d%(q-1), 
                                                    iqmp=mod_inverse(q, p), public_numbers=rsa.RSAPublicNumbers(e=e, n=n))
            private_key = private_numbers.private_key(backend=default_backend())
            return private_key

if __name__ == "__main__":
    private_key = generate_valid_rsa_key()
    print(f"Generated RSA Parameters:\n e = {private_key.public_key().public_numbers().e}\n n = {private_key.public_key().public_numbers().n}")

