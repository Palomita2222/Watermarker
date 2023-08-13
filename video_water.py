from moviepy.editor import VideoFileClip, clips_array
from PIL import Image
import numpy as np

def watermark_video(video_path, logo_image_path, output_video_path, transparency, interval, logo_scale_factor, rotation_angle):
    # Load the video
    video = VideoFileClip(video_path)
    
    # Load the logo and prepare it
    logo = Image.open(logo_image_path).convert("RGBA")
    logo_size = (int(logo.width * logo_scale_factor), int(logo.height * logo_scale_factor))
    logo = logo.resize(logo_size, Image.LANCZOS)
    logo = logo.rotate(rotation_angle, expand=True)
    r, g, b, a = logo.split()
    a = a.point(lambda i: i * transparency)
    logo.putalpha(a)

    # Function to apply watermark to each frame
    def watermark_frame(frame):
        main = Image.fromarray(frame).convert("RGB")
        watermarked = watermark_with_logo_image(main, logo, interval)
        return np.array(watermarked)

    # Apply watermark to video
    watermarked_video = video.fl_image(watermark_frame)
    watermarked_video.write_videofile(output_video_path, codec='libx264')

def watermark_with_logo_image(main, logo, interval):
    main_width, main_height = main.size
    logo_width, logo_height = logo.size

    watermarked = main.copy()
    offset = int(0.5 * logo_width)

    for y in range(0, main_height, int(interval * logo_height)):
        start_x = 0 if (y // (int(interval * logo_height))) % 2 == 0 else offset
        for x in range(start_x, main_width, int(interval * logo_width)):
            watermarked.paste(logo, (x, y), logo)
    
    return watermarked

# Example usage
#watermark_video('video.mp4', 'lays.png', 'output_video.mp4', 0.2, 1, 0.1, 20)