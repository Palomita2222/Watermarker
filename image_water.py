from PIL import Image

def watermark_with_logo(main_image_path, logo_image_path, output_image_path, transparency, interval, logo_scale_factor, rotation_angle):
    # Load the main image and the logo
    main = Image.open(main_image_path).convert("RGB")
    logo = Image.open(logo_image_path).convert("RGBA")  # Keep the alpha channel for transparency

    # Resize the logo
    logo_size = (int(logo.width * logo_scale_factor), int(logo.height * logo_scale_factor))
    logo = logo.resize(logo_size, Image.LANCZOS)
    
    # Rotate the logo
    logo = logo.rotate(rotation_angle, expand=True)

    # Adjust the logo's transparency
    r, g, b, a = logo.split()
    a = a.point(lambda i: i * transparency)
    logo.putalpha(a)

    # Get the dimensions of the main image and the logo
    main_width, main_height = main.size
    logo_width, logo_height = logo.size

    # Create a watermarked version of the main image
    watermarked = main.copy()

    # Tile the logo across the main image
    offset = int(0.5 * logo_width)  # Half the width of the logo for offset

    for y in range(0, main_height, int(interval * logo_height)):
        # If it's an even row, start from 0, else start from the offset
        start_x = 0 if (y // (int(interval * logo_height))) % 2 == 0 else offset
        for x in range(start_x, main_width, int(interval * logo_width)):
            watermarked.paste(logo, (x, y), logo)

    # Save the result
    watermarked.save(output_image_path)

# Example usage
watermark_with_logo('image.jpg', 'lays.png', 'output.jpg', 0.5, 1.5, 0.3, 20)
