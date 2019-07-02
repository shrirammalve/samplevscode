import requests
import math

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    test = "te"
    greeting = "hello,{}".format(who_to_greet)
    return greeting


""" print(greet("world"))
print(greet("shriram")) """
print(requests.get("https://slproweb.com/products/Win32OpenSSL.html").status_code)
print(r.ok)
