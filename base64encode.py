import base64
from sys import argv
  
username = argv[1]
password = argv[2]
ascii_encoded = (argv[1]+":"+argv[2]).encode("ascii")
  
base64_bytes = base64.b64encode(ascii_encoded)
base64_string = base64_bytes.decode("ascii")
  
print(f"Encoded string: {base64_string}")