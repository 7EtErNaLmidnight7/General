LETTERS = "abcdefghijklmnopqrstuvwxyz "
KEY = "turnip".lower() # You can change this to anything (No special characters/numbers)
# TODO, try to abstract the code, so there are less lines

def encrypt(msg):
    i = 0 # Incrementing value
    encrypted_msg = ""

    for letter in list(msg.lower()):

        if letter in LETTERS:
            letter_index = LETTERS.index(letter) # Finidng index of the character
            key_index = LETTERS.index(KEY[i % len(KEY)]) # Finding the index of the correct key

            encrypted_letter = LETTERS[(letter_index + key_index) % len(LETTERS)]
        
        else:
            encrypted_letter = letter # Making sure code works with special characters
        
        encrypted_msg = encrypted_msg + encrypted_letter
        i = i + 1  

    return encrypted_msg


def decrypt(msg): # This is just a repeat of the encrypt() with a small change...
    i = 0
    encrypted_msg = ""

    for letter in list(msg):

        if letter in LETTERS:
            letter_index = LETTERS.index(letter)
            key_index = LETTERS.index(KEY[i % len(KEY)])

            encrypted_letter = LETTERS[(letter_index - key_index) % len(LETTERS)] # Here, a "+" to a "-" WOW!
        
        else:
            encrypted_letter = letter
        
        encrypted_msg = encrypted_msg + encrypted_letter
        i = i + 1  

    return encrypted_msg