import cv2
import os

# Loading the image
img = cv2.imread(os.path.join('imagess', 'pexels-kirandeepsingh-12469893.jpg'))

# Making the image grayscaled to make the threshold
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Making threshold for the birds
_, img_thresh = cv2.threshold(img_gray, 180, 255, cv2.THRESH_BINARY_INV) # Note: the threshold is inverted because we need the birds to be the white object not the black. 

# Making contour
contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 120: # Filter only non-noise contours

        x, y, w, h = cv2.boundingRect(cnt) # Create bounding boxes around the contour

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)   # rectangle(image, top_left_point, bottom_right_point, colour, stroke_thickness)


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
