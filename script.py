import requests
import sys

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "hello,{}".format(who_to_greet)
    return greeting


print(greet("world"))
print(greet("shriram"))
r = requests.get("https://slproweb.com/products/Win32OpenSSL.html")
print(r.ok)

