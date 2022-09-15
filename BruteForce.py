from itertools import product


def findPassword(chars, function, show=50, format_="%s"):

    password = None
    attempts = 0
    size = 1
    stop = False

    while not stop:

        # Gets all possible combinations with the digits of the "chars" parameter.
        for pw in product(chars, repeat=size):

            password = "".join(pw)

            # Prints the password that will be tried.
            if attempts % show == 0:
                print(format_ % password)

            # Checks if the password is correct.
            if function(password):
                stop = True
                break
            else:
                attempts += 1
        size += 1

    return password, attempts


def getChars():
    """
    Method to get a list containing all the
    alphabet letters and numbers.
    """
    chars = []

    # Adds all capital letters to the list
    for id_ in range(ord("A"), ord("Z") + 1):
        chars.append(chr(id_))

    # Adds all lowercase letters to the list
    for id_ in range(ord("a"), ord("z") + 1):
        chars.append(chr(id_))

    # Adds all numbers to the list
    for number in range(10):
        chars.append(str(number))

    return chars


# If this module is not imported, the program will be tested.
# To perform the test, the user must enter a password to be found.

if __name__ == "__main__":

    import datetime
    import time

    # Ask the user for a password
    pw = input("\n Type a password: ")
    print("\n")

    def testFunction(password):
        global pw
        if password == pw:
            return True
        else:
            return False

    # Gets the digits a password can have
    chars = getChars()

    t = time.process_time()

    # Get the password found and the number of attempts
    password, attempts = findPassword(
        chars, testFunction, show=1000, format_=" Trying %s"
    )

    t = datetime.timedelta(seconds=int(time.process_time() - t))
    input(f"\n\n Password found: {password}\n Attempts: {attempts}\n Time: {t}\n")