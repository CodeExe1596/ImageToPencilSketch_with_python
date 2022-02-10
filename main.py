# Import Modules
import cv2

# Animals assets available
animals = (
    'dog',
    'cat',
    'horse',
    'monkey',
    'fox',
    'lion',
    'squirrel',
    'rabbit'
)

# Asking User to Insert an Animal Name
print('Select your Animal and we will make a pencil Sketch of It.')
for animal in animals :
    print('- ', animal)

user_input = input('What animal did you choose ?   ')

# LowerCase the User Input
user_input = user_input.lower()

# If the Animal is not available ...
while user_input not in animals:

    print('Sorry ! This Animal is not available ! Try Again !')

    print('Select your Animal and we will make a pencil Sketch of It.')

    for animal in animals:
        print('- ' + animal)

    user_input = input('What animal did you choose ?   ')

    user_input = user_input.lower()

# Read the Image File
image = cv2.imread('assets/' + user_input + '.jpg')

# Convert Image from RGB to gray (colorless)
imgToGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the Grayscale
invertGrayImg = 255 - imgToGray

# Making Pencil Sketch by mixing grayscale image with inverted image blurry image
blurredImg = cv2.GaussianBlur(invertGrayImg, (21, 21), 0)

# Invert the Blur
invertBlurredImg = 255 - blurredImg

# Final Result - Pencil Sketch
pencilSketchImg = cv2.divide(imgToGray, invertBlurredImg, scale=260.0)

# Show the "before" and the "after"
cv2.imshow("Before", image)
cv2.imshow("After", pencilSketchImg)
cv2.waitKey(0)