import os
import time

def delete_image_after_delay(image_path, delay):
  time.sleep(delay)
  try:
    os.remove(image_path)
    print(f"Image {image_path} deleted after {delay} seconds.")
  except OSError as e:
    print(f"Error deleting image: {e}")

image_path = "decryptedImage.png"
cipher_path1 = "static\\cipher\\cipher.txt"
image_path1 = "static\\cipher\\decryptedimage.png"
cipher_path2 = "static\\cipher\\encrypted.txt"
image_path2 = "static\\cipher\\image.jpg"

delay = 20

delete_image_after_delay(cipher_path1, delay)
delete_image_after_delay(image_path1, delay)
delete_image_after_delay(cipher_path2, delay)
delete_image_after_delay(image_path2, delay)
delete_image_after_delay(image_path, delay)