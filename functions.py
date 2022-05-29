from time import perf_counter
import string
from itertools import product
import secrets


def typpe(type):
    tyyppi = []
    if type == 0:
        tyyppi = list(string.printable)
    elif type == 1:
        tyyppi = list(string.digits)
    else:
        tyyppi = list(string.ascii_letters) 
    return tyyppi


def cracker(passw, type):
    # Specify the type of the passwords for more accurate simulation
    tyyppi = typpe(type)
    # Convert password into tuple
    pWord = tuple(passw)
    # Start a counter to measure the time to crack the password
    start = perf_counter()
    # Loop through all the combinations
    for i in product(tyyppi, repeat=len(passw)):
        # Check against the password
        if i == pWord:
            # End the counter
            end = perf_counter()
            # Calculate the time
            elapsed = end-start
            # convert the tuple to string
            ret = ''.join(i)
            return ret, round(elapsed,2)
    # If no match is found i.e. wrong type
    return "Error", 404 


# def generator(type, length):
#     tyyppi = typpe(type)
#     passw = ''.join(secrets.choice(tyyppi) for i in range(length))
#     return passw