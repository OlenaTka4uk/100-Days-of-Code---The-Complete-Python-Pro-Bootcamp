alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(original_text, shift_amount, direction):
    cipher_text = ""

    if direction == "decode":
            shift_amount *= -1

    for char in original_text:
        if char not in alphabet:
            cipher_text += char
        else:
            shifted_position = alphabet.index(char) + shift_amount
            shifted_position = shifted_position % len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the {direction}d result: {cipher_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(original_text=text, shift_amount=shift, direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")



