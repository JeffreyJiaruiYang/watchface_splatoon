from PIL import Image, ImageDraw

# Open the image
image = Image.open('2.png').convert("RGBA")

# Create a mask to make a circular image
mask = Image.new("L", image.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)

# Apply the mask to the image
output = Image.new("RGBA", image.size)
output.paste(image, (0, 0), mask=mask)

# Resize the image to 480x480
output = output.resize((480, 480))

# Save the output image with a transparent background
output.save('output_image.png', format="PNG")
