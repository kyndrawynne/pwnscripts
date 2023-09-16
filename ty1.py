from Crypto.Util.number import inverse

def decrypt_challenge(p, q, e, challenge):
    # Compute phi(n)
    phi_n = (p-1) * (q-1)
    
    # Compute the modular inverse of e modulo phi(n)
    d = inverse(e, phi_n)
    
    # Compute n
    n = p * q
    
    # Decrypt the challenge
    m = pow(challenge, d, n)
    return m

# Parameters
e = 65537
p = # Your prime p value
q = # Your prime q value
challenge = 0xe75f62d5e3db145a752b43df9bbc223f0794fe5f233555efffa70a9ed3550ca1c5eb6ac1501079710711cb82ee75d0d86a3d6ad0e7ac18dbb81ba6708cb90c8e 
response = decrypt_challenge(p, q, e, challenge)
print(hex(response))

