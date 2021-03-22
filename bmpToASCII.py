from PIL import Image

imagePath = 'testImage.png'

ASCIICharacters = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", " "]
newWidth = 100

# Resize image maintaining aspect ratio ------> 2 = approx aspect ratiop of unicode character
def resizeImage(image, newWidth = 100):
    width, height = image.size
    aspectRatio = height / width / 2
    newHeight = int(newWidth * aspectRatio)

    resizedImage = image.resize((newWidth, newHeight))
    return(resizedImage)

# Convert to grayscale
def convertToGray(image):
    grayscaleImage = image.convert("L")
    return(grayscaleImage)

# Each pixel to an ascii character
def convertToASCII(image):
    pixels = image.getdata()
    characters = "".join([ASCIICharacters[pixel//25] for pixel in pixels])
    return(characters)

# ASCIIfy the image
def ASCIIfy(newWidth = 100):
    # Open and validate image
    try:
        image = Image.open(imagePath)
    except:
        print(imagePath, "Invalid image")
    
    # Convert image to ASCII
    newImageData = convertToASCII(convertToGray(resizeImage(image)))

    # Format
    pixelCount = len(newImageData)
    outputImage = "\n".join(newImageData[i:(i + newWidth)] for i in range(0, pixelCount, newWidth))

    # Print output
    print(outputImage)

ASCIIfy()