import cv2
import matplotlib.pyplot as plt

image = cv2.imread(r'C:\Users\Pinal Gadhiya\OneDrive\Pictures\Camera Roll\MU.jpg')


if image is None:
    print("Image not found.")
else:
    # Convert image from BGR to RGB
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Split RGB channels
    r, g, b = cv2.split(img_rgb)

    # Display channels
    plt.subplot(1, 4, 1)
    plt.imshow(img_rgb)
    plt.title("Original")
    plt.axis('off')

    plt.subplot(1, 4, 2)
    plt.imshow(r, cmap='Reds')
    plt.title("Red")
    plt.axis('off')

    plt.subplot(1, 4, 3)
    plt.imshow(g, cmap='Greens')
    plt.title("Green")
    plt.axis('off')

    plt.subplot(1, 4, 4)
    plt.imshow(b, cmap='Blues')
    plt.title("Blue")
    plt.axis('off')

    plt.tight_layout()
    plt.show()
