import string

# Function to handle encryption and decryption with Caesar Cipher
def caesar_cipher(text, shift, decrypt=False, case_insensitive=False):
    shift = shift % 26  # Normalize shift to 0-25 to handle negative or large shifts
    if decrypt:
        shift = -shift  # Reverse shift for decryption
    if case_insensitive:
        text = text.lower()

    result = ""
    for char in text:
        if char.isalpha():  # Shift letters only
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep non-alphabetic characters as they are
    return result

# Function to validate inputs
def validate_shift(shift):
    try:
        return int(shift) % 26  # Normalize shift to the range of 0-25
    except ValueError:
        print("Shift must be a valid number. Try again.")
        return None

# Function to validate password input
def validate_password():
    password = input("Set a password for this file: ")
    confirm_password = input("Confirm your password: ")
    if password == confirm_password:
        return password
    else:
        print("Passwords do not match. Try again.")
        return validate_password()

# Function to encrypt text
def encrypt(text, shift, case_insensitive=False):
    return caesar_cipher(text, shift, decrypt=False, case_insensitive=case_insensitive)

# Function to decrypt text
def decrypt(text, shift, case_insensitive=False):
    return caesar_cipher(text, shift, decrypt=True, case_insensitive=case_insensitive)

# Function to load text from a file with optional password protection
def load_text_from_file(filename, password=None):
    try:
        with open(filename, "r") as file:
            file_content = file.read().splitlines()
            if password and file_content[0] != password:
                print("Error: Incorrect password.")
                return None
            return "\n".join(file_content[1:]) if password else "\n".join(file_content)
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None

# Function to save text to a file with optional password protection
def save_text_to_file(filename, text, password=None):
    with open(filename, "w") as file:
        if password:
            file.write(password + "\n")
        file.write(text)
    print(f"Text successfully saved to {filename}")

# Function to crack Caesar Cipher using frequency analysis (placeholder)
def crack_caesar_cipher(ciphertext):
    print("Cracking the cipher using frequency analysis is a complex feature.")
    print("Future implementation will be added here.")

# Function to visually represent the Caesar Cipher shift
def display_shift_visual(text, shift):
    shifted_text = caesar_cipher(text, shift)
    print("\nOriginal Text:  ", text)
    print("Shifted Text:   ", shifted_text)
    print("Shift Value:    ", shift)
    print("Visual Representation:")
    for original_char, shifted_char in zip(text, shifted_text):
        if original_char.isalpha():
            print(f"{original_char} -> {shifted_char}")
        else:
            print(f"{original_char} (no change)")

# Main function with extended features
def main():
    print("=== Caesar Cipher Program ===")
    print("\nMenu Options:")
    print("1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Load Text from File")
    print("4. Save Text to File")
    print("5. Visualize Caesar Cipher Shift")
    print("6. Crack Encrypted Message")
    print("7. Quit Program\n")

    text = ""
    while True:
        choice = input("Choose an option (1-7): ").strip()

        if choice == '7':
            print("Exiting program.")
            break
        elif choice == '3':
            filename = input("Enter filename to load from: ")
            password_protected = input("Is the file password-protected (y/n)? ").lower() == 'y'
            password = input("Enter password: ") if password_protected else None
            text = load_text_from_file(filename, password)
            if text is None:
                continue
        elif choice == '4':
            filename = input("Enter filename to save to: ")
            password_protected = input("Would you like to protect this file with a password (y/n)? ").lower() == 'y'
            password = validate_password() if password_protected else None
            save_text_to_file(filename, text, password)
            continue
        elif choice in ['1', '2']:
            text = input("Enter the message: ") if choice == '1' else input("Enter the encrypted message: ")
            shift = None
            while shift is None:
                shift_input = input("Enter the shift value (negative or positive): ")
                shift = validate_shift(shift_input)

            case_insensitive = input("Ignore case (y/n)? ").lower() == 'y'

            if choice == '1':
                encrypted_message = encrypt(text, shift, case_insensitive)
                print("Encrypted message:", encrypted_message)
                text = encrypted_message
            else:
                decrypted_message = decrypt(text, shift, case_insensitive)
                print("Decrypted message:", decrypted_message)
                text = decrypted_message
        elif choice == '5':
            text = input("Enter the message to visualize the shift: ")
            shift = None
            while shift is None:
                shift_input = input("Enter the shift value (negative or positive): ")
                shift = validate_shift(shift_input)
            display_shift_visual(text, shift)
        elif choice == '6':
            ciphertext = input("Enter the encrypted message to crack: ")
            crack_caesar_cipher(ciphertext)
        else:
            print("Invalid option. Please choose a valid action.")

# Run the program
if __name__ == "__main__":
    main()
