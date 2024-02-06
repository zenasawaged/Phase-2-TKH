import sys
#DEFINE VARIABLES    
message = "helloworld"
k = 10
# UTILIZED ENCRYPT FUNCTION TO START ENCRYPTING
def encrypt(message, k):
    great = [] #To access elements in cypher code
    for x in message: # creating for loop of message    
        numer = ord(x) # returns Unicode code from a given character
        char = numer + k # define char
        if char > ord("z"): # if statement to ensure after z we return to a 
            char -= 26 #26 REPRESENT "Z" 
        great.append(chr(char)) #add each character 
    my_string = ''.join(great) #join helloworld instead of creating singular characters
    return my_string  
# UTILIZED DECRYPT FUNCTION TO START DECRYPTING
def decrypt(message, k): 
    great = []
    for x in message: 
        numer = ord(x)
        char = numer - k
        if char < ord("a"): # if statement to ensure after "a" we return to "z"
            char += 26 #26 REPRESENT "Z"
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
