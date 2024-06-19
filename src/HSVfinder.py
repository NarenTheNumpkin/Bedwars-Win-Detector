import cv2
import numpy as np


# Callback function for trackbars (does nothing)
def nothing(x):
    pass


# Load an image
image_path = 'mvp.jpg'
image = cv2.imread(image_path)
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Create a window
cv2.namedWindow('Trackbars')

# Create trackbars for lower and upper bounds of H, S, and V
cv2.createTrackbar('Lower H', 'Trackbars', 0, 179, nothing)
cv2.createTrackbar('Lower S', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Lower V', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Upper H', 'Trackbars', 179, 179, nothing)
cv2.createTrackbar('Upper S', 'Trackbars', 255, 255, nothing)
cv2.createTrackbar('Upper V', 'Trackbars', 255, 255, nothing)

while True:
    # Get current positions of the trackbars
    lh = cv2.getTrackbarPos('Lower H', 'Trackbars')
    ls = cv2.getTrackbarPos('Lower S', 'Trackbars')
    lv = cv2.getTrackbarPos('Lower V', 'Trackbars')
    uh = cv2.getTrackbarPos('Upper H', 'Trackbars')
    us = cv2.getTrackbarPos('Upper S', 'Trackbars')
    uv = cv2.getTrackbarPos('Upper V', 'Trackbars')

    # Define the lower and upper bounds for the HSV values
    lower_bound = np.array([lh, ls, lv])
    upper_bound = np.array([uh, us, uv])

    # Create a mask using the bounds
    mask = cv2.inRange(image_hsv, lower_bound, upper_bound)

    # Apply the mask to the original image
    result = cv2.bitwise_and(image, image, mask=mask)

    # Display the original image, mask, and result
    cv2.imshow('Original Image', image)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Destroy all windows
cv2.destroyAllWindows()
