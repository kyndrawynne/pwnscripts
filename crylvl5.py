import base64
import subprocess

CHALLENGE_EXECUTABLE = "/challenge/run"

def interact_with_challenge(input_data):
    """Interact with the challenge binary and return the ciphertext."""
    process = subprocess.Popen([CHALLENGE_EXECUTABLE], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, _ = process.communicate(input=input_data.encode())
    return stdout.decode()

def detect_block_size():
    """Detect the block size used by the encryption."""
    for i in range(1, 65):
        input_data = base64.b64encode(b'A' * i).decode()
        response = interact_with_challenge(input_data)
        ciphertext = base64.b64decode(response.split("ciphertext (b64): ")[1].strip())

        # Check for repeated blocks in the ciphertext
        blocks = [ciphertext[j:j+16] for j in range(0, len(ciphertext), 16)]
        for block in blocks:
            if blocks.count(block) > 1:
                return len(block)

    raise ValueError("Unable to detect block size")

def ecb_byte_at_a_time_attack():
    block_size = 16
    discovered_secret = b""

    for _ in range(block_size * 2):  # Assuming the secret is at most 2 block sizes
        input_padding = b'A' * (block_size - 1 - (len(discovered_secret) % block_size))
        input_data = base64.b64encode(input_padding).decode()
        
        print(f"Payload: {input_padding}")
        response = interact_with_challenge(input_data)
        print(f"Response: {response}")
        target_ciphertext = base64.b64decode(response.split("ciphertext (b64): ")[1].strip())
        print(f"Ciphertext: {target_ciphertext}")

        for byte_val in range(256):
            test_input = input_padding + discovered_secret + bytes([byte_val])
            test_data = base64.b64encode(test_input).decode()
            response = interact_with_challenge(test_data)
            test_ciphertext = base64.b64decode(response.split("ciphertext (b64): ")[1].strip())

            if test_ciphertext[:len(test_input)] == target_ciphertext[:len(test_input)]:
                discovered_secret += bytes([byte_val])
                break

        # Optional: Print progress
        print(discovered_secret)

    return discovered_secret

if __name__ == "__main__":
    secret = ecb_byte_at_a_time_attack()
    print("Discovered Secret:", secret)

