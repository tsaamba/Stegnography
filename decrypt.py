import cv2

def decrypt_image(image_path, password):
    img = cv2.imread(image_path)
    d = {chr(i): i for i in range(255)}
    c = {i: chr(i) for i in range(255)}

    message = ""
    n, m, z = 0, 0, 0
    for i in range(img.shape[0] * img.shape[1] * img.shape[2]):
        message += c[img[n, m, z]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    pas = input("Enter passcode for Decryption: ")
    if password == pas:
        print("Decryption message:", message)
    else:
        print("YOU ARE NOT auth")

def main():
    image_path = input("Enter the encrypted image path: ")
    password = input("Enter the passcode: ")

    decrypt_image(image_path, password)

if __name__ == "__main__":
    main()
