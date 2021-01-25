import os
from urllib import parse

images = os.listdir("images")

print("const images = [")

for i in images:
    enc = parse.quote_plus(i).replace("+", "%20")
    print(f"    \"images/{enc}\",")
print("];")
