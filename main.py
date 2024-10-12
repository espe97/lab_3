alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabet_size = len(alphabet)

def text_to_indices(text, alphabet):
    return [alphabet.index(char) for char in text.upper() if char in alphabet]
def indices_to_text(indices, alphabet):
    return ''.join([alphabet[i % alphabet_size] for i in indices])

def encrypt(message, gamma, alphabet):
    message_indices = text_to_indices(message, alphabet)
    gamma_indices = text_to_indices(gamma, alphabet)
    
    encrypted_indices = []
    
    for i in range(len(message_indices)):
        encrypted_index = (message_indices[i] + gamma_indices[i % len(gamma_indices)]) % alphabet_size
        encrypted_indices.append(encrypted_index)
    
    return indices_to_text(encrypted_indices, alphabet)

def decrypt(encrypted_message, gamma, alphabet):
    encrypted_indices = text_to_indices(encrypted_message, alphabet)
    gamma_indices = text_to_indices(gamma, alphabet)
    
    decrypted_indices = []
    
    for i in range(len(encrypted_indices)):
        decrypted_index = (encrypted_indices[i] - gamma_indices[i % len(gamma_indices)]) % alphabet_size
        decrypted_indices.append(decrypted_index)
    
    return indices_to_text(decrypted_indices, alphabet)

while True: 
    
    action = input("Put '1' for encryption and '2' for decryption: ")
    
    if action == alphabet:
        break

    message = input("Put your message here:")
    gamma = input("Put your gamma here:")

    if action == '1':
        encrypted_message = encrypt(message,gamma,alphabet)
        print(f"Your encrypted messgae is:{encrypted_message}")
        
    elif action == '2':
        decrypt_message = decrypt(message,gamma,alphabet)
        print(f"Your decrypted message:{decrypt_message}")

    else:
        print("Choose option 1 or 2")    