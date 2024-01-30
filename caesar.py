import sys

message = "helloworld"
k = 10

def encrypt(message, k):
    great = []
    for x in message:
        numer = ord(x)
        char = numer + k
        if char > ord("z"):
            char -= 26
        great.append(chr(char))
    my_string = ''.join(great)
    return my_string

def decrypt(message, k):
    great = []
    for x in message: 
        numer = ord(x)
        char = numer - k
        if char < ord("a"):
            char += 26
        great.append(chr(char))
    my_string = ''.join(great)
    return my_string


if __name__ == "__main__":
    # take in first arg as word
    message = sys.argv[1]
    # take in second arg as int key
    key = int(sys.argv[2])

    # encrypt your word
    encrypted = encrypt(message, key)

    # decrypt your encrypted word
    decrypted = decrypt(encrypted, key)

    print("Your encrypted word is", encrypted)
    print("Your decrypted word is", decrypted)
