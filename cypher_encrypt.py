print("Select mode: encrypt or decrypt\n")
prompt_mode = input("e/d: ").lower()
message = input("Enter message to encrypt: ").lower()
shift = int(input("Enter shift value: "))


def message_enc(message, shift):
    if prompt_mode == "e":
        e_message = ""
        for char in message:
            if char.islower():
                e_message += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                e_message += char
    return e_message


print(message_enc(message, shift))
