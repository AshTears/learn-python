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
    key_index = 0
    encrypted_text = ''
    for char in message.lower():
        # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index+=1
            # Define the offset and the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
        
    return encrypted_text

print(vigenere(text, custom_key))