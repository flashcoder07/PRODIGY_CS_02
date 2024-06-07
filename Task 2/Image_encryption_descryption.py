
import os
from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = img.load()

    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[x, y] = (r, g, b)

    encrypted_img_path = os.path.join(os.path.dirname(image_path), "encrypted_" + os.path.basename(image_path))
    img.save(encrypted_img_path)
    return encrypted_img_path

def decrypt_image(encrypted_image_path, key):
    img = Image.open(encrypted_image_path)
    img = img.convert('RGB')
    pixels = img.load()

    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[x, y] = (r, g, b)

    decrypted_img_path = os.path.join(os.path.dirname(encrypted_image_path), "decrypted_" + os.path.basename(encrypted_image_path)[len("encrypted_"):])
    img.save(decrypted_img_path)
    return decrypted_img_path

# Example usage
image_path = "C:\\Users\\harsh\\Desktop\\Intership\\Task 2\\clear.png"
encryption_key = 50

encrypted_image = encrypt_image(image_path, encryption_key)
print("Image encrypted:", encrypted_image)

decrypted_image = decrypt_image(encrypted_image, encryption_key)
print("Image decrypted:", decrypted_image)









