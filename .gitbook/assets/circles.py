import os
from PIL import Image, ImageDraw, ImageFont

def generate_smooth_badges(start=1, end=30, output_dir="circlemarkers"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # Configuration
    target_size = 24                # Desired output dimensions (64x64)
    scale = 4                       # Upscale multiplier for supersampling
    canvas_size = target_size * scale  # 256x256 internal workspace
    
    bg_color = (255, 255, 255, 0)   # Transparent
    circle_fill = (255, 255, 255)   # White circle
    circle_outline = (0, 0, 0)      # Black outline
    text_color = (0, 0, 0)          # Black text
    
    # Scale up line thickness and text sizes to match the 4x canvas
    outline_width = 3 * scale
    base_font_size = 18 * scale
    
    # Find a valid system font path
    font_path = "arial.ttf"
    try:
        ImageFont.truetype(font_path, 10)
    except IOError:
        try:
            font_path = "DejaVuSans-Bold.ttf"
            ImageFont.truetype(font_path, 10)
        except IOError:
            font_path = None  # Will fallback to default non-scalable font

    for num in range(start, end + 1):
        # 1. Create a massive, high-res canvas
        img_large = Image.new("RGBA", (canvas_size, canvas_size), bg_color)
        draw = ImageDraw.Draw(img_large)
        
        # 2. Add padding on the large canvas to keep the thick outline safe
        padding = 1 
        circle_box = [
            padding, 
            padding, 
            canvas_size - padding, 
            canvas_size - padding
        ]
        
        # 3. Draw the crisp, high-res vector-like shape
        draw.ellipse(circle_box, fill=circle_fill, outline=circle_outline, width=outline_width)
        
        # 4. Handle font sizing dynamically on the large canvas
        current_size = base_font_size
        if num >= 10:
            current_size -= (4 * scale)  # Scale down slightly for double digits
            
        if font_path:
            font = ImageFont.truetype(font_path, current_size)
        else:
            font = ImageFont.load_default()
            
        # 5. Place the text at the absolute center
        center = canvas_size / 2
        draw.text((center, center), str(num), fill=text_color, font=font, anchor="mm")
        
        # 6. Downsample using LANCZOS to blend pixels for perfect anti-aliasing
        img_final = img_large.resize((target_size, target_size), Image.Resampling.LANCZOS)
        
        # 7. Save output
        file_path = os.path.join(output_dir, f"{num}.png")
        img_final.save(file_path, "PNG")
        print(f"Generated smooth badge: {file_path}")

if __name__ == "__main__":
    generate_smooth_badges(1, 50)
    print("\nAll 30 anti-aliased badges generated successfully!")
