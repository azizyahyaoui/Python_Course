import random, string


def encrypt(msg):
    pass









def main():
    print("-------------------------------------------------------------------------------------------------")

    
    chars = " " + string.ascii_letters + string.digits + string.punctuation # all possible characters '94#'
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)
    
    # Encrypt the message
    plain_text = input("Enter the message to encrypt: ")
    cipher_text = ""

    for char in plain_text:
        if char in chars:
            index = chars.index(char)
            cipher_text += key[index]


    print(f"Plain text: {plain_text}")
    print(f"Encrypted message: {cipher_text}")
    
    # Decrypt the message
    decrypted_text = ""

    for char in cipher_text:
        if char in key:
            index = key.index(char)
            decrypted_text += chars[index]
    
    print(f"Decrypted message: {decrypted_text}")





    print()
    print("-------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()
