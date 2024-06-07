# PRODIGY_CS_02
Image Encryption and Decryption
This repository contains Python scripts for encrypting and decrypting images using a simple key-based algorithm. The encryption process shifts the RGB values of each pixel by a specified key value, and the decryption process reverses this shift.

Features
Encrypt an image by shifting the RGB values of each pixel.
Decrypt an image by reversing the RGB value shifts.
Save the encrypted and decrypted images with appropriate filenames.
Requirements
Python 3.x
Pillow library (PIL fork)
Installation
Clone this repository to your local machine:
sh
Copy code
Navigate to the project directory:
sh
Copy code
cd image-encryption-decryption
Install the required dependencies:
sh
Copy code
pip install pillow
Usage
Encrypt an Image
To encrypt an image, use the encrypt_image function. The function takes the path to the image file and a key for encryption.

python
Copy code
from encrypt_decrypt import encrypt_image

image_path = "path/to/your/image.png"
encryption_key = 50

encrypted_image = encrypt_image(image_path, encryption_key)
print("Image encrypted:", encrypted_image)
Decrypt an Image
To decrypt an image, use the decrypt_image function. The function takes the path to the encrypted image file and the same key used for encryption.

python
Copy code
from encrypt_decrypt import decrypt_image

encrypted_image_path = "path/to/your/encrypted_image.png"
encryption_key = 50

decrypted_image = decrypt_image(encrypted_image_path, encryption_key)
print("Image decrypted:", decrypted_image)
Example
Here's a full example of how to encrypt and decrypt an image:

python
Copy code
from encrypt_decrypt import encrypt_image, decrypt_image

image_path = "C:\\Users\\harsh\\Desktop\\Intership\\Task 2\\clear.png"
encryption_key = 50

# Encrypt the image
encrypted_image = encrypt_image(image_path, encryption_key)
print("Image encrypted:", encrypted_image)

# Decrypt the image
decrypted_image = decrypt_image(encrypted_image, encryption_key)
print("Image decrypted:", decrypted_image)
File Structure
bash
Copy code
image-encryption-decryption/
│
├── encrypt_decrypt.py    # Contains the encryption and decryption functions
├── README.md             # This README file
└── requirements.txt      # List of dependencies
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
