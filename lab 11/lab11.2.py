import cv2

image = cv2.imread(r'C:\Users\Pinal Gadhiya\OneDrive\Pictures\Camera Roll\MU.jpg')

if image is None:
    print("Error: Image not found.")
else:
    padded_image = cv2.copyMakeBorder(
        image,
        top=50,
        bottom=50,
        left=100,
        right=100,
        borderType=cv2.BORDER_CONSTANT,
        value=[0, 0, 0]  
    )

    cv2.imshow("Original Image", image)
    cv2.imshow("Padded Image", padded_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
