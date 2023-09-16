hex_output = "3ad52473ea8f529627b54c902fca946075763a5423ea5e1c60990c63cf0ca264992a6f7f0cbfa073b47b883847cda1ec468580bfc3ce942554f0fccf98b1c44969e4755327aed08f29716c44f3dcad64cf703ad8f54a14b69a2532f38933dc552eeb11e3ba237dab9ec35b8a3636fa95103f0b9b1a3e15151c145ebd06ca9f06"

# Convert the hex string to bytes
byte_data = bytes.fromhex(hex_output)

# Convert byte_data to ASCII
try:
    ascii_output = byte_data.decode('utf-8')
except:
    ascii_output = None

# Check if we have the flag pattern
if ascii_output and "pwn.college" in ascii_output:
    print(ascii_output)
else:
    print("Unable to find flag pattern in the output.")
