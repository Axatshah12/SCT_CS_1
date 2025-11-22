 Caesar Cipher – Python Encryption & Decryption Tool

A clean and simple Python implementation of the Caesar Cipher, a classic cryptographic technique used for shifting characters in plaintext.
This project demonstrates fundamental concepts of encryption, ASCII manipulation, loops, and modular arithmetic.

 Overview

The Caesar Cipher is one of the oldest known encryption methods, famously used by Julius Caesar to secure military messages.
This program allows users to:

✔ Encrypt plaintext
✔ Decrypt ciphertext
✔ Use any shift value between 1–25
✔ Preserve case and punctuation

It’s a great beginner-friendly cryptography project that strengthens logic-building and Python fundamentals.

✨ Features

🔐 Encrypt text using a chosen shift value

🔓 Decrypt previously encrypted text

🔤 Preserves uppercase/lowercase

🔣 Keeps numbers, spaces & punctuation unchanged

🧮 Uses ASCII-based character shifting

💻 Interactive command-line interface

 Project Structure
SCT_CS_1/
│
├── caesar_cipher.py        # Main program (user interface)
├── encrypt.py              # Encryption logic
├── decrypt.py              # Decryption logic
├── README.md               # Project documentation
└── (optional: screenshots/)

🧠 How the Cipher Works

Each letter is shifted by n positions:

Encryption Formula:

E(x) = (x + n) mod 26


Decryption Formula:

D(x) = (x - n) mod 26


Where:

x = letter index (0–25)

n = shift value

mod 26 ensures wrap-around (Z → A)

▶️ Usage

Run the program:

python caesar_cipher.py


Follow the on-screen menu:

Encrypt a message

Decrypt a message

Exit

🧪 Example Output
=== Caesar Cipher Encryption/Decryption Tool ===

Choose an option:
1. Encrypt a message
2. Decrypt a message
3. Exit

Enter your choice (1/2/3): 1
Enter the message to encrypt: Hello World
Enter the shift value (1-25): 3

Encrypted message: Khoor Zruog

Enter your choice (1/2/3): 2
Enter the message to decrypt: Khoor Zruog
Enter the shift value used: 3

Decrypted message: Hello World

📦 Requirements

Python 3.x

 Installation

Clone this repository:

cd SCT_CS_1

Run the script as shown above.

🙌 Acknowledgments

Julius Caesar for inspiring this cipher

Cryptography learners and enthusiasts

Anyone exploring the basics of cybersecurity
