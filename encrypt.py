import cv2
import os

def encrypt_image(image_path, message, password):
    img = cv2.imread(image_path)
    d = {chr(i): i for i in range(255)}
    c = {i: chr(i) for i in range(255)}

    n, m, z = 0, 0, 0
    for i in range(len(message)):
        img[n, m, z] = d[message[i]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    cv2.imwrite("encrypted_image.jpg", img)
    os.system("start encrypted_image.jpg")

    return img

def main():
    image_path = input("Enter the image path: ")
    message = input("Enter the secret message: ")
    password = input("Enter a passcode: ")

    encrypt_image(image_path, message, password)

if __name__ == "__main__":
    main()

