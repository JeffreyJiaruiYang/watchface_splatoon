from PIL import Image, ImageDraw, ImageFont
import os

# Define constants
FONT_PATH = "BlitzBold.otf"  # Replace with the path to your OTF file
IMG_WIDTH = 40
IMG_HEIGHT = 40
POINT_SIZE = 36  # Adjust the font size to fit within 100x100
OUT_DIR = "output_images"
os.makedirs(OUT_DIR, exist_ok=True)

# Characters you want to generate images for
chars = "0123456789"

# Load the font
font = ImageFont.truetype(FONT_PATH, POINT_SIZE)

# Generate PNG images
for char in chars:
    # Create a new image with a transparent background
    image = Image.new('RGBA', (IMG_WIDTH, IMG_HEIGHT), (255, 255, 255, 0))
    
    # Create an ImageDraw object
    draw = ImageDraw.Draw(image)
    
    # Calculate the size of the text using textbbox to get accurate placement
    bbox = draw.textbbox((0, 0), char, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Calculate position to center the text
    x = (IMG_WIDTH - text_width) // 2
    y = (IMG_HEIGHT - text_height) // 2 - bbox[1]  # Adjust for baseline offset
    
    # Draw the text onto the image, vertically adjusted
    draw.text((x, y), char, font=font, fill='white')
    
    # Save the image
    image.save(f"{OUT_DIR}/{char}.png")
