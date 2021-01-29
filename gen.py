import os
from urllib import parse

images = sorted(os.listdir("images"))

print("const images = [")

for i in images:
    if i.startswith("."):
        continue
    enc = parse.quote_plus(i).replace("+", "%20")
    print(f"    \"images/{enc}\",")
print("];")
