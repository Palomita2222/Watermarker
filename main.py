import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Watermarker")
window.geometry("750x550")
window.configure(bg="#FAF3E0")  # Light beige background

# Styling
style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", font="Calibri 15", background="#FAF3E0", padding=10)
style.configure("TEntry", font="Calibri 18", padding=10)
style.configure("TButton", font="Calibri 15 bold", padding=10, width=20)
style.configure("Title.TLabel", font="Calibri 20 bold underline", background="#FAF3E0")

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

transparency_label = ttk.Label(window, text="Transparency")
transparency_slider = ttk.Scale(window, from_=0, to_=1, orient=tk.HORIZONTAL, length=400)
transparency_slider.set(0.5)
transparency_value = tk.StringVar()
transparency_value_label = ttk.Label(window, textvariable=transparency_value, background="#FAF3E0")
transparency_slider.config(command=lambda val=transparency_slider.get(): update_label(val, transparency_value))

interval_label = ttk.Label(window, text="Distance Between")
interval_slider = ttk.Scale(window, from_=1, to_=5, orient=tk.HORIZONTAL, length=400)
interval_slider.set(1.5)
interval_value = tk.StringVar()
interval_value_label = ttk.Label(window, textvariable=interval_value, background="#FAF3E0")
interval_slider.config(command=lambda val=interval_slider.get(): update_label(val, interval_value))

scale_label = ttk.Label(window, text="Logo Scale")
scale_slider = ttk.Scale(window, from_=0.1, to_=2, orient=tk.HORIZONTAL, length=400)
scale_slider.set(0.3)
scale_value = tk.StringVar()
scale_value_label = ttk.Label(window, textvariable=scale_value, background="#FAF3E0")
scale_slider.config(command=lambda val=scale_slider.get(): update_label(val, scale_value))

rotation_label = ttk.Label(window, text="Rotation Angle")
rotation_slider = ttk.Scale(window, from_=0, to_=360, orient=tk.HORIZONTAL, length=400)
rotation_slider.set(20)
rotation_value = tk.StringVar()
rotation_value_label = ttk.Label(window, textvariable=rotation_value, background="#FAF3E0")
rotation_slider.config(command=lambda val=rotation_slider.get(): update_label(val, rotation_value))

button = ttk.Button(window, text="Watermark", command=watermark)

# Layout using grid
title.grid(row=0, column=0, columnspan=3, pady=20, sticky=tk.EW)
Image.grid(row=1, column=0, sticky=tk.W)
Img_Src.grid(row=1, column=1, padx=10)
Video.grid(row=2, column=0, sticky=tk.W)
Vid_Src.grid(row=2, column=1, padx=10)
Logo.grid(row=3, column=0, sticky=tk.W)
Log_Src.grid(row=3, column=1, padx=10)

transparency_label.grid(row=4, column=0, sticky=tk.W)
transparency_slider.grid(row=4, column=1, padx=10)
transparency_value_label.grid(row=4, column=2)

interval_label.grid(row=5, column=0, sticky=tk.W)
interval_slider.grid(row=5, column=1, padx=10)
interval_value_label.grid(row=5, column=2)

scale_label.grid(row=6, column=0, sticky=tk.W)
scale_slider.grid(row=6, column=1, padx=10)
scale_value_label.grid(row=6, column=2)

rotation_label.grid(row=7, column=0, sticky=tk.W)
rotation_slider.grid(row=7, column=1, padx=10)
rotation_value_label.grid(row=7, column=2)

button.grid(row=8, column=0, columnspan=3, pady=20)

window.mainloop()
