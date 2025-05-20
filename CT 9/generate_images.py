from PIL import Image, ImageDraw, ImageFont
import os

# Create image directory if it doesn't exist
if not os.path.exists('image'):
    os.makedirs('image')

# Define font and size
font = ImageFont.truetype("arial.ttf", 100)

# List of characters to generate
characters = ['A', 'B', 'C', 'D', 'E', '1', '2', '3', '4', '5']

# Generate images for each character
for char in characters:
    # Create a white image with some padding
    img = Image.new('RGB', (150, 150), color = (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Calculate text size
    bbox = draw.textbbox((0, 0), char, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    
    # Draw the character centered
    draw.text(((150-w)//2, (150-h)//2), char, font=font, fill=(0, 0, 0))
    
    # Save the image
    img.save(f'image/{char}.png')
    print(f'Saved image/{char}.png')
