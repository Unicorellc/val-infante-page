#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Create image with exact LinkedIn preview size
width, height = 1200, 630
image = Image.new('RGB', (width, height), color='#000312')
draw = ImageDraw.Draw(image)

# Add gradient effect by drawing multiple rectangles with alpha
for i in range(height):
    alpha = int(255 * (1 - abs(i - height/2) / (height/2)) * 0.3)
    color = f'#{alpha:02x}FB6B'
    try:
        draw.rectangle([(0, i), (width, i+1)], fill='#00052E')
    except:
        pass

# Try to use system fonts
try:
    font_large = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 90)
    font_medium = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 32)
    font_small = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 48)
    font_tiny = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 18)
except:
    font_large = ImageFont.load_default()
    font_medium = ImageFont.load_default()
    font_small = ImageFont.load_default()
    font_tiny = ImageFont.load_default()

# Colors
green = '#27FB6B'
white = '#FFFFFF'
gray = '#9CA3AF'

# Draw tagline
draw.text((80, 80), 'FINTECH EXECUTIVE & ENTREPRENEUR', fill=green, font=font_tiny)

# Draw name
draw.text((80, 130), 'Val Infante', fill=white, font=font_large)

# Draw subtitle
draw.text((80, 240), "Built America's #1 Fintech", fill=white, font=font_medium)
draw.text((80, 280), "for Immigrants", fill=white, font=font_medium)

# Draw stats boxes
stat_y = 360
stat_spacing = 360

# Stat 1
draw.rectangle([(80, stat_y), (80 + 300, stat_y + 120)], outline=green, width=2)
draw.text((100, stat_y + 20), '1.2M+', fill=green, font=font_small)
draw.text((100, stat_y + 75), 'ACCOUNTS OPENED', fill=gray, font=font_tiny)

# Stat 2
draw.rectangle([(80 + stat_spacing, stat_y), (80 + stat_spacing + 300, stat_y + 120)], outline=green, width=2)
draw.text((100 + stat_spacing, stat_y + 20), '$3B+', fill=green, font=font_small)
draw.text((100 + stat_spacing, stat_y + 75), 'MONEY MOVED', fill=gray, font=font_tiny)

# Stat 3
draw.rectangle([(80 + stat_spacing*2, stat_y), (80 + stat_spacing*2 + 300, stat_y + 120)], outline=green, width=2)
draw.text((100 + stat_spacing*2, stat_y + 20), '$35 CAC', fill=green, font=font_small)
draw.text((100 + stat_spacing*2, stat_y + 75), 'LOWEST IN FINTECH', fill=gray, font=font_tiny)

# Draw footer
draw.text((80, 560), 'CTO · COO · CMO — Building from Zero to Billions', fill=gray, font=font_tiny)
draw.text((980, 560), 'MyBambu', fill=green, font=font_medium)

# Save image
output_path = os.path.join(os.path.dirname(__file__), 'preview.jpg')
image.save(output_path, 'JPEG', quality=95)
print(f'Preview image created: {output_path}')
