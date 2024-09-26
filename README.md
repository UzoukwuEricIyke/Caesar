This project is part of my internship with Prodigy InfoTech, and I’m excited to share it with the community.

Features
- Encrypt Messages: Secure your message with this Caesar Cipher, using customizable shift values.
- Decrypt Messages: Decrypt messages encrypted with the Caesar Cipher by providing the correct shift value.
- Negative Shift Handling: Supports both positive and negative shift values.
- Case Insensitivity: You can choose whether to make the encryption case-sensitive or ignore letter casing entirely.
- File Handling: Load messages from files and save the results (encrypted/decrypted) into files.
- Password Protection for Files: Add password protection to your files for added security.
- Crack Encrypted Messages: Using *frequency analysis*, the tool can automatically crack encrypted messages without knowing the shift.
- Visual Representation: See a detailed breakdown of how each character is shifted during the encryption process.

Requirements
Python  3.12.6 installed on your system.
No additional dependencies are required.

How to Use
1. Clone the repository:
   `git clone https://github.com/UzoukwuEricIyke/PRODIGY_CS_01`

2. `cd caesarcipher.py`

3. Run the program:
   `python caesarcipher.py`

4. Menu Options:
   After launching, you will be greeted with a menu.

Here's a quick breakdown of the available options:
   1. Encrypt Text: Encrypt a message by providing the shift value and other preferences.
   2. Decrypt Text: Decrypt a message by specifying the shift used during encryption.
   3. Load Text from File: Load text from a file to either encrypt or decrypt it.
   4. Save Text to File: Save the resulting encrypted/decrypted message to a file with optional password protection.
   5. Visualize Caesar Cipher Shift: View a visual representation of how characters are shifted in the cipher.
   6. Crack Encrypted Message: Crack an encrypted message using frequency analysis, without needing the shift.
   7. Quit: Exit the program.


Example

Encrypting a Message:

Enter the message: HELLO WORLD

Enter the shift value: 3

Ignore case (y/n)? n

Encrypted message: KHOOR ZRUOG



Cracking a Cipher:

Enter the encrypted message to crack: KHOOR ZRUOG

Best shift found: 3

Decrypted message: HELLO WORLD



Visual Representation of Shift:

Original Text:   HELLO

Shifted Text:    KHOOR

Shift Value:     3

H -> K

E -> H

L -> O

L -> O

O -> R

Feel free to fork this project and submit pull requests. I’m open to contributions, especially to improve the *frequency analysis* cracking algorithm or introduce new features.


If you have any questions or feedback, please contact me or open an issue in this repository:

  *Uzoukwu Eric Ikenna*  
  Email: [uzoukwuericiyke@yahoo.com](mailto:uzoukwuericiyke@yahoo.com)
  LinkedIn - https://www.linkedin.com/in/uzoukwu-eric-ikenna/

Notes:
Make sure to update the `git clone` URL to match your repository.
