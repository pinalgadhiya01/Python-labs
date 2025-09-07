import cv2

image = cv2.imread(r'C:\Users\Pinal Gadhiya\OneDrive\Pictures\Camera Roll\MU.jpg')

if image is None:
    print("Error: Image not found.")
else:
    # Shape of the image (height, width, channels)
    print("Shape of the image:", image.shape)

    # Dimensions
    height, width, channels = image.shape
    print("Image dimensions: Width =", width, ", Height =", height)
    print("Number of channels:", channels)

    min_blue = image[:, :, 0].min()
    print("Minimum pixel value in Blue channel (B):", min_blue)
