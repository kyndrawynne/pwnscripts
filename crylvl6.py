import base64

# The secret ciphertext in base64
ciphertext_b64 = "joiR0ZyQk5MNzcnxC8NFJ3ZAntlrC79/kQbcvgkx/Qg1Vm/MqZRE8K06NiGKEIH59uNTodvOXcx+jA=="
ciphertext = base64.b64decode(ciphertext_b64)

# The shared secret 's'
p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca18217c32905e462e36ce3be39e772c180e86039b2783a2ec07a28fb5c55df06f4c52c9de2bcbf6955817183995497cea956ae515d2261898fa051015728e5a8aacaa68fffffffffffffffe
s_bytes = (p - 1).to_bytes(256, "little")

# XOR the ciphertext with the shared secret to get the plaintext
plaintext = bytes([c ^ s for c, s in zip(ciphertext, s_bytes)])

print(plaintext.decode())

