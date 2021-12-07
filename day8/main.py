# Ceasar Cipher
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
run_again = True

def encrypt(plain_text, shift_amount):
    # function to encrypt
    encrypted_text = ""
    for char in plain_text:
        if char not in alphabet:
            encrypted_text += char
        else:
            index_position = alphabet.index(char)
            shift_index = index_position + shift_amount
            if shift_index > len(alphabet):
                shift_index %= len(alphabet)
                encrypted_text += alphabet[shift_index]
            else:
                encrypted_text += alphabet[shift_index]
    print("The encoded text is %s " % encrypted_text)

def decrypt(cipher_text, shift_amount):
    # function to decrypt
    decrypted_text = ""
    for char in cipher_text:
        if char not in alphabet:
            decrypted_text += char
        else:
            index_position = alphabet.index(char)
            shift_index = index_position - shift_amount
            decrypted_text += alphabet[shift_index]
    print("The decoded text is %s" % decrypted_text) 

def user_inputs():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction.lower() == 'encode':
        encrypt(text, shift)
    elif direction.lower() == 'decode':
        decrypt(text, shift)
    else:
        print("not a valid entry, please type 'encode' or 'decode'")

print(art.logo)

user_inputs()
while run_again:
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no' \n")
    if restart.lower() == 'no':
        run_again = False
        print("Goodbye!")
    else:
        user_inputs()
