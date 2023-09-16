import sys
import re

def main():
    # Read the HTTP request from standard input
    http_request = sys.stdin.read()

    # Extract the file path from the HTTP request using regex
    match = re.search(r'GET (/.*?) ', http_request)
    if match:
        file_path = match.group(1)
        # Print the file path to standard output
        print(file_path, end='')
    else:
        # If the request is not valid, print an error message or handle it accordingly
        print("ERROR: Invalid Request", end='')

if __name__ == "__main__":
    main()

