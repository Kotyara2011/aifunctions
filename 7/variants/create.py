# Import the modules you need
import os
from PIL import Image, ImageDraw, ImageFont

# Define the path to your original ad image
original_image = "ad_original.png"

# Define the path to your variants folder
variants_folder = "variants"

# Define the colors for your CTA buttons
colors = ["red", "green"]

# Define the coordinates and size of your CTA button
x1, y1 = 100, 200 # top left corner
x2, y2 = 200, 250 # bottom right corner
width = x2 - x1
height = y2 - y1

# Define the text and font for your CTA button
text = "Buy Now"
font = ImageFont.truetype("arial.ttf", 32)

# Loop through each color and create a variant
for color in colors:
    # Open the original image and create a drawing object
    image = Image.open(original_image)
    draw = ImageDraw.Draw(image)

    # Draw a rectangle with the color and fill it with white
    draw.rectangle([x1, y1, x2, y2], fill="white", outline=color)

    # Draw the text with the color and center it in the rectangle
    text_width, text_height = draw.textsize(text, font=font)
    text_x = x1 + (width - text_width) // 2
    text_y = y1 + (height - text_height) // 2
    draw.text([text_x, text_y], text, fill=color, font=font)

    # Save the variant image in the variants folder with the color name
    variant_image = os.path.join(variants_folder, f"ad_{color}.png")
    image.save(variant_image)

    # Print a message to confirm the creation of the variant
    print(f"Created variant with {color} CTA button: {variant_image}")
