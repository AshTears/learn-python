# Caesar cipher
text = 'Hello Zaira'
shift = 3
custom_key = 'python'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def caesar_encode(message, offset):
    encrypted_text = ''
    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
        
    print('encrypted text:', encrypted_text)

caesar_encode(text, shift)

# Vigenere cipher
def vigenere(message, key):
    encrypted_text = ''
    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
        
    print('encrypted text:', encrypted_text)