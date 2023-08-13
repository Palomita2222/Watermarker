import tkinter as tk
from tkinter import ttk
import image_water
import video_water
from PIL import ImageTk
from PIL import Image as PILImage
import os

window = tk.Tk()
window.title("Watermarker")
window.geometry("750x1100")
window.configure(bg="#FAF3E0")  # Light beige background

# Styling
style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", font="Calibri 15", background="#FAF3E0", padding=10)
style.configure("TEntry", font="Calibri 18", padding=10)
style.configure("TButton", font="Calibri 15 bold", padding=10, width=20)
style.configure("Title.TLabel", font="Calibri 20 bold underline", background="#FAF3E0")


def update_preview(*args):
    try:
        # Generate a preview using the watermark_with_logo function
        temp_output_path = "temp_preview.jpg"
        image_water.watermark_with_logo(Img_Src.get(), Log_Src.get(), temp_output_path, 
                                       transparency_slider.get(), interval_slider.get(), 
                                       scale_slider.get(), rotation_slider.get())
        
        # Load the preview image
        temp_image = PILImage.open(temp_output_path)
        
        # Adjust image dimensions (e.g., reduce size by 20%)
        new_width = int(temp_image.width * 0.5)
        new_height = int(temp_image.height * 0.5)
        temp_image = temp_image.resize((new_width, new_height), PILImage.ANTIALIAS)
        
        # Update the canvas dimensions
        preview_canvas.config(width=new_width, height=new_height)
        
        # Convert to PhotoImage and display on canvas
        temp_photo = ImageTk.PhotoImage(temp_image)
        
        # Clear the previous image
        preview_canvas.delete("all")
        
        # Display the new image centered in the canvas
        preview_canvas.create_image(new_width/2, new_height/2, image=temp_photo)
        preview_canvas.image = temp_photo
    except Exception as e:
        # Let's print the exception for debugging purposes
        print(e)

def save():
    f = open("saves.txt", "w")
    f.write(f"{transparency_slider.get()},{interval_slider.get()},{scale_slider.get()},{rotation_slider.get()}")
    f.close()

def watermark():
    import video_water
    import image_water
    if Img_Src.get() != "":
        if Log_Src.get() != "":
            try:
                image_water.watermark_with_logo(Img_Src.get(), Log_Src.get(), 'output.jpg', transparency_slider.get(), interval_slider.get(), scale_slider.get(), rotation_slider.get())
            except:
                print("Error with the image watermarking.")
    if Vid_Src.get() != "":
        if Log_Src.get() != "":
            try:
                video_water.watermark_video(Vid_Src.get(), Log_Src.get(), 'output_video.mp4', transparency_slider.get(), interval_slider.get(), scale_slider.get(), rotation_slider.get())
            except:
                print("Error with the video watermarking.")


img_src = tk.StringVar()
video_src = tk.StringVar()
logo_src = tk.StringVar()

title = ttk.Label(window, text="Watermarker", style="Title.TLabel")
Image = ttk.Label(window, text="Image Watermark path")
Img_Src = ttk.Entry(window, textvariable=img_src, width=40)
Video = ttk.Label(window, text="Video Watermark path")
Vid_Src = ttk.Entry(window, textvariable=video_src, width=40)
Logo = ttk.Label(window, text="Logo Watermark path")
Log_Src = ttk.Entry(window, textvariable=logo_src, width=40)

# Sliders and their value labels
def update_label(val, var):
    var.set(f"{float(val):.2f}")

if os.path.exists("saves.txt"):
    transparency, interval, scale, rotation = open("saves.txt", "r").read().split(",")
else:
    transparency, interval, scale, rotation = 0,0,0,0

transparency_label = ttk.Label(window, text="Transparency")
transparency_slider = ttk.Scale(window, from_=0, to_=1, orient=tk.HORIZONTAL, length=400)
transparency_slider.set(transparency)
transparency_value = tk.StringVar()
transparency_value_label = ttk.Label(window, textvariable=transparency_value, background="#FAF3E0")
transparency_slider.config(command=lambda val=transparency_slider.get(): update_label(val, transparency_value))

interval_label = ttk.Label(window, text="Distance Between")
interval_slider = ttk.Scale(window, from_=1, to_=5, orient=tk.HORIZONTAL, length=400)
interval_slider.set(interval)
interval_value = tk.StringVar()
interval_value_label = ttk.Label(window, textvariable=interval_value, background="#FAF3E0")
interval_slider.config(command=lambda val=interval_slider.get(): update_label(val, interval_value))

scale_label = ttk.Label(window, text="Logo Scale")
scale_slider = ttk.Scale(window, from_=0.1, to_=2, orient=tk.HORIZONTAL, length=400)
scale_slider.set(scale)
scale_value = tk.StringVar()
scale_value_label = ttk.Label(window, textvariable=scale_value, background="#FAF3E0")
scale_slider.config(command=lambda val=scale_slider.get(): update_label(val, scale_value))

rotation_label = ttk.Label(window, text="Rotation Angle")
rotation_slider = ttk.Scale(window, from_=0, to_=360, orient=tk.HORIZONTAL, length=400)
rotation_slider.set(rotation)
rotation_value = tk.StringVar()
rotation_value_label = ttk.Label(window, textvariable=rotation_value, background="#FAF3E0")
rotation_slider.config(command=lambda val=rotation_slider.get(): update_label(val, rotation_value))

button = ttk.Button(window, text="Watermark", command=watermark)
save = ttk.Button(window, text="Save ", command=save)


# Binding the update_preview function
Img_Src.bind("<KeyRelease>", update_preview)
Log_Src.bind("<KeyRelease>", update_preview)
transparency_slider.bind("<B1-Motion>", update_preview)
interval_slider.bind("<B1-Motion>", update_preview)
scale_slider.bind("<B1-Motion>", update_preview)
rotation_slider.bind("<B1-Motion>", update_preview)
title.grid(row=0, column=0, columnspan=3, pady=20)
Image.grid(row=1, column=0)
Img_Src.grid(row=1, column=1, padx=10)
Video.grid(row=2, column=0)
Vid_Src.grid(row=2, column=1, padx=10)
Logo.grid(row=3, column=0)
Log_Src.grid(row=3, column=1, padx=10)

transparency_label.grid(row=4, column=0)
transparency_slider.grid(row=4, column=1, padx=10)
transparency_value_label.grid(row=4, column=2)

interval_label.grid(row=5, column=0)
interval_slider.grid(row=5, column=1, padx=10)
interval_value_label.grid(row=5, column=2)

scale_label.grid(row=6, column=0)
scale_slider.grid(row=6, column=1, padx=10)
scale_value_label.grid(row=6, column=2)

rotation_label.grid(row=7, column=0)
rotation_slider.grid(row=7, column=1, padx=10)
rotation_value_label.grid(row=7, column=2)


# Image Preview Canvas
canvas_width = 400  # or any suitable width
canvas_height = 400  # or any suitable height
preview_canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg='white')
preview_canvas.grid(row=10, column=0, columnspan=3, padx=10, pady=10)

button.grid(row=8, column=0, columnspan=3, pady=20)
save.grid(row=9, column=0, columnspan=3, pady=20)

window.mainloop()